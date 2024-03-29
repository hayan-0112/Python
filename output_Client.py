import socket
import tkinter
import numpy as np
import cv2
import tkinter as tk
import threading as th
import PIL.Image, PIL.ImageTk
import queue as que

root = tk.Tk()
result_img = 0
xml = 'haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(xml)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def video_output():
    HOST = '192.168.31.53'
    PORT = 9999
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    global result_img
    count = 0
    while True:
        message = '1'
        client_socket.send(message.encode())
        length = recvall(client_socket, 16)
        stringData = recvall(client_socket, int(length))
        data = np.frombuffer(stringData, dtype='uint8')
        if count == 0:
            print(length, "len")
            print(stringData, "std")
            print(type(data))
            for i in data:
                count += 1
                print(i)
                print(count, ":c\n")
        decimg = cv2.imdecode(data, 1)
        result_img = decimg
        #reuslt_img = queue.get()
    client_socket.close()

class WebcamEditor:
    def __init__(self, master):
        self.master = master
        self.master.geometry("650x500")
        self.master.title("Webcam")
        self.delay = 15
        self.flag = 0
        self.angle = 0

        self.webcam = tk.Canvas(self.master, width=600, height=450)
        self.webcam.pack()
        self.update()
        self.load_label1 = tk.Label(self.master, width=20, height=5)
        self.load_label1.pack()

        self.load_button1 = tk.Button(self.load_label1, text="오목거울", command=self.flag_change2)
        self.load_button1.pack(side="left")

        self.load_button2 = tk.Button(self.load_label1, text="색상반전", command=self.flag_change1)
        self.load_button2.pack(side="left")

        self.load_button2 = tk.Button(self.load_label1, text="색상 + 풍차", command=self.flag_change3)
        self.load_button2.pack(side="left")

        self.load_button3 = tk.Button(self.load_label1, text="원상복귀", command=self.flag_change0)
        self.load_button3.pack(side="left")
        self.entry = tkinter.Entry(self.master,width=30)
        self.entry.pack()
        self.webcam.focus_set()
        self.webcam.bind("<Button-1>", self.func1)

    def flag_change0(self):
        self.flag = 0

    def flag_change1(self):
        self.flag = 1

    def flag_change2(self):
        self.flag = 2

    def flag_change3(self):
        self.flag = 3

    def color_change(self, frame):
        if frame is not None:
            image = frame
            gary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            invert_image = np.invert(gary_image)
            frame = invert_image
            return frame

    def zoon_out(self, frame):
        if frame is not None:
            rows, cols = frame.shape[:2] #너비 추출

            exp = 0.6 #오목 지수
            scale = 1.3 #변환 영역 크기

            map_y, map_x = np.indices((rows, cols), dtype = np.float32) # x좌표와 y좌표를 담고 있는 매핑 배열 생성
            # 이미지의 각 픽셀을 변형할 위치를 정의하고, 이를 기반으로 이미지 변환 작업을 수행

            # 좌상단 기준좌표(원점)에서 -1~1로 정규화된 중심점 기준 좌표로 변경
            #이미지 픽셀 좌표를 일반화하여 [-1,1] 범위로 정규화하는 연산
            #이미지의 중앙을 (0, 0)으로 두기 위해서 좌표의 값을 -1 ~ 1로 정규화해야 한다.
            map_x = 2 * map_x / (cols-1) - 1
            map_y = 2 * map_y / (rows-1) - 1
            #이미지의 처리에서 편리하고 효율적인 작업을 위해 정규화를 함

            # 직교좌표(원점)를 극 좌표(이미지 중앙)로 변환 / r: 각 픽셀의 중심으로부터의 거리 , theta: 각 픽셀의 중심에서 x축까지의 각도를 나타내는 배열
            r, theta = cv2.cartToPolar(map_x, map_y)
            #반지름(r)과 각도(θ)로 나타내는 좌표 시스템 --> 직교좌표계보다 극좌표계에서 표현하는 것이 더 쉽기 때문(극 좌표계는 원의 중심으로 하여 좀 더 직관적으료 표현 가능) --> 특정 효과를 적용하기 위함

            # 왜곡 영역만 중심 축소 지수 적용
            # 거리(r)가 특정 값(scale)보다 작은 픽셀들의 거리(r)를 제곱하는 연산을 수행
            r[r < scale] = r[r < scale] ** exp # r[r < scale]는 r 배열에서 scale보다 작은 값을 가지는 요소들로 이루어진 배열을 선택
            #이후에 선택된 요소들에 대해서는 제곱 연산을 수행하여 거리를 변형시킴
            #결과적으로 r 배열에서 scale보다 작은 값들의 거리를 제곱하여 강조하는 효과를 얻게 된다.

            # 극 좌표를 직교좌표로 변환
            map_x, map_y = cv2.polarToCart(r, theta)
            # 이미지를 표현할 때에는 각도와 거리가 아닌 x와 y좌표를 이용한 직교좌표를 이용하여 처리하기 때문에 다시 직교좌표계로 바꿔줘야 함

            # 중심점 기준에서 좌상단(원점) 기준으로 변경
            map_x = ((map_x + 1) * cols-1)/2
            map_y = ((map_y + 1) * rows-1)/2
            # 좌상단을 원점으로 하는 좌표 시스템을 기준으로 동작하기 때문에 직교좌표 중심점 기준에서 다시 원점인 좌상단 기준으로 변경

            # 재매핑 변환
            distorted = cv2.remap(frame, map_x, map_y, cv2.INTER_LINEAR)
            #중심 축소 효과를 포함하여 이미지에 효과를 적용하기 위해 재매핑
            return distorted

            # #frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
            # #faces = eye_cascade.detectMultiScale(frame_gray, 1.05, 5)
            # height, width = frame.shape[:2]
            # center = (width//2, height//2)
            # self.angle = (self.angle+1) % 360
            # #각도를 1씩 증가시키고, 그 값이 360을 넘어가면 다시 0부터 시작하여 각도를 계속 유지 --> 0~359까지 유지하며 계속 회전 가능
            #
            # rotation_matrix = cv2.getRotationMatrix2D(center, self.angle, 1)
            # rotated_frame = cv2.warpAffine(frame, rotation_matrix, (width, height))
            # return rotated_frame

    def color_and_rotate(self, frame):
        if frame is not None:
            image = frame
            gary_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            invert_image = np.invert(gary_image)
            frame = invert_image

            height, width = frame.shape[:2]
            center = (width // 2, height // 2)
            self.angle = (self.angle + 1) % 360
            #각도를 1씩 증가시키고, 그 값이 360을 넘어가면 다시 0부터 시작하여 각도를 계속 유지 --> 0~359까지 유지하며 계속 회전 가능

            rotation_matrix = cv2.getRotationMatrix2D(center, self.angle, 1) #이미지나 객체를 회전하기 위한 변환 매트릭스를 생성
            rotated_frame = cv2.warpAffine(frame, rotation_matrix, (width, height)) #실제 이미지 회전
            return rotated_frame

    def func1(self, e):
        vid2 = cv2.cvtColor(vid, cv2.COLOR_RGB2BGR)
        cv2.imwrite(f'{self.entry.get()}.png', vid2)

    def update(self):
        global vid
        try:
            vid = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
            if self.flag == 1:
                vid = self.color_change(vid)
            elif self.flag == 2:
                vid = self.zoon_out(vid)
            elif self.flag == 0:
                self.flag = 0
            elif self.flag == 3:
                vid = self.color_and_rotate(vid)

            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(vid))
            self.webcam.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
        except:
            pass
        self.master.after(self.delay, self.update)
        #queue.put()

if __name__ == "__main__":
    csv_webcamEditor = WebcamEditor(root)
    t = th.Thread(target=video_output, args=())
    t.daemon = True
    t.start()
    root.mainloop()

# cap = cv2.VideoCapture(0)
# while True:
#     rt, frame = cap.read()
#     if rt:
#         res1=np.fliplr(frame) #좌우반전
#         if res1.shape[:][1]%2 != 0:
#             res1=res1[:,:-1]
#         height, width = res1.shape[:2]
#         width2 = width//2
#         res2=res1[:,:width2]
#         res1[:,width2:] = np.fliplr(res2)
#         cv2.imshow('ress', res1)
#         cv2.waitKey(1)