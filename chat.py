import random
import socketserver
import threading
import time

HOST = '192.168.31.53'
PORT = 9900
lock = threading.Lock()
userlist = ["김중규", "정재현", "허민재", "이윤서", "윤하얀", "전준용", "윤석현",
            "박희창", "진정현", "김지욱", "성재민", "강병헌", "김자연", "김영기"]
admin = ["admin"]
filePath = "CussWord.txt"

class UserManager():
    def __init__(self):
        self.users = {} # client side를 통해 접속한 유저 객체를 담는 변수
        self.per = True
    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send('already exist.\n'.encode())
            return None
        lock.acquire() #thread의 lock객체는 공유데이터를 다룰 때 스레드를 독립성을 보장('lock'으로 스레드를 묶음)
        self.users[username] = (conn, addr) #튜플
        lock.release() #독립성 보장해야하는 작업이 끝나면 release 로 풀어 준다.
        self.sendMessageToAll('[%s] 입장' % username)
        return username

    def removeUser(self, username):
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessageToAll('[%s] 퇴장' % username)

    def forced_exit(self, username):
        if username not in self.users: #현재 서버가 관리하고 있는 접속자 목록 중 username이 있는지
            return
        userlist.remove(username)
        self.users[username][0].close()

    def messageHandler(self, username, msg): # 서버가 유저를 강제 퇴장시킬 수 있는 기능 구현 가능한 부분
        if msg[0] != '/' and self.per: #원래는 귓속말 부분
            self.sendMessageToAll('[%s] %s' % (username, msg)) #전체 채팅 / 귓속말 했을 시, 귓속말을 하고자 하는 유저에게 메시지 전송하는 기능
            return
        else: #메시지가 /로 시작한다면 조건
            if msg[0:2] == '/o' and username == 'admin': #admin이 /o를 입력했을 때
                self.name = msg[3] + msg[4] + msg[5]
                self.sendMessageToAll("[%s]님이 강제퇴장하셨습니다." % self.name)
                self.forced_exit(self.name)
            elif msg[0:2] == '/i' and username == 'admin':
                self.name = msg[2:5]
                userlist.append(self.name)
            elif msg[0:2] == '/n' and username == 'admin':
                self.sendMessageToAll("[공지사항]: %s" % msg[2:])
            elif msg[0:2] == '/b' and username == 'admin':
                if self.per:
                    self.per = False
                    return
                else:
                    self.per = True
            elif msg[0:2] == '/w':
                self.name = msg[3] + msg[4] + msg[5]
                if self.name in userlist or self.name in 'admin':
                    tmp = msg.split()
                    str1 = self.name + ">>>" #self.name : 받는 사람 이름
                    str2 = username + '>>>' #username : 보내는 사람 이름
                    for i in range(2,len(tmp)):
                        str1 += tmp[i] + ' '
                        str2 += tmp[i] + ' '
                    self.recUserMessage(username, str1) #보내는 사람 >>> 멘트
                    self.sendUserMessage(self.name, str2) #받는 사람 >>> 멘트
                    return
                else:
                    self.users[username][0].send("없는 유저 입니다.".encode())
                    return

    def sendMessageToAll(self, msg): # echo 역할(모두에게 메시지를 뿌려주는 역할)
        for conn, addr in self.users.values():
            conn.send(msg.encode())

# 귓속말 당한 유저에게만 메시지 보이게 하는 함수
    def recUserMessage(self, target_username, msg): #귓속말 받는 사람 함수
        self.users[target_username][0].send(msg.encode())

    def sendUserMessage(self, sender_username, msg): #귓속말 보내는 사람 함수
        self.users[sender_username][0].send(msg.encode())

class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()

    def handle(self):
        print(random.sample([1,2,3,4,5,6], k=1)) #request 객체별로 구분되는 코드 영역
        print(self,"self memory")
        print('client [%s] 연결' % self.client_address[0])


        f = open(filePath, 'r', encoding='UTF8')
        lines = f.read().split(' ')
        try:
            self.latest = 0
            username = self.registerUsername() #id 받는 부분
            print(username, ":username")
            #msg = self.request.recv(1024) #첫 번째 메세지 받는 부분 / 첫 번째 메시지만 따로 받을 이유 x
            #print(self.request)
            #print(self.client_address)
            #print(self.server)
            while 1:
                msg = self.request.recv(1024)
                print(msg.decode()) #decode : 바이트 -> 문자열
                message = str(msg, "utf-8")
                x = ""

                for i in range(len(lines)):
                    if lines[i] in message:
                        self.request.send("욕설금지".encode())
                        x = "메시지"
                if x == "메시지":
                    continue

                if time.time() - self.latest >= 0.5:
                    self.latest = time.time()
                    if self.userman.messageHandler(username, msg.decode()) == -1: #msg.decode()의 값이 없으면 'return = -1' 이 나옴 --> '/quit'  --> 퇴장
                        self.request.close()
                        break

                else:
                    self.latest = time.time()
                    self.request.send("도배금지".encode()) #encode : 문자열 -> 바이트



                #msg = self.request.recv(1024) #두 번째 ~ n번째 메세지 받는 부분
        except Exception as e:
            print(e)

        print('[%s]종료' % self.client_address[0])
        self.userman.removeUser(username)
    def registerUsername(self):
        self.request.send('ID'.encode())  # 요청
        while True:
            username = self.request.recv(1024) #답변
            username = username.decode().strip() #strip() : 공백 제거
            ############################################################################
            if username in userlist or username in admin:
                if self.userman.addUser(username, self.request, self.client_address):
                    return username
            else:
                self.request.send("ID 다시 입력:".encode())

class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
def runServer():
    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('서버종료')
        server.shutdown()
        server.server_close()
runServer()