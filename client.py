import socket #통신 소켓 TCP / UDP

from threading import Thread #동시 처리를 위해 thread 사용

import tkinter #파이썬 내장 GUI 개발 라이브러리

tk = tkinter.Tk() #메인프레임 선언 new FROM()
tk.geometry("600x800") #해상도 설정
stringv = tkinter.StringVar()
stringv2 = tkinter.StringVar()
entry = tkinter.Entry(tk, textvariable=stringv) #entry식별자에서 tkinter에서 제공하는 Entry (텍스트입력상자)
entry2 = tkinter.Listbox(tk, height=10, width=50) #대화창 목록 리스트박스 생성
entry3_info = tkinter.Entry(tk, width=20)
entry4_person = tkinter.Listbox(tk, height=10, width=30)
entry5 = tkinter.Entry(tk, width=20)
#localhost : 내 로컬 환경 ip를 의미
#127.0.0.1 : 내 로컬 환경 ip를 의미
HOST = '192.168.31.53'    # 내가 접속할 서버의 ip주소
PORT = 9900        # 서버의 포트 번호 (서로 같아야 연결 가능)

def get_selection(event):
    global stringv
    try:
        index = entry2.curselection()[0]
        value = entry2.get(index)
        splitValue = value.split()
        # print("귓속말 => ", value)
        # if ">>>" in value:
        #     entry.insert(0,"/w ")
        #     cell = value[0] + value[1] + value[2]
        #     entry.insert(3, cell + " ")
        #     tk.after(1, entry.focus_set)
        if splitValue[1] == ">>>":  # entry.icursor(tkinter.END)
            entry.delete(0, tkinter.END)
            stringv.set("/w "+splitValue[0]+" ")
            entry.icursor(len(entry.get())+1)
            tk.after(1, entry.focus_set)
    except Exception as e:
        print(e)


def get_selection2(event):
    global stringv
    try:
        idx = entry4_person.curselection()[0]
        value = entry4_person.get(idx)
        entry.delete(0, tkinter.END)
        stringv.set("/w " + value + " ")
        entry.icursor(len(entry.get()) + 1)
        tk.after(1, entry.focus_set())
    except Exception as e:
        print(e)

def rcvMsg(sock):
    while True: #무한루프
        try:
            data = sock.recv(1024) # 1024 단위로 자른 데이터를 받는다.

            if " " in data.decode():
                splitData = data.decode().split()
            color = ["red", "blue", "grey", "green"]
            print(data.decode()) #리시브 받은 데이터를 콘솔에 출력한다. decode 로 풀어서 출력
            if data:
                if splitData[1] == ">>>" or splitData[1] == "<<<":
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0, {'fg': color[3]})
                elif splitData[0] == "[전체공지]":
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0, {'fg': color[1]})
                elif splitData[1] == "입장" or splitData[1] == "퇴장." or splitData[0] == "채팅이":
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0, {'fg': color[2]})
                elif splitData[1] == "강제퇴장":  # 강제퇴장 메세지 받은 경우
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0, {'fg': color[0]})
                elif splitData[0] == "^^":  # 실시간 접속 명부 데이터임
                    entry4_person.delete(0, tkinter.END)
                    for i in range(1, len(splitData)):
                        entry4_person.insert(-1, splitData[i] + "\n")
                else: #일반 메세지
                    entry2.insert(-1, data.decode() + "\n")
                    entry2.itemconfig(0,{'fg':'black'})
            #entry2.insert(-1,data.decode()+"\n") #'-1' : 맨 뒤 // 맨 뒤에 데이터를 추가하겠다. 그리고, 줄바꿈
            entry2.update() #인서트 결과 반영
            entry2.see(0) #실행시켰을 때 최신 메시지(읽을 메시지)가 맨 위에 출력된다.(맨 첫번째 자리에 출력) #0번째 관점을 맞추겠다
            entry4_person.update()
            entry4_person.see(0)
        except: #예외
            tk.destroy() #form1.dispose() #form1.close()
            pass

def runChat():
    try:
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

            def out():
                tk.destroy()

            def forced_exit_Click():
                sock.send(("/o " + entry3_info.get()).encode())

            def forced_exit_lifted_Click():
                sock.send(("/i " + entry3_info.get()).encode())

            def btn_enable_chat_Click():
                sock.send("/b".encode())

            def btn_notice_chat_Click():
                sock.send(("/n " + entry5.get()).encode())

            # def ice_on_off():
            #     if chat.admin[0]:
            #         if btn_ice["active"] == "normal":
            #             entry2.config(state="disable")
            #         else:
            #             pass
            #
            # def force_out():
            #     if chat.admin[0]:
            #         for i in chat.userlist:
            #             if chat.userlist[i] in entry:
            #                 chat.userlist[i].remove()
            #                 #.send("%s 가 강퇴되었습니다." % chat.userlist[i])

            entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
            # pack함수 : 배치를 위한 함수 // fill : 채우는 함수
            label = tkinter.Label(tk, text="채팅")
            entry.pack()
            label.pack()
            btn = tkinter.Button(tk, text="OK", command=okClick)
            btn.pack()
            entry.bind("<Return>", onEnter)  # Return은 엔터키를 의미
            entry2.bind("<<ListboxSelect>>", get_selection)
            entry4_person.bind("<<ListboxSelect>>", get_selection2)
            btn_out = tkinter.Button(tk, text="나가기", command=out, pady=5)
            btn_out.pack(pady=5)
            entry3_info.pack(pady=5)
            btn_forced_exit = tkinter.Button(tk, text="강제퇴장", command=forced_exit_Click)
            btn_forced_exit.pack(pady=5)
            btn_forced_exit_lifted = tkinter.Button(tk, text="강제퇴장 해제", command=forced_exit_lifted_Click)
            btn_forced_exit_lifted.pack(pady=5)
            btn_enable_chat = tkinter.Button(tk, text="채팅 활성화/비활성화", command=btn_enable_chat_Click)
            btn_enable_chat.pack(pady=5)
            btn_notice_chat = tkinter.Button(tk, text="공지하기", command=btn_notice_chat_Click)
            entry5.pack()
            btn_notice_chat.pack()
            entry4_person.pack(side=tkinter.BOTTOM, pady=50)

            # entry3_info.pack()
            # btn_info = tkinter.Button(tk, text="공지")
            # btn_info.place(x=760, y=99)
            # btn_freeze = tkinter.Button(tk, text="채팅창 활성화/비활성화")
            # btn_freeze.pack(pady=7)
            # btn_force_out = tkinter.Button(tk, text="강퇴")
            # btn_force_out.place(x=620, y=72)
            # btn_force_in = tkinter.Button(tk, text="강퇴해제")
            # btn_force_in.place(x=708, y=71)
            # label_person = tkinter.Label(tk, text="총 인원")
            # label_person.place(x=785, y=435)
            # entry4_person.pack(side=tkinter.RIGHT, padx=5, pady=5)

            tk.mainloop()  # mainloop 위에서 만든 tk_form을 구동시킨다
            # mainloop는 스레드 점유한다.(=스레드가 갇힌 상태)
            # ex) print("123") ---> 영원히 출력 안 됨.

    except Exception:
        pass

runChat()