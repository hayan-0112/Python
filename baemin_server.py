import socketserver
import threading
import time
from datetime import datetime
import pymysql

HOST = '172.20.10.2'
PORT = 9900
lock = threading.Lock()
connect = pymysql.connect(host='localhost', user='root', password='0000', db='baemin', charset='utf8mb4')
cur = connect.cursor()


class MyTcpHandler(socketserver.BaseRequestHandler):
    client_sockets = []
    def handle(self):
        self.client_sockets.append(self.request)
        try:
            while 1:
                data = self.request.recv(129536)
                dataSplit = data.decode().split()
                print(dataSplit)
                if dataSplit[0] == "#1": # 로그인
                    if dataSplit[1]:
                        query = "SELECT user_id, user_pw, user_type, user_name from user"
                        cur.execute(query)
                        connect.commit()
                        id_pass_datas = cur.fetchall()
                        login_user_check = False
                        login_ceo_check = False
                        user_id = ""
                        owner_name = ""
                        for i in range(len(id_pass_datas)):
                            if (dataSplit[1] == id_pass_datas[i][0] + id_pass_datas[i][1]):
                                if id_pass_datas[i][2] == '사용자':
                                    login_user_check = True
                                    user_id = id_pass_datas[i][0]
                                    break
                                elif id_pass_datas[i][2] == '사장님':
                                    login_ceo_check = True
                                    owner_name =id_pass_datas[i][3]
                                    query1 = "SELECT store_name from store_info join user on user.user_name = store_info.store_owner where store_owner = "+"\""+owner_name+"\""
                                    cur.execute(query1)
                                    connect.commit()
                                    store_name = cur.fetchall()
                                    break
                        if login_user_check:
                            self.request.send(("정상_유저 "+user_id).encode())
                            print("로그인 정상")
                        elif login_ceo_check:
                            query1 = "SELECT * from owner_order_list where store_name ='{}'".format(store_name[0][0])
                            cur.execute(query1)
                            connect.commit()
                            order_list = cur.fetchall()
                            send_order_list = ""
                            for i in range(len(order_list)):
                                for j in range(len(order_list[i])):
                                    if j == len(order_list[i]) - 1:
                                        send_order_list += str(order_list[i][j])
                                    else:
                                        send_order_list += str(order_list[i][j]) + "||"
                                if i != len(order_list)-1:
                                    send_order_list += "|||"
                            query2 = "SELECT * from review where store_name ='{}' order by owner_comment ".format(store_name[0][0])
                            cur.execute(query2)
                            connect.commit()
                            review_list = cur.fetchall()
                            send_review_list = "####"
                            for i in range(len(review_list)):
                                for j in range(len(review_list[i])):
                                    if j == len(review_list[i]) - 1:
                                        send_review_list += str(review_list[i][j])
                                    else:
                                        send_review_list += str(review_list[i][j]) + "||"
                                if i != len(review_list) - 1:
                                    send_review_list += "|||"

                            self.request.send(("정상_사장님 "+store_name[0][0]+"#"+send_order_list).encode())
                            self.request.send(("리뷰사장님"+send_review_list).encode())
                            print("사장님 정상")
                        else:
                            self.request.send('비정상'.encode())
                            print("로그인 비정상")
                elif dataSplit[0] == "#2": # 회원가입
                    query = "insert into user values("
                    for i in range(1,len(dataSplit)):
                        if i == len(dataSplit) - 1:
                            query += '"'+dataSplit[i]+'",'+'"사용자", "귀한분")'
                        else:
                            query += '"'+dataSplit[i]+'",'
                    cur.execute(query)
                    connect.commit()
                elif dataSplit[0] == "#3": # 카테고리 선텍
                    query = "select store_name, store_rating, delivery_time, delivery_tip, minOrder, logo_img from store_info where store_category = "+"\""+dataSplit[1]+"\""
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    store_info = "카테고리 "
                    for i in range(len(data)):
                        if i == len(data)-1:
                            store_info += data[i][0] + "," + str(data[i][1])+","+str(data[i][2])+","+str(data[i][3])+","+str(data[i][4])+","+str(data[i][5])
                        else:
                            store_info += data[i][0]+","+str(data[i][1])+","+str(data[i][2])+","+str(data[i][3])+","+str(data[i][4])+","+str(data[i][5])+"|"
                    self.request.send(store_info.encode())
                elif dataSplit[0] == "#4":  # 카테고리 선텍
                    store_name = ""
                    for i in range(1, len(dataSplit)):
                        if i == len(dataSplit)-1:
                            store_name += dataSplit[i]
                        else:
                            store_name += dataSplit[i] + " "
                    query = "select * from store_info where store_name = " +"\""+store_name+"\""
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    store_info = "가게정보 및 메뉴"
                    for i in range(len(data[0])):
                        if i == 20:
                            store_info += str(data[0][i])
                        else:
                            store_info += str(data[0][i]) + "||"
                    query1 = "select * from store_menu_info where store_name = " + "\"" + store_name + "\""
                    cur.execute(query1)
                    connect.commit()
                    data1 = cur.fetchall()
                    store_info += " ### "
                    for i in range(len(data1)):
                        for j in range(len(data1[i])):
                            if j == 5:
                                store_info += str(data1[i][j])
                            else:
                                store_info += str(data1[i][j]) + "||"
                        if i != len(data1)-1:
                            store_info += "##"
                    query2 = "select * from review_info where store_name = " + "\"" + store_name + "\""
                    cur.execute(query2)
                    connect.commit()
                    data1 = cur.fetchall()
                    store_info += " ### "
                    for i in range(len(data1)):
                        for j in range(len(data1[i])):
                            if j == 3:
                                store_info += str(data1[i][j])
                            else:
                                store_info += str(data1[i][j]) + "||"
                        if i != len(data1) - 1:
                            store_info += "##"

                    query3 = "select * from review where store_name = " + "\"" + store_name + "\""
                    cur.execute(query3)
                    connect.commit()
                    data2 = cur.fetchall()
                    store_info += "###"
                    for i in range(len(data2)):
                        for j in range(len(data2[i])):
                            if j == 6:
                                store_info += str(data2[i][j])
                            else:
                                store_info += str(data2[i][j]) + "||"
                        if i != len(data2) - 1:
                            store_info += "##"

                    self.request.send(store_info.encode())

                elif dataSplit[0] == "#5":  # my배민 선텍
                    query = "select user_name, user_birthday, user_phone, user_addr, user_rank from user where user_id = " +"\""+dataSplit[1]+"\""
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    my_baemin = "my배민 "
                    for i in range(len(data[0])):
                        if i == 5:
                            my_baemin += str(data[0][i])
                        else:
                            my_baemin += str(data[0][i]) + "||"
                    self.request.send(my_baemin.encode())
                elif dataSplit[0] == "#6":
                    menu_name = data.decode()[3:].split("||")[0]
                    store_name = data.decode()[3:].split("||")[1]
                    query = "select store_menu_name, store_menu_img, store_menu_description, store_menu_price from store_menu_info where store_menu_name = '{}' and store_name = '{}'".format(menu_name,store_name)
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    menu_data = "메뉴클릭 "
                    for i in range(len(data[0])):
                        if i == 3:
                            menu_data += str(data[0][i])
                        else:
                            menu_data += str(data[0][i]) +"||"
                    query = "select menu_choice_cate,menu_choice_list, add_amount from store_menu_click_info where menu_name = '{}' and store_name ='{}' ORDER BY add_amount desc".format(menu_name, store_name)
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    menu_data += "메뉴정보"
                    for i in range(len(data)):
                        if i == len(data)-1:
                            for j in range(len(data[i])):
                                if j == 2:
                                    menu_data += str(data[i][j])
                                else:
                                    menu_data += str(data[i][j]) + "||"
                        else:
                            for j in range(len(data[i])):
                                if j == 2:
                                    menu_data += str(data[i][j]) + "#"
                                else:
                                    menu_data += str(data[i][j])+"||"
                    self.request.send(menu_data.encode())
                elif dataSplit[0] == "#7":
                    tmpData = data.decode()[3:]
                    tmpData = tmpData.split('||')
                    query = "insert into owner_order_list values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(tmpData[0],tmpData[1],tmpData[2],tmpData[3],tmpData[4],tmpData[5],tmpData[6],tmpData[7],tmpData[8],tmpData[9],tmpData[10])
                    cur.execute(query)
                    connect.commit()
                    for client_socket in MyTcpHandler.client_sockets:
                        client_socket.send("주문도착".encode())

                elif dataSplit[0] == "#8":
                    tmpData = data.decode()[3:]
                    tmpData = tmpData.split('||')
                    query = "insert into user_order_list values('{}', '{}', '{}', '{}', '{}', '{}','{}')".format(tmpData[0], tmpData[1], tmpData[2], tmpData[3], tmpData[4], tmpData[5], tmpData[6])
                    cur.execute(query)
                    connect.commit()


                elif dataSplit[0] == "#9":
                    query1 = "SELECT user_order_list.user_name, user_order_list.store_name, user_order_list.menu_name, user_order_list.menu_price, store_info.logo_img, user_order_list.order_date, user_order_list.order_state FROM user_order_list JOIN store_info ON store_info.store_name = user_order_list.store_name WHERE user_name = '{}'".format(
                        dataSplit[1])
                    print(query1)
                    cur.execute(query1)
                    connect.commit()
                    data = cur.fetchall()
                    send_order = "주문내역 "
                    for i in range(len(data)):
                        for j in range(7):
                            if j == 6:
                                send_order += str(data[i][j]) + "#"
                            else:
                                send_order += str(data[i][j]) + "||"
                    self.request.send(send_order.encode())
  
                elif dataSplit[0] == "#10":
                    dSplit =data.decode()[4:].split("||")
                    print(dSplit)

                    query1 = "update user set user_phone ='{}', user_addr='{}' where user_name = '{}'".format(dSplit[2],dSplit[1],dSplit[0])
                    print(query1)
                    cur.execute(query1)
                    connect.commit()
                elif dataSplit[0] == "#11":
                    dSplit =data.decode()[4:].split("||")
                    query = "insert into review values('{}','{}','{}','{}','{}','{}',{})".format(dSplit[0],dSplit[1],dSplit[2],dSplit[3],dSplit[4],dSplit[5],dSplit[6])
                    cur.execute(query)
                    connect.commit()


                elif dataSplit[0] == "#98":
                    store_name = ""
                    for i in range(1, len(dataSplit)):
                        if i == len(dataSplit)-1:
                            store_name += dataSplit[i]
                        else:
                            store_name += dataSplit[i] +" "
                    query = "select owner_notice from review_info where store_name = '{}'".format(store_name)
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    self.request.send(("사장님공지 "+data[0][0]).encode())

                elif dataSplit[0] == "#99":
                    store_name = ""
                    for i in range(1, len(dataSplit)):
                        if i == len(dataSplit) - 1:
                            store_name += dataSplit[i]
                        else:
                            store_name += dataSplit[i] + " "
                    query = "select a_word_owner from review_info where store_name = '{}'".format(store_name)
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    self.request.send(("사장님한마디 " + data[0][0]).encode())

                elif dataSplit[0] == "#101":  # 정보/원산지 선텍
                    #select user_name, user_birthday, user_phone, user_addr, user_rank from user where user_id = "1541"
                    owner_store_name = ""
                    for i in range(1,len(dataSplit)):
                        if i == len(dataSplit)-1:
                            owner_store_name += dataSplit[i]
                        else:
                            owner_store_name += dataSplit[i] +" "
                    query = "SELECT store_name, operating_time, store_closed_days, store_phone, delivery_area, store_introduction from store_info  where store_name = " +"\""+owner_store_name+"\""
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    store_info = "사장님가게정보 "
                    for i in range(len(data[0])):
                        if i == 5:
                            store_info += str(data[0][i])
                        else:
                            store_info += str(data[0][i]) + "||"
                    self.request.send(store_info.encode())
                elif dataSplit[0] == "#102":  # 사장님 메뉴 등록
                    print("사장님 메뉴등록~", dataSplit)
                    query = "insert into store_menu_info"
                    pass
                elif dataSplit[0] == "#103":  # 사장님 메뉴 등록
                    store_name = data.decode().split("||")[0]
                    notice = data.decode().split("||")[1]
                    query = "update review_info set owner_notice = '{}' where store_name = '{}'".format(notice, store_name[5:])
                    cur.execute(query)
                    connect.commit()
                elif dataSplit[0] == "#104":  # 사장님 한마디 등록
                    store_name = data.decode().split("||")[0]
                    word = data.decode().split("||")[1]
                    query = "update review_info set a_word_owner = '{}' where store_name = '{}'".format(word, store_name[5:])
                    cur.execute(query)
                    connect.commit()
                elif dataSplit[0] == "#105":
                    query = "update owner_order_list set request = '{}' where id = '{}'".format(dataSplit[1], dataSplit[2])
                    print(dataSplit)
                    cur.execute(query)
                    print(query)
                    connect.commit()
                    tmpData = dataSplit[3:]
                    send_user = "손님알림 "
                    for i in range(len(tmpData)):
                        if i == len(tmpData)-1:
                            send_user += tmpData[i]
                        else:
                            send_user += tmpData[i] +" "
                    print(send_user)
                    if "가게에서 주문 취소 되셨습니다." in send_user:
                        query = "update user_order_list set order_state = '{}' where id = '{}'".format("취소주문", dataSplit[2])
                        cur.execute(query)
                        connect.commit()
                    elif "가게에서 주문 완료 처리 하셨습니다." in send_user:
                        query = "update user_order_list set order_state = '{}' where id = '{}'".format("배달완료", dataSplit[2])
                        print("완료 처리", dataSplit)
                        cur.execute(query)
                        connect.commit()
                    elif "30분 후 도착 예정입니다." in send_user:
                        now = datetime.now()
                        hour = now.hour
                        minute = now.minute
                        minute += 30
                        if minute >= 60:
                            hour += 1
                            minute -= 60
                        time1 = str(hour)+":"+str(minute)+"에 도착 예정"
                        query = "update user_order_list set order_state = '{}' where id = '{}'".format(time1, dataSplit[2])
                        cur.execute(query)
                        connect.commit()
                    elif "40분 후 도착 예정입니다." in send_user:
                        now = datetime.now()
                        hour = now.hour
                        minute = now.minute
                        minute += 40
                        if minute >= 60:
                            hour += 1
                            minute -= 60
                        time1 = str(hour) + ":" + str(minute) + "에 도착 예정"
                        query = "update user_order_list set order_state = '{}' where id = '{}'".format(time1, dataSplit[2])
                        cur.execute(query)
                        connect.commit()
                    for client_socket in MyTcpHandler.client_sockets:
                        client_socket.send(send_user.encode())
                elif dataSplit[0] == "#106":
                    store_name = data.decode().split('#')[1]
                    store_name = store_name[4:]
                    query = "select store_menu_name, store_menu_img, store_menu_description, store_menu_price from store_menu_info where  store_name = '{}'".format(store_name)
                    cur.execute(query)
                    connect.commit()
                    data = cur.fetchall()
                    menu_data = "메뉴클릭 "
                    for i in range(len(data[0])):
                        if i == 3:
                            menu_data += str(data[0][i])
                        else:
                            menu_data += str(data[0][i]) +"||"
                    self.request.send(menu_data.encode())

                    query1 = "select store_menu_name, store_menu_img, store_menu_description, store_menu_price from store_menu_info where  store_name = '{}'".format(
                        store_name)
                    cur.execute(query1)
                    connect.commit()
                    data = cur.fetchall()
                    menu_data1 = "사장메뉴 "
                    for i in range(len(data[0])):
                        if i == 3:
                            menu_data1 += str(data[0][i])
                        else:
                            menu_data1 += str(data[0][i]) + "||"
                    print(menu_data1)
                    self.request.send(menu_data1.encode())

                elif dataSplit[0] == "#107":
                    query1 = "SELECT * from owner_order_list where store_name ='{}'".format(store_name[0][0])#8
                    cur.execute(query1)
                    connect.commit()
                    order_list = cur.fetchall()
                    send_order_list = "업데이트오더 "
                    for i in range(len(order_list)):
                        for j in range(len(order_list[i])):
                            if j == len(order_list[i]) - 1:
                                send_order_list += str(order_list[i][j])
                            else:
                                send_order_list += str(order_list[i][j]) + "||"
                        if i != len(order_list) - 1:
                            send_order_list += "|||"
                    query2 = "SELECT * from review where store_name ='{}'".format(store_name[0][0])
                    cur.execute(query2)
                    connect.commit()
                    review_list = cur.fetchall()
                    send_order_list += "^^^"
                    for i in range(len(review_list)):
                        for j in range(len(review_list[i])):
                            if j == len(review_list[i]) - 1:
                                send_order_list += str(review_list[i][j])
                            else:
                                send_order_list += str(review_list[i][j]) + "||"
                        if i != len(review_list) - 1:
                            send_order_list += "|||"
                    self.request.send(send_order_list.encode())

                elif dataSplit[0] == "#108":
                    query2 = "SELECT * from review where store_name ='{}' order by owner_comment ".format(
                        store_name[0][0])
                    cur.execute(query2)
                    connect.commit()
                    review_list = cur.fetchall()
                    send_review_list = "####"
                    for i in range(len(review_list)):
                        for j in range(len(review_list[i])):
                            if j == len(review_list[i]) - 1:
                                send_review_list += str(review_list[i][j])
                            else:
                                send_review_list += str(review_list[i][j]) + "||"
                        if i != len(review_list) - 1:
                            send_review_list += "|||"
                    self.request.send(("리뷰사장님"+send_review_list).encode())
                elif dataSplit[0] == "#109":  # 사장님 한마디 등록
                    tmp = data.decode()[5:].split("||")
                    query = "update review set owner_comment = '{}' where id = '{}'".format(tmp[1], tmp[0])
                    cur.execute(query)
                    connect.commit()

        except Exception as e:
            print("클라이언트 연결 종료")
            self.client_sockets.remove(self.request)
            print(MyTcpHandler.client_sockets)
            print(e)
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

