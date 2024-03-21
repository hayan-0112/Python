import socket #통신 소켓 TCP / UDP

from threading import Thread #동시 처리를 위해 thread 사용

import tkinter #파이썬 내장 GUI 개발 라이브러리

tk = tkinter.Tk() #메인프레임 선언 new FROM()
tk.geometry("1000x1000") #해상도 설정
entry = tkinter.Entry(tk) #entry식별자에서 tkinter에서 제공하는 Entry (텍스트입력상자)
entry2 = tkinter.Listbox(tk, height=15, width=50) #대화창 목록 리스트박스 생성
#localhost : 내 로컬 환경 ip를 의미
#127.0.0.1 : 내 로컬 환경 ip를 의미
HOST = '192.168.31.53'    # 내가 접속할 서버의 ip주소
PORT = 9900        # 서버의 포트 번호 (서로 같아야 연결 가능)
def rcvMsg(sock):
    while True: #무한루프
        try:
            data = sock.recv(1024) # 1024 단위로 자른 데이터를 받는다.
            if not data: #data가 없으면
                break #탈출한다.
            print(data.decode()) #리시브 받은 데이터를 콘솔에 출력한다. decode 로 풀어서 출력
            entry2.insert(-1,data.decode()+"\n") #'-1' : 맨 뒤 // 맨 뒤에 데이터를 추가하겠다. 그리고, 줄바꿈
            entry2.update() #인서트 결과 반영
            entry2.see(0) #실행시켰을 때 최신 메시지(읽을 메시지)가 맨 위에 출력된다.(맨 첫번째 자리에 출력)
        except: #예외
            tk.destroy() #form1.dispose() #form1.close()
            pass

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: #소켓 객체 sock 생성
        sock.connect((HOST, PORT)) #소켓을 통해 connect 메서드 호출
        t = Thread(target=rcvMsg, args=(sock,)) #쓰레드를 생성하고 쓰레드로 rcvMsg함수를 구동시키고, 매개변수는 sock객체 지정
        t.daemon = True#데몬스레드로 설정해서 메인스레드가 종료되면 자동으로 함꼐 종료, 프로세스 묶이는 문제 방지
        t.start()

        def okClick():
            sock.send(entry.get().encode()) #entry박스 값을 소켓에 인코딩 후 전송

        def onEnter(event):
            okClick()
            entry.delete(0,tkinter.END) #처음부터 끝까지(0: 처음 / thinter.END : 끝) --> entry 박스 값 지우기

        entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
        #pack함수 : 배치를 위한 함수 // fill : 채우는 함수
        label = tkinter.Label(tk, text="채팅")
        entry.pack()
        label.pack()
        btn = tkinter.Button(tk, text="OK", command=okClick)
        btn.pack()
        entry.bind("<Return>", onEnter) #Return은 엔터키를 의미
        tk.mainloop() #mainloop 위에서 만든 tk_form을 구동시킨다
        #mainloop는 스레드 점유한다.(=스레드가 갇힌 상태)
        #ex) print("123") ---> 영원히 출력 안 됨.

runChat()