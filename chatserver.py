import socketserver
import threading

HOST = '192.168.31.88'
PORT = 9900
lock = threading.Lock()


class UserManager:
    def __init__(self):
        self.users = {} # client side를 통해 접속한 유저 객체를 담는 변수

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
        self.sendMessageToAll('[%s] 퇴장.' % username)


    def messageHandler(self, username, msg): # 서버가 유저를 강제 퇴장시킬 수 있는 기능 구현 가능한 부분
        if msg[0] != '/': #원래는 귓속말 부분
            self.sendMessageToAll('[%s] %s' % (username, msg)) #전체 채팅 / 귓속말 했을 시, 귓속말을 하고자 하는 유저에게 메시지 전송하는 기능
            return

        if msg.strip() == '/quit':
            self.removeUser(username)
            return -1

    def sendMessageToAll(self, msg): # echo 역할(모두에게 메시지를 뿌려주는 역할)
        for conn, addr in self.users.values():
            conn.send(msg.encode())

# 귓속말 당한 유저에게만 메시지 받는 함수 구현 가능

class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()


    def handle(self):
        print(self,"self memory")
        print('client [%s] 연결' % self.client_address[0])
        try:
            username = self.registerUsername()
            print(username,":username")
            msg = self.request.recv(1024)
            print(self.request)
            print(self.client_address)
            print(self.server)
            while msg:
                print(msg.decode())
                if self.userman.messageHandler(username, msg.decode()) == -1: #msg.decode()의 값이 없으면 'return = -1' 이 나옴 --> '/quit'  --> 퇴장
                    self.request.close()
                    break
                msg = self.request.recv(1024)
        except Exception as e:
            print(e)

        print('[%s]종료' % self.client_address[0])
        self.userman.removeUser(username)
    def registerUsername(self):
        while True:
            self.request.send('ID'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip() #strip() : 공백 제거
            if self.userman.addUser(username, self.request, self.client_address):
                return username

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



