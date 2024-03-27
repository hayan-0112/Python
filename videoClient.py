import socket
import numpy as np
import cv2

def recvall(sock, count):
    buf = b'' #데이터를 수신하는 동안 해당 변수에 데이터가 누적 // buf는 데이터를 수신하기 위한 임시 저장소 역할
    while count:
        newbuf = sock.recv(count) #newbuf : 현재 수신한 데이터의 길이
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf) #이 count는 아직 수신해야 할 데이터의 총 길이 // 아직 수신해야 할 데이터의 양이 줄어들었음을 의미
    return buf

HOST = '192.168.31.53'
PORT = 9999
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
count = 0
while True:
    message = '1'
    client_socket.send(message.encode())
    length = recvall(client_socket, 16) #16바이트씩 전송받기 // 클라이언트가 수신하는 데이터의 길이 // 1. 프레임 정보 먼저 받기
    #print(length)
    stringData = recvall(client_socket, int(length)) #실제 이미지 데이터 값 // 2. 실제 데이터 정보 받기
    data = np.frombuffer(stringData, dtype='uint8') #numpy로 바꿔서 실제 픽셀 값 얻을 수 있음 // 2. 실제 데이터 정보 받기
    if count == 0:
        print(length, "len")
        print(stringData, "std")
        print(data) #JPEG 이미지의 데이터를 나타내는 NumPy 배열
        print(type(data))
        for i in data:
            count += 1
            print(i)
            print(count, ":c\n")
    decimg = cv2.imdecode(data, 1) #1: 디코딩된 이미지를 컬러로 처리하겠다는 의미
    cv2.imshow('client', decimg)
    key = cv2.waitKey(1)
client_socket.close()