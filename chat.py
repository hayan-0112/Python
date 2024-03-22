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
        self.user_list_str = "^^" #실시간 접속자 목록을 담은 문자열을 첫글자 ^^로 시작해서 만드는 변수
        for key in self.users.keys(): #실시간 self.users 딕셔너리에서 사용자 이름만 뜯어서 문자열로 만드는 과정
            self.user_list_str += " " + key
        self.sendMessageToAll(self.user_list_str)
        #모든 접속 중인 클라이언트 객체들에게 위에서 만든 명부 문자열을 송출하는 함수 호출
        return username

    def removeUser(self, username):
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessageToAll('[%s] 퇴장' % username)
        self.user_list_str = "^^" #실시간 접속자 목록을 담은 문자열을 첫글자 ^^로 시작해서 만드는 변수
        for key in self.users.keys(): #실시간 self.users 딕셔너리에서 사용자 이름만 뜯어서 문자열로 만드는 과정
            self.user_list_str += " " + key
        self.sendMessageToAll(self.user_list_str)

    def forced_exit(self, username):
        if username not in self.users: #현재 서버가 관리하고 있는 접속자 목록 중 username이 있는지
            return
        self.users[username][0].close()
        userlist.remove(username)
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessageToAll("[%s] 강제퇴장 당하셨습니다." % username)
        self.user_list_str = "^^"  # 실시간 접속자 목록을 담은 문자열을 첫글자 ^^로 시작해서 만드는 변수
        for key in self.users.keys():  # 실시간 self.users 딕셔너리에서 사용자 이름만 뜯어서 문자열로 만드는 과정
            self.user_list_str += " " + key
        self.sendMessageToAll(self.user_list_str)

    def messageHandler(self, username, msg): #강퇴하기나 이런 명령 여기서 하기
        try:
            splMsg = msg.split()
            if msg[0] != '/' and self.per: #일반 메세지 부분
                self.sendMessageToAll('[%s] %s' % (username, msg))
                return
            else: # /command 형태의 특수 메세지
                if splMsg[0] == "/o" and username == "admin":
                    self.name = splMsg[1]
                    self.forced_exit(self.name)
                    print(self.name)
                elif splMsg[0] == "/b" and username == "admin":
                    if (self.per):
                        self.per = False
                        self.sendMessageToAll("채팅이 비활성화 됩니다.")
                        return
                    elif (self.per == False):
                        self.per = True
                        self.sendMessageToAll("채팅이 활성화 됩니다.")
                        return
                elif splMsg[0] == "/n" and username == "admin" and self.per:
                    tmp = msg.strip('/n')
                    print(tmp)
                    self.sendMessageToAll('%s %s' % ("[전체공지]", tmp))
                    return

                elif splMsg[0] == "/i" and username == "admin":
                    self.name = splMsg[1]
                    if self.name not in userlist:
                        userlist.append(self.name)
                    print(self.name)

                elif splMsg[0] == "/w":
                    self.name = splMsg[1]
                    if self.name in userlist or self.name in admin:
                        tmp = msg.split()
                        str1 = self.name + " <<< "
                        str2 = username + " >>> "
                        for i in range(2, len(tmp)):
                            str1 += tmp[i]+ " "
                            str2 += tmp[i]+ " "
                        self.recUserMessage(username, str1)
                        self.sendUserMessage(self.name, str2)
                        return
                    else:
                        self.users[username][0].send("잘못된 유저에게 전송 시도 하였습니다.".encode())
                        return
                elif splMsg[0] == "/차단":
                    self.name = splMsg[1]
                    self.block_list.append(self.name)
                elif splMsg[0] == "/차단해제":
                    self.name = splMsg[1]
                    self.block_list.remove(self.name)
            if msg.strip() == '/quit':
                self.removeUser(username)
                return -1
        except Exception as e:
            print(e)


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
        while True:
            self.request.send('ID를 입력해주세요'.encode())  # 요청
            username = self.request.recv(1024) #답변
            username = username.decode().strip() #strip() : 공백 제거
            ############################################################################
            if username in userlist or username in admin:
                if self.userman.addUser(username, self.request, self.client_address):
                    return username
            else:
                self.request.send("다시 입력해주세요".encode())

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