import socket
import threading
import tkinter

def reveive_image(connection, save_path):
    with open(save_path, "wb") as image_file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(data)
            image_file.write(data)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ent_ip.get(), int(ent_port.get())))
    save_path = ent_file.get()
    reveive_image(client_socket,save_path)
    print("완료")
    client_socket.close()

#ip / port / filename / button
root = tkinter.Tk()
root.geometry("600x600")
label1 = tkinter.Label(text="HOST")
ent_ip = tkinter.Entry(root)
label2 = tkinter.Label(text="PORT")
ent_port = tkinter.Entry(root)
label3 = tkinter.Label(text="저장할 이름 입력")
ent_file = tkinter.Entry(root)
btn_connect = tkinter.Button(root, command=main, text="rcv")
label1.pack()
ent_ip.pack()
label2.pack()
ent_port.pack()
label3.pack()
ent_file.pack()
btn_connect.pack()
root.mainloop()