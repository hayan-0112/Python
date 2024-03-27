import socket
import cv2
import numpy
from queue import Queue
from _thread import *
enclosure_queue = Queue() #큐 공간의 이름 : enclosure_queue

def threaded(client_socket, addr, queue):
    print('Connected by :', addr[0], ':', addr[1])
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1]) #굳이 'addr[1]'에서 1이 아니어도 됨. a 나 x 나 등등 다른 것도 가능
                break
            stringData = queue.get() #queue로 가져오기
            client_socket.send(str(len(stringData)).ljust(16).encode()) #ljust : 왼쪽부터 정렬 // encode 해서 전송 <-> decode 해서 받기
            client_socket.send(stringData)
        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0], ':', addr[1])
            break
    client_socket.close()
counnt = 0

def webcam(queue):
    global counnt
    video_path = 'pexels-skymax-9129254 (2160p).mp4'
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        if ret == False:
            continue
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90] #90: JPEG 이미지를 인코딩할 때 사용되는 압축 품질(Quality)
                                                           #중간 정도의 품질(보통 이미지의 품질을 충분히 유지하면서도 파일 크기를 상대적으로 작게 유지할 수 있는 값)
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)
        data = numpy.array(imgencode)
        stringData = data.tostring()
        if counnt == 0:
            print(stringData) #0일 때 stringData 출력
        counnt = 1 #1일 때 종료
        queue.put(stringData) #queue 안에 담아 놓는다
        cv2.imshow('server', frame)
        key = cv2.waitKey(1)
        if key == 27: # 27 = esc 키 버튼
            break
HOST = '192.168.31.53'
PORT = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #'socket.SO_REUSEADDR = 1' 똑같은 주소에 다시 접속해도 timewait 안 걸리고 바로 송출 가능
server_socket.bind((HOST, PORT))
server_socket.listen()
print('server start')
start_new_thread(webcam,(enclosure_queue,)) #서버의 웹캠 먼저 on
while True:
    print('wait')
    client_socket, addr = server_socket.accept()
    start_new_thread(threaded, (client_socket, addr, enclosure_queue,))
server_socket.close()