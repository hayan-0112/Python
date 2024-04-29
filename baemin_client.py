import ast
import tkinter as tk
from tkinter import *
import tkinter.messagebox
import tkinter.ttk as ttk
import socket
from threading import Thread
import tkinter
from tkinter import font
from PIL import Image, ImageTk
from tkinter import filedialog
import io
import base64
import random
from datetime import datetime
import platform

root = tk.Tk()
logout_img = PhotoImage(file='014.png')
login_btn_img = PhotoImage(file='로그인.png')
user_add_btn_img = PhotoImage(file='회원가입.png')
id_label_img = PhotoImage(file='ID.png')
pw_label_img = PhotoImage(file='PW.png')

add_user_from = PhotoImage(file='ddd.png')
join_name = PhotoImage(file='join_name.png')
join_birth = PhotoImage(file='생년월일.png')
join_phone = PhotoImage(file='전화번호.png')
join_addr = PhotoImage(file='join_addr.png')
join_id = PhotoImage(file='join_id.png')
join_pw = PhotoImage(file='join_pw.png')
star1 = PhotoImage(file='star1.png')
star2 = PhotoImage(file='star2.png')

main_de = PhotoImage(file='가게배달.png')
main_basket = PhotoImage(file='장바구니.png',width=40,height=30)

put_img = PhotoImage(file='baemin.png')
pizza_img = PhotoImage(file='del_pizza_resize.png')
chicken_img = PhotoImage(file='del_chicken_resize.png')
korea_img = PhotoImage(file='del_hansik_resize.png')
china_img = PhotoImage(file='del_junsik_resize.png')
japan_img = PhotoImage(file='del_illsik_resize.png')
usa_img = PhotoImage(file='del_yangsik_resize.png')
login_color = '#34C2C3'
del_camera_img = PhotoImage(file='del_camera.png')
ad1_img = PhotoImage(file='add1.png')

review_com_img = PhotoImage(file='review_com.png')

home_img = PhotoImage(file='홈.png')
cart_img = PhotoImage(file='장바구니.png')
pizza_owner_img = PhotoImage(file='pizzaaaaaaaaa.png')
review_btn_img =  PhotoImage(file='review_btn.png')
orderlist_img = PhotoImage(file='001.png')
review_img = PhotoImage(file='002.png')
menu_img = PhotoImage(file='003.png')
time_30_img = PhotoImage(file='004.png')
time_40_img = PhotoImage(file='005.png')
time_cancel_img = PhotoImage(file='006.png')
time_ing_img = PhotoImage(file='007.png')
time_final_cancel_img = PhotoImage(file='008.png')
baedali_img = PhotoImage(file='009.png')
comment_img = PhotoImage(file='010.png')
comment_write_img = PhotoImage(file='011.png')
sajang_img = PhotoImage(file='012.png')
baeminLogo_img = PhotoImage(file='013.png')
complete_img = PhotoImage(file='015.png')
final_complete_img = PhotoImage(file='016.png')
star_img = PhotoImage(file='star.png')

#del_img = PhotoImage(file='del.img.png')
del_pinglive_img = PhotoImage(file='del_pinglive_resize2.png')
#del_present_img = PhotoImage(file='del_pre_resize.png')
#del_Bmart_img = PhotoImage(file='del_Bmart_resize.png')
#del_fastdel_img = PhotoImage(file='del_fastdel_resize.png')
#del_riders_img = PhotoImage(file='del_riders_resize.png')
#del_takeout_img = PhotoImage(file='del_takeout_resize.png')
del_one_img = PhotoImage(file='del_one_resize.png')
del_bunski_img = PhotoImage(file='del_bunsik_resize.png')
del_dessert_img = PhotoImage(file='del_dessert_resize.png')
del_jokbal_img = PhotoImage(file='del_jokbal_resize.png')
del_yasik_img = PhotoImage(file='del_yasik_resize.png')
del_soup_img = PhotoImage(file='del_soup_resize.png')
del_lunch_img = PhotoImage(file='del_lunch_resize.png')
del_fastfood_img = PhotoImage(file='del_fastfood_resize.png')
del_coup_img = PhotoImage(file='del_coup.png')
del_lowtip_img = PhotoImage(file='del_lowtip.png')
del_reorder_img = PhotoImage(file='del_reorder.png')
del_nice_img = PhotoImage(file='nice.png')
del_search_img = PhotoImage(file='del_search.png')
del_deliverystore_img = PhotoImage(file='del_deliverystore.png')
del_pick_img = PhotoImage(file='del_pick.png')
del_ordered_img = PhotoImage(file='del_ordered.png')
del_mydelivery_img = PhotoImage(file='del_mydeliver.png')
del_home_img = PhotoImage(file='del_home.png')
del_basket_img = PhotoImage(file='del_basket.png')
del_advertistment_img = PhotoImage(file='del_ad_resize.png')

del_arrow_img = PhotoImage(file='del_arrow.png')
del_right_img = PhotoImage(file='del_right_resize.png')
del_left_img= PhotoImage(file='del_left_resize.png')

l_img= PhotoImage(file='l.png')
c_img= PhotoImage(file='c.png')
r_img= PhotoImage(file='r.png')

l_bimg= PhotoImage(file='l_b.png')
c_bimg= PhotoImage(file='c_b.png')
r_bimg= PhotoImage(file='r_b.png')

rating_img55 = PhotoImage(file='rating55.png')

del_order_btn_img = PhotoImage(file='배달주문.png')
del_order_noc_btn_img = PhotoImage(file='배달주문x.png')
po_order_btn_img = PhotoImage(file='포방.png')
po_order_noc_btn_img = PhotoImage(file='포방x.png')


b_img= PhotoImage(file='b.png')

rating_5_img = PhotoImage(file='rating_5.png')
rating_45_img = PhotoImage(file='rating_4.5.png')
rating_4_img = PhotoImage(file='rating_4.png')
rating_35_img = PhotoImage(file='rating_3.5.png')

co_img = PhotoImage(file='co.png')

del_cat_img = PhotoImage(file='del_cat.png')
del_baket_cat_img = PhotoImage(file='del_wink_cats.png')
del_more_put_img = PhotoImage(file="del_more_put.png")

del_glass_img = PhotoImage(file='del_glass.png')
login_color = '#34C2C3'

HOST = '192.168.31.198'
PORT = 9900

class form():
    def __init__(self,master):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        t = Thread(target=self.rcvMsg, args=(self.sock,))
        t.daemon = True
        t.start()
        self.master = master
        canvas_img = tk.Canvas(self.master,bg='white',width=550,height=250)

        canvas_img.create_image((275,125),image=put_img)
        canvas_bg = tk.Canvas(self.master,bg='#2AC1BC',width=550,height=850)


        canvas_img.pack()
        canvas_bg.pack()

        self.master.title("로그인")
        self.master.geometry("550x550")
        self.ID = tk.Label(self.master,bg='#2AC1BC',image=id_label_img)
        self.ID.place(x=40,y=292)
        self.PW = tk.Label(self.master, image=pw_label_img,bg='#2AC1BC')
        self.PW.place(x=40, y=365)
        self.ID_entry = tk.Entry(self.master,font=('',20))
        self.ID_entry.place(x=105,y=300,width=400,height=30)
        self.pw_entry = tk.Entry(self.master,font=('',20),show="*")
        self.pw_entry.place(x=105, y=370,width=400,height=30)
        self.login = tk.Button(self.master,image=login_btn_img,command=self.open_main_form,bg='#247DE5',bd=0,highlightthickness=0)
        self.login.place(x=110,y=450)
        self.join = tk.Button(self.master,image=user_add_btn_img , command=self.open_join_form,bg='#247DE5',bd=0,highlightthickness=0)
        self.join.place(x=280, y=450)
        self.ID_entry.bind("<Return>", self.onEnter)
        self.pw_entry.bind("<Return>", self.onEnter)
        self.user_id = ""
        self.user_store_name=""
        self.img_path = ""
        self.owner_store_info = ""
        self.searchable_items = ["치킨", "치밥", "치킨버거", "초밥", "피자", '치약', '유치', '김치', '수치', '가물치', '망치', '치질', '갈치', '상치',
                                 '인치']
        self.logo_img = b""
        self.ctn = 0
        self.labels_list = []
        self.selected_values = {}
        self.basket = {}
        self.labels_list = []
        self.review_list = []
        self.tk_image_menu = []  # ------
        self.tk_image_store = []  # --------
        self.key_list = []
        self.value_list = []
        self.basket_list = []
        self.user_login = False
        self.owner_login = False
        self.store_name = []
        self.del_order = True
        self.po_order = False
        self.rating_num = "5"
        self.plz_entry = []
        self.text_name = []
        self.text_price = []
    def change_orderList(self):
        self.order_frame.pack(fill='both', expand=True)
        self.review_frame.pack_forget()
        self.menu_frame.pack_forget()
        self.menu_bottom_frame.place_forget()

    def change_reviewList(self):
        self.order_frame.pack_forget()
        self.review_frame.pack()
        self.review_frame.pack_propagate(False)
        self.menu_frame.pack_forget()
        self.menu_bottom_frame.place_forget()
        self.review_items_canvas.config(scrollregion=self.review_items_canvas.bbox("all"))
        self.review_items_canvas.bind("<Configure>", self.on_review_canvas_configure)
        self.review_items_canvas.bind_all("<MouseWheel>", self.on_review_ousewheel)

        self.sock.send(("#108 ").encode())

    def change_menuList(self):
        self.order_frame.pack_forget()
        self.review_frame.pack_forget()
        self.menu_frame.pack(fill='both', expand=True, anchor='n')
        self.menu_frame.pack_propagate(False)
        self.menu_bottom_frame.place(y=760)
        self.menu_bottom_frame.pack_propagate(False)
        self.sock.send(("#106 " + self.user_store_name).encode())
    def on_main_form_close(self):
        pass

    def open_owner_main_form(self, data):
        global main_form

        main_form = tk.Toplevel(self.master)
        # self.create_owner_menu_form()
        # self.change_reivewList()
        root.withdraw()
        main_form.title('사장님')
        main_form.geometry('550x850')
        main_form.resizable(False, False)

        self.Canvas_main_top_bg = tk.Canvas(main_form, bg='#25c4be', width=550, height=50)
        self.Canvas_main_top_bg.pack()

        self.order_frame = tk.Frame(main_form, width=550, height=800, bg='black')
        self.order_frame.pack(fill='both', expand=True)

        # self.bottom_frame = tk.Frame(main_form, width=550, height=50, bg='#25c4be')  #######추가
        # self.bottom_frame.place(y=800)
        #
        # self.logout_button = tk.Button(self.bottom_frame, image=logout_img, relief='flat', bd=0, bg='#25c4be',
        #                                command=self.close_main_form)  #######추가
        # self.logout_button.place(x=500, y=4)

        font_instance = font.Font(family="맑은 고딕", size=12)
        self.shop = tk.Label(self.Canvas_main_top_bg, text=self.user_store_name, font=font_instance, bg='#25c4be',
                             fg='white', wraplength=220)  # 가게이름
        self.shop.place(x=10, y=2)
        self.orderList = tk.Button(self.Canvas_main_top_bg, image=orderlist_img, bg='#25c4be', bd=0, relief="flat",
                                   # 주문내역
                                   command=self.change_orderList)
        self.orderList.place(x=250, y=10)
        self.view = tk.Button(self.Canvas_main_top_bg, image=review_img, bg='#3bd1d1', command=self.change_reviewList,
                              bd=0, relief="flat")  # 리뷰관리
        self.view.place(x=350, y=10)
        self.menu = tk.Button(self.Canvas_main_top_bg, image=menu_img, bg='#25c4be', bd=0, command=self.change_menuList,
                              # 메뉴관리
                              relief="flat")
        self.menu.place(x=450, y=10)

        # 스크롤 전체 캔버스
        self.order_all_canvas = tk.Canvas(self.order_frame, borderwidth=0, bg="white", highlightthickness=0)

        # 스크롤바
        self.scrollbar = tk.Scrollbar(self.order_frame, command=self.order_all_canvas.yview, borderwidth=0)
        self.order_all_canvas.configure(yscrollcommand=self.scrollbar.set,
                                        scrollregion=self.order_all_canvas.bbox("all"))
        #self.scrollbar.pack(side='right', fill='y')
        self.order_all_canvas.pack(side="right", fill='both', expand=True)
        self.order_all_canvas.pack_propagate(False)

        self.inner_frame = tk.Frame(self.order_all_canvas, bg='white')
        # self.inner_frame.pack(side='right', fill='y')
        # self.inner_frame.pack_propagate(False)
        self.order_all_canvas_window = self.order_all_canvas.create_window(0, 0, window=self.inner_frame, anchor="nw")

        # 주문 접수 버튼 프레임
        self.order_ing_canvas = tk.Canvas(self.order_frame, width=120, height=800, bg='lightgray')
        self.order_ing_canvas.pack(side='left', fill='both')
        self.order_ing_canvas.pack_propagate(False)
        self.order_ing_frame = tk.Frame(self.order_ing_canvas, width=120, height=800, bg="lightgray")
        self.order_ing_frame.pack(fill='y')
        self.order_ing_frame.pack_propagate(False)
        self.selected_button = tk.StringVar(value="before")  # 초기 상태를 'before'로 설정

        # 주문 동적 접수 프레임
        self.orderlist_before_frame = tk.Frame(self.inner_frame, width=428, bg='white')
        self.orderlist_before_frame.pack(side='right', fill='y')
        self.orderlist_ing_frame = tk.Frame(self.inner_frame, width=428, bg='white')
        self.orderlist_complete_frame = tk.Frame(self.inner_frame, width=428, bg='white')

        self.inner_frame.bind("<Configure>", self.onFrameConfigure)
        self.order_all_canvas.bind("<Configure>", self.onCanvasConfigure)
        self.inner_frame.bind('<Enter>', self.onEnterrr)  # bind wheel events when the cursor enters the control
        self.inner_frame.bind('<Leave>', self.onLeave)
        self.onFrameConfigure(None)

        self.update_order_frame(data, 0)

        self.order_ing_before_button = tk.Button(self.order_ing_frame, width=11, height=9,
                                                 text=f'접수대기',
                                                 font=("arial", 15, "bold"), fg='grey', bg='lightgray', bd=1,
                                                 command=lambda: self.change_orderList_bt('before'))
        self.order_ing_before_button.pack()

        self.order_ing_ing_button = tk.Button(self.order_ing_frame, width=11, height=10, text='진행중',
                                              font=("arial", 15, "bold"), fg='grey', bg='lightgray', bd=1,
                                              command=lambda: self.change_orderList_bt('ing'))
        self.order_ing_ing_button.pack()

        self.order_ing_after_button = tk.Button(self.order_ing_frame, width=11, height=10, text='완료',
                                                font=("arial", 15, "bold"), fg='grey', bg='lightgray', bd=1,
                                                command=lambda: self.change_orderList_bt('complete'))
        self.order_ing_after_button.pack()
        test_frame = tk.Frame(self.order_ing_frame, width=10, height=10, bg='red')
        test_frame.place(x=200, y=200)

        # self.order_ing_frame = tk.Frame(self.order_frame, width=120, height=850, bg="lightgray")
        # self.order_ing_frame.place(y=0)
        # self.order_ing_frame.pack_propagate(False)
        # self.selected_button = tk.StringVar(value="before")  # 초기 상태를 'before'로 설정
        #
        #
        # self.orderlist_before_frame = tk.Frame(self.order_frame, width=428, height=800, bg='white')
        # self.orderlist_before_frame.place(x=120)
        # self.orderlist_before_frame.pack_propagate(False)
        # self.orderlist_ing_frame = tk.Frame(self.order_frame, width=428, height=800, bg='white')
        # self.orderlist_ing_frame.pack_propagate(False)
        # self.orderlist_complete_frame = tk.Frame(self.order_frame, width=428, height=800, bg='white')
        # self.orderlist_complete_frame.pack_propagate(False)
        #
        # self.update_order_frame(data, 0)
        #
        # self.order_ing_before_button = tk.Button(self.order_ing_frame, width=11, height=9,
        #                                          text=f'접수대기',
        #                                          font=("arial", 15, "bold"), fg='grey', bg='lightgray', bd=1,
        #                                          command=lambda: self.change_orderList_bt('before'))
        # self.order_ing_before_button.pack()
        #
        # self.order_ing_ing_button = tk.Button(self.order_ing_frame, width=11, height=10, text='진행중',
        #                                       font=("arial", 15, "bold"), fg='grey', bg='lightgray', bd=1,
        #                                       command=lambda: self.change_orderList_bt('ing'))
        # self.order_ing_ing_button.pack()
        #
        # self.order_ing_after_button = tk.Button(self.order_ing_frame, width=11, height=10, text='완료',
        #                                         font=("arial", 15, "bold"), fg='grey', bg='lightgray', bd=1,
        #                                         command=lambda: self.change_orderList_bt('complete'))
        # self.order_ing_after_button.pack()
        # test_frame = tk.Frame(self.order_ing_frame, width=10, height=10, bg='red')
        # test_frame.place(x=200, y=200)

        ################################리뷰





        ##################################################

        self.menu_frame = tk.Frame(main_form, width=550, height=750, bg='white')
        self.order_frame.pack(fill='both', expand=True, anchor='n')

        # 스크롤 전체 캔버스
        self.menu_canvas = tk.Canvas(self.menu_frame, borderwidth=0, bg="white", highlightthickness=0)

        # 스크롤바
        self.menu_scrollbar = tk.Scrollbar(self.menu_frame, command=self.menu_canvas.yview, borderwidth=0)
        self.menu_canvas.configure(yscrollcommand=self.menu_scrollbar.set,
                                   scrollregion=self.menu_canvas.bbox("all"))

        self.menu_canvas.pack(side="right", fill='both', expand=True)
        self.menu_canvas.pack_propagate(False)

        self.menu_inner_frame = tk.Frame(self.menu_canvas, bg='white')
        # self.inner_frame.pack(side='right', fill='y')
        # self.inner_frame.pack_propagate(False)
        self.menu_canvas_window = self.menu_canvas.create_window(0, 0, window=self.menu_inner_frame, anchor="nw")

        # 메뉴 동적 프레임
        self.menu_up_frame = tk.Frame(self.menu_inner_frame, width=550, bg='white')
        self.menu_up_frame.pack(side='top', fill='y', padx=110, pady=20)

        self.menu_checkbox = []
        self.menu_checkbox_var = IntVar()

        self.menu_up_checkbox = Checkbutton(self.menu_up_frame, variable=self.menu_checkbox_var, bg='white')
        # self.menu_up_checkbox.grid(row=0, column=0)
        self.menu_checkbox.append((self.menu_checkbox_var, self.menu_up_checkbox))

        self.checkbox_widgets = []

        self.menu_bottom_frame = tk.Frame(main_form, height=40, width=550, bg='white')
        # self.menu_bottom_frame.place(y=760)
        # self.menu_bottom_frame.pack_propagate(False)
        self.sign_up = tk.Button(self.menu_bottom_frame, text='메뉴 등록', font=('맑은 고딕', 15), bg='white', bd=0,
                                 command=self.open_owner_menu_sign_up_form)
        self.sign_up.pack(side="left", anchor='w', padx=45)  # 변경

        self.origin_information = tk.Button(self.menu_bottom_frame, text='정보/원산지', font=('맑은 고딕', 15), bg='white', bd=0,
                                            command=self.open_owner_information_origin_form)
        self.origin_information.pack(side="left", anchor='w', padx=15)  # 변경

        self.delete = tk.Button(self.menu_bottom_frame, text='삭제', font=('맑은 고딕', 15), bg='white', bd=0,
                                command=self.menu_delete)
        self.delete.pack(side="right", anchor='e', padx=50)  # 변경

        # self.change = tk.Button(self.menu_bottom_frame, text='수정', font=('맑은 고딕', 15), bg='white', bd=0,
        #                         command=self.edit_selected_menu)
        # self.change.pack(side="right", anchor='e', padx=30)  # 변경

        self.bottom_frame = tk.Frame(main_form, width=550, height=50, bg='#25c4be')  #######추가
        self.bottom_frame.place(y=800)

        self.logout_button = tk.Button(self.bottom_frame, image=logout_img, relief='flat', bd=0, bg='#25c4be',
                                       command=self.close_main_form)  #######추가
        self.logout_button.place(x=500, y=4)

        self.menu_inner_frame.bind("<Configure>", self.onMenuFrameConfigure)
        self.menu_canvas.bind("<Configure>", self.onMenuCanvasConfigure)
        self.menu_inner_frame.bind('<Enter>', self.onMenuEnter)  # bind wheel events when the cursor enters the control
        self.menu_inner_frame.bind('<Leave>', self.onMenuLeave)
        self.onMenuFrameConfigure(None)


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.order_all_canvas.configure(scrollregion=self.order_all_canvas.bbox("all"))

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.order_all_canvas.itemconfig(self.order_all_canvas_window, width=canvas_width)

    def onEnterrr(self, event):  # bind wheel events when the cursor enters the control
        if platform.system() == 'Linux':
            self.order_all_canvas.bind_all("<Button-4>", self.onMouseWheel)
            self.order_all_canvas.bind_all("<Button-5>", self.onMouseWheel)
        else:
            self.order_all_canvas.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):  # unbind wheel events when the cursorl leaves the control
        if platform.system() == 'Linux':
            self.order_all_canvas.unbind_all("<Button-4>")
            self.order_all_canvas.unbind_all("<Button-5>")
        else:
            self.order_all_canvas.unbind_all("<MouseWheel>")


    def onMouseWheel(self, event):  # cross platform scroll wheel event
        if platform.system() == 'Windows':
            self.order_all_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif platform.system() == 'Darwin':
            self.order_all_canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.order_all_canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.order_all_canvas.yview_scroll(1, "units")

    def onMenuFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.menu_canvas.configure(scrollregion=self.menu_canvas.bbox("all"))

    def onMenuCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.menu_canvas.itemconfig(self.menu_canvas_window, width=canvas_width)

    def onMenuEnter(self, event):  # bind wheel events when the cursor enters the control
        if platform.system() == 'Linux':
            self.menu_canvas.bind_all("<Button-4>", self.onMenuMouseWheel)
            self.menu_canvas.bind_all("<Button-5>", self.onMenuMouseWheel)
        else:
            self.menu_canvas.bind_all("<MouseWheel>", self.onMenuMouseWheel)

    def onMenuLeave(self, event):  # unbind wheel events when the cursorl leaves the control
        if platform.system() == 'Linux':
            self.menu_canvas.unbind_all("<Button-4>")
            self.menu_canvas.unbind_all("<Button-5>")
        else:
            self.menu_canvas.unbind_all("<MouseWheel>")

    def onMenuMouseWheel(self, event):  # cross platform scroll wheel event
        if platform.system() == 'Windows':
            self.menu_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif platform.system() == 'Darwin':
            self.menu_canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.menu_canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.menu_canvas.yview_scroll(1, "units")

    def create_review_info(self, data):
        tmp = data[3:]
        splitData = tmp.split("|||")
        review_list = []
        for i in range(len(splitData)):
            review_list.append(splitData[i].split("||"))

        print(review_list)
        self.review_frame = tk.Frame(main_form, width=550, height=746, bg='white')
        self.review_score_frame = tk.Frame(self.review_frame, width=550, height=145, bg="white")
        self.review_score_frame.pack()
        self.review_score_frame.pack_propagate(False)

        self.review_number = tk.Frame(self.review_frame, width=550, height=105, bg="white", bd=1, relief="groove")
        self.review_number.pack()
        self.review_number.pack_propagate(False)

        self.review_items_frame = tk.Frame(self.review_frame, width=550, height=450, bg="white")
        self.review_items_frame.pack()
        self.review_items_frame.propagate(False)
        self.review_items_frame.bind("<Configure>", self.on_frame_configure)

        self.owner_notice_frame = tk.Frame(self.review_frame, width=550, height=45, bg="white", bd=0)
        self.owner_notice_frame.pack()
        self.owner_notice_frame.propagate(False)
        self.notice = tk.Button(self.owner_notice_frame, text="사장님 공지", font=("맑은 고딕", 14), bd=0, bg='white',
                                fg='black', relief="flat", command=self.review_owner_notice)
        self.notice.pack(side="left", padx=10)
        self.word = tk.Button(self.owner_notice_frame, text="사장님 한마디", font=("맑은 고딕", 14), bd=0, bg="white", fg='black',
                              relief="flat", command=self.review_owner_word)
        self.word.pack(side="right", padx=10)

        self.review_items_canvas = tk.Canvas(self.review_items_frame, bg='lightgray', width=550, height=450)
        self.review_items_canvas.pack(fill='both', expand=True)

        self.scrollbar_review = tk.Scrollbar(self.review_items_canvas, orient="vertical",
                                             command=self.review_items_canvas.yview)
        self.scrollbar_review.pack(side='right', fill='y')

        self.review_items_canvas.configure(yscrollcommand=self.scrollbar_review.set)

        y = 0
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        cnt5 = 0

        for i in range(len(review_list)):
            self.review_list_frame = tk.Frame(self.review_items_canvas, width=550, height=400, bg='white')
            self.baedali = tk.Label(self.review_list_frame, image=baedali_img, bd=0)
            self.baedali.place(x=10, y=15)
            self.name_label = tk.Label(self.review_list_frame, text=review_list[i][4], font=('맑은 고딕', 14), bg='white')
            self.name_label.place(x=80, y=15)
            self.grade = tk.Label(self.review_list_frame, text='평점:', font=('맑은 고딕', 12), bg='white')
            self.grade.place(x=80, y=50)
            self.grade_num = tk.Label(self.review_list_frame, text=review_list[i][0], font=('맑은 고딕', 12), bg='white')
            self.grade_num.place(x=120, y=50)
            self.grade_total_num = tk.Label(self.review_list_frame, text='/ 5', font=('맑은 고딕', 12), bg='white')
            self.grade_total_num.place(x=135, y=50)
            self.menuName = tk.Label(self.review_list_frame, text=review_list[i][3], font=('맑은 고딕', 12), bg='lightgray')
            self.menuName.place(x=10, y=100)
            self.reviewContent = tk.Label(self.review_list_frame, text=review_list[i][2], font=('맑은 고딕', 16), bg='white')
            self.reviewContent.place(x=10, y=140)
            if review_list[i][0] == '1':
                cnt1 += 1
            elif review_list[i][0] == '2':
                cnt2 += 1
            elif review_list[i][0] == '3':
                cnt3 += 1
            elif review_list[i][0] == '4':
                cnt4 += 1
            elif review_list[i][0] == '5':
                cnt5 += 1


            if review_list[i][5] != " ":
                text_content = review_list[i][5]
                self.review_label = tk.Label(self.review_list_frame, text=text_content, font=('맑은 고딕', 10), width=45,
                                             height=7,
                                             bg='#EBDDCC', wraplength=350)
                self.review_label.place(x=110, y=210)
                self.sajang_review = tk.Label(self.review_list_frame, image=sajang_img, bd=0)
                self.sajang_review.place(x=10, y=210)

            else:
                self.review_text = tk.Text(self.review_list_frame, font=('맑은 고딕', 10), width=50, height=7, bg='white')  # 텍스트창
                self.review_text.place(x=105, y=190)
                print(self.review_text.get("1.0", tk.END))
                self.add_new_button = tk.Button(self.review_list_frame, image=comment_write_img,
                                                command=lambda frame=self.review_list_frame,
                                                               re_text=self.review_text,
                                                               review_idx=review_list[i][6]:
                                                self.review_write(frame, re_text, review_idx),
                                                relief="flat")
                self.add_new_button.place(x=380, y=320)
                self.sajang_review = tk.Label(self.review_list_frame, image=sajang_img, bd=0)
                self.sajang_review.place(x=10, y=210)
            self.review_items_canvas.create_window((0, y), window=self.review_list_frame, anchor='nw')
            y += 410

        self.review_items_canvas.update_idletasks()

        aver_rating = ((cnt1 * 1)+(cnt2 * 2)+(cnt3 * 3)+(cnt4 * 4)+(cnt5 * 5))/(cnt1+cnt2+cnt3+cnt4+cnt5)
        rounded_rating = round(aver_rating, 2)

        self.review_score_label = tk.Label(self.review_score_frame, text=str(rounded_rating), font=("arial", 25, "bold"), bg="white")
        self.review_score_label.place(x=150, y=20)
        self.review_score_star = tk.Label(self.review_score_frame, image=rating_5_img, bd=0, height=30, width=201)
        self.review_score_star.place(x=70, y=70)
        self.review_score_detail5 = tk.Label(self.review_score_frame, text='5점: ', font=("arail", 10, "bold"),
                                             bg="white")
        self.review_score_detail5.place(x=330, y=10)

        self.review_score_detail5_number = tk.Label(self.review_score_frame, text=str(cnt5), font=("", 12), bg="white",
                                                    fg="gray")
        self.review_score_detail5_number.place(x=355, y=10)
        self.review_score_detail4 = tk.Label(self.review_score_frame, text='4점: ', font=("arail", 10, "bold"),
                                             bg="white")
        self.review_score_detail4.place(x=330, y=35)
        self.review_score_detail4_number = tk.Label(self.review_score_frame, text=str(cnt4), font=("", 12), bg="white",
                                                    fg="gray")
        self.review_score_detail4_number.place(x=355, y=35)
        self.review_score_detail3 = tk.Label(self.review_score_frame, text='3점: ', font=("arail", 10, "bold"),
                                             bg="white")
        self.review_score_detail3.place(x=330, y=60)
        self.review_score_detail3_number = tk.Label(self.review_score_frame, text=str(cnt3), font=("", 12), bg="white",
                                                    fg="gray")
        self.review_score_detail3_number.place(x=355, y=60)
        self.review_score_detail2 = tk.Label(self.review_score_frame, text='2점: ', font=("arail", 10, "bold"),
                                             bg="white")
        self.review_score_detail2.place(x=330, y=85)
        self.review_score_detail2_number = tk.Label(self.review_score_frame, text=str(cnt2), font=("", 12), bg="white",
                                                    fg="gray")
        self.review_score_detail2_number.place(x=355, y=85)
        self.review_score_detail1 = tk.Label(self.review_score_frame, text='1점: ', font=("arail", 10, "bold"),
                                             bg="white")
        self.review_score_detail1.place(x=330, y=110)
        self.review_score_detail1_number = tk.Label(self.review_score_frame, text=str(cnt1), font=("", 12), bg="white",
                                                    fg="gray")
        self.review_score_detail1_number.place(x=355, y=110)

        self.nickname_list = []
        self.nickname_list.append(self.name_label)
        self.review_count = len(self.nickname_list)
        self.total_review_label = tk.Label(self.review_number, text=f"최근 리뷰 {str(len(review_list))}개",
                                           font=("arail", 15, "bold"), bg="white")
        self.total_review_label.place(x=10, y=5)
        self.owner_review_list = []

        self.owner_review_label = tk.Label(self.review_number, text="사장님 댓글 0개", font=("맑은 고딕", 11), bg="white")
        self.owner_review_label.place(x=10, y=35)

        self.comboList = ['리뷰 댓글 없음']
        self.review_sequence = ttk.Combobox(self.review_number, height=1, width=13, state='readonly',
                                            values=self.comboList)
        self.review_sequence.set("리뷰 댓글 없음")
        self.review_sequence.place(x=10, y=70)
        self.review_items_canvas.config(scrollregion=self.review_items_canvas.bbox("all"))
        self.review_items_canvas.bind("<Configure>", self.on_review_canvas_configure)
        self.review_items_canvas.bind_all("<MouseWheel>", self.on_review_ousewheel)

    def on_review_canvas_configure(self, event):
        self.review_items_canvas.config(scrollregion=self.review_items_canvas.bbox("all"))

    def on_review_ousewheel(self, event):
        self.review_items_canvas.yview_scroll(-1 * (event.delta // 120), "units")  # 마우스 휠 스크롤 기능 구현

    def clear_order_frames(self):
        for widget in self.orderlist_before_frame.winfo_children():
            widget.destroy()
        for widget in self.orderlist_ing_frame.winfo_children():
            widget.destroy()
        for widget in self.orderlist_complete_frame.winfo_children():
            widget.destroy()


    def update_order_frame(self, data, num):
        self.clear_order_frames()
        splitData = data.split('^^^')
        tmp = splitData[0]
        splitData = tmp.split("|||")
        data_list = []


        for i in range(len(splitData)):
            data_list.append(splitData[i].split("||"))
        for i in range(len(data_list)):
            if (data_list[i][6] == "접수대기"):
                self.scrollbar_wait = tk.Scrollbar(self.orderlist_before_frame, orient="vertical")
                self.input_order_frame = tk.Canvas(self.orderlist_before_frame, width=428, height=250,
                                                  bg='white', bd=3,
                                                  relief='ridge')

                self.input_order_frame.pack(side="top")
                self.input_order_frame.pack_propagate(False)
                self.orderlist_timeButton_30 = tk.Button(self.input_order_frame, image=time_30_img,
                                                         command=lambda index=i,
                                                                frame=self.input_order_frame: self.timeButton_click(
                                                             30, data_list[index][2], frame, data_list[index][10]),
                                                         relief="flat")
                self.orderlist_timeButton_30.pack(side="top", anchor="e", padx=5, pady=5)
                self.orderlist_timeButton_30.pack_propagate(False)
                self.orderlist_timeButton_40 = tk.Button(self.input_order_frame, image=time_40_img,
                                                         command=lambda index=i,frame=self.input_order_frame: self.timeButton_click(40, data_list[index][2], frame, data_list[index][10]),
                                                         relief="flat")
                self.orderlist_timeButton_40.pack(side="top", anchor="e", padx=5, pady=5)
                self.orderlist_timeButton_30.pack_propagate(False)
                self.orderlist_timeButton_cancel = tk.Button(self.input_order_frame, image=time_cancel_img,
                                                             command=lambda index=i,frame=self.input_order_frame: self.timeButton_click(0, data_list[index][2], frame, data_list[index][10]),
                                                             relief="flat")
                self.orderlist_timeButton_cancel.pack(side="top", anchor="e", padx=5, pady=5)
                self.orderlist_timeButton_30.pack_propagate(False)
                self.new_order_label = tk.Label(self.input_order_frame, text='NEW', font=('arial', 18, 'bold'),
                                                bg='lightblue',
                                                fg='white')
                self.new_order_label.place(x=18, y=75)
                self.order_time_label = tk.Label(self.input_order_frame, text=data_list[i][7],
                                                 font=('arial', 20, 'bold'), bg='white')
                self.order_time_label.place(x=10, y=5)
                self.order_delivery_pack = tk.Label(self.input_order_frame, text=data_list[i][4],
                                                    font=('arial', 16, 'bold'), bg='white',
                                                    fg='#3bd1d1')
                self.order_delivery_pack.place(x=25, y=40)
                self.orderlist_label = tk.Label(self.input_order_frame, text='주문리스트',
                                                font=('arial', 13, 'bold'), bg='white',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=5)
                self.orderlist_label = tk.Label(self.input_order_frame, text=data_list[i][8], font=('맑은 고딕', 13),
                                                fg='gray',
                                                bg='white', wraplength=280)
                self.orderlist_label.place(x=100, y=35)
                self.orderlist_label = tk.Label(self.input_order_frame, text='주소', font=('arial', 13, 'bold'),
                                                bg='white',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=75)
                self.orderlist_label = tk.Label(self.input_order_frame, text=data_list[i][1], font=('맑은 고딕', 13),
                                                bg='white', fg='gray',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=105)
                self.orderlist_label.pack_propagate(False)
                self.order_price_label = tk.Label(self.input_order_frame, text="결제완료",
                                                  font=('arial', 12, 'bold'), bg='white',
                                                  relief="solid", bd=1)
                self.order_price_label.place(x=205, y=5)
                if self.order_price_label.cget("text") == "결제완료":
                    self.order_price_label.config(fg="black")
                elif self.order_price_label.cget("text") == "후불/현금":
                    self.order_price_label.config(fg="red")
                elif self.order_price_label.cget("text") == "후불/카드":
                    self.order_price_label.config(fg="red")
                self.order_request_label = tk.Label(self.input_order_frame, text="요청사항",
                                                    font=('arial', 13, 'bold'), bg='white')
                self.order_request_label.place(x=15, y=165)
                self.order_request_detail_label = tk.Label(self.input_order_frame, text=data_list[i][5],
                                                           font=('arial', 10, 'bold'),
                                                           bg='white')
                self.order_request_detail_label.place(x=15, y=195)
            elif (data_list[i][6] == "진행중"):
                self.input_order_frame = tk.Frame(self.orderlist_ing_frame, width=428, height=250,
                                                  bg='white', bd=3,
                                                  relief='ridge')
                self.input_order_frame.pack(side="top")
                self.input_order_frame.pack_propagate(False)
                self.orderlist_ing = tk.Label(self.input_order_frame, image=time_ing_img, width=77, height=31)
                self.orderlist_ing.pack(side='top', anchor='ne', padx=5, pady=5)
                self.orderlist_complete = tk.Button(self.input_order_frame, image=complete_img, relief='flat',
                                                    command=lambda index=i,frame=self.input_order_frame: self.timeButton_click(1, data_list[index][2], frame, data_list[index][10]))
                self.orderlist_complete.pack(side='top', anchor='e', padx=5, pady=5)
                self.orderlist_timeButton_cancel = tk.Button(self.input_order_frame, image=time_cancel_img,
                                                             command=lambda index=i,frame=self.input_order_frame: self.timeButton_click(0, data_list[index][2], frame, data_list[index][10]),
                                                             relief="flat")
                self.orderlist_timeButton_cancel.pack(side="top", anchor="e", padx=5, pady=5)
                self.new_order_label = tk.Label(self.input_order_frame, text='진행중', font=('arial', 16, 'bold'),
                                                bg='#3bd1d1',
                                                fg='white')
                self.new_order_label.place(x=15, y=75)
                self.order_time_label = tk.Label(self.input_order_frame, text=data_list[i][7],
                                                 font=('arial', 20, 'bold'), bg='white')
                self.order_time_label.place(x=10, y=5)
                self.order_delivery_pack = tk.Label(self.input_order_frame, text=data_list[i][4],
                                                    font=('arial', 16, 'bold'), bg='white',
                                                    fg='#3bd1d1')
                self.order_delivery_pack.place(x=25, y=40)
                self.orderlist_label = tk.Label(self.input_order_frame, text='주문리스트',
                                                font=('arial', 13, 'bold'), bg='white',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=5)
                self.orderlist_label = tk.Label(self.input_order_frame, text=data_list[i][8], font=('맑은 고딕', 13),
                                                fg='gray',
                                                bg='white', wraplength=280)
                self.orderlist_label.place(x=100, y=35)
                self.orderlist_label = tk.Label(self.input_order_frame, text='주소', font=('arial', 13, 'bold'),
                                                bg='white',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=75)
                self.orderlist_label = tk.Label(self.input_order_frame, text=data_list[i][1], font=('맑은 고딕', 13),
                                                bg='white', fg='gray',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=105)
                self.orderlist_label.pack_propagate(False)
                self.order_price_label = tk.Label(self.input_order_frame, text="결제완료",
                                                  font=('arial', 12, 'bold'), bg='white',
                                                  relief="solid", bd=1)
                self.order_price_label.place(x=205, y=5)
                if self.order_price_label.cget("text") == "결제완료":
                    self.order_price_label.config(fg="black")
                elif self.order_price_label.cget("text") == "후불/현금":
                    self.order_price_label.config(fg="red")
                elif self.order_price_label.cget("text") == "후불/카드":
                    self.order_price_label.config(fg="red")
                self.order_request_label = tk.Label(self.input_order_frame, text="요청사항",
                                                    font=('arial', 13, 'bold'), bg='white')
                self.order_request_label.place(x=15, y=165)
                self.order_request_detail_label = tk.Label(self.input_order_frame, text=data_list[i][5],
                                                           font=('arial', 10, 'bold'),
                                                           bg='white')
                self.order_request_detail_label.place(x=15, y=195)
            elif (data_list[i][6] == "완료"):
                self.input_order_frame = tk.Frame(self.orderlist_complete_frame, width=428, height=250,
                                                  bg='white', bd=3,
                                                  relief='ridge')
                self.input_order_frame.pack(side="top")
                self.input_order_frame.pack_propagate(False)
                self.complete_label = tk.Label(self.input_order_frame, image=final_complete_img, relief='flat',
                                               bd=0)
                self.complete_label.pack(side='top', anchor='e', padx=5, pady=5)
                self.new_order_label = tk.Label(self.input_order_frame, text='완료', font=('arial', 18, 'bold'),
                                                bg='gray',
                                                fg='white')
                self.new_order_label.place(x=18, y=75)
                self.order_time_label = tk.Label(self.input_order_frame, text=data_list[i][7],
                                                 font=('arial', 20, 'bold'), bg='white')
                self.order_time_label.place(x=10, y=5)
                self.order_delivery_pack = tk.Label(self.input_order_frame, text=data_list[i][4],
                                                    font=('arial', 16, 'bold'), bg='white',
                                                    fg='#3bd1d1')
                self.order_delivery_pack.place(x=25, y=40)
                self.orderlist_label = tk.Label(self.input_order_frame, text='주문리스트',
                                                font=('arial', 13, 'bold'), bg='white',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=5)
                self.orderlist_label = tk.Label(self.input_order_frame, text=data_list[i][8], font=('맑은 고딕', 13),
                                                fg='gray',
                                                bg='white', wraplength=280)
                self.orderlist_label.place(x=100, y=35)
                self.orderlist_label = tk.Label(self.input_order_frame, text='주소', font=('arial', 13, 'bold'),
                                                bg='white',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=75)
                self.orderlist_label = tk.Label(self.input_order_frame, text=data_list[i][1], font=('맑은 고딕', 13),
                                                bg='white', fg='gray',
                                                wraplength=280)
                self.orderlist_label.place(x=100, y=105)
                self.orderlist_label.pack_propagate(False)
                self.order_price_label = tk.Label(self.input_order_frame, text="결제완료",
                                                  font=('arial', 12, 'bold'), bg='white',
                                                  relief="solid", bd=1)
                self.order_price_label.place(x=205, y=5)
                if self.order_price_label.cget("text") == "결제완료":
                    self.order_price_label.config(fg="black")
                elif self.order_price_label.cget("text") == "후불/현금":
                    self.order_price_label.config(fg="red")
                elif self.order_price_label.cget("text") == "후불/카드":
                    self.order_price_label.config(fg="red")
                self.order_request_label = tk.Label(self.input_order_frame, text="요청사항",
                                                    font=('arial', 13, 'bold'), bg='white')
                self.order_request_label.place(x=15, y=165)
                self.order_request_detail_label = tk.Label(self.input_order_frame, text=data_list[i][5],
                                                           font=('arial', 10, 'bold'),
                                                           bg='white')
                self.order_request_detail_label.place(x=15, y=195)



    def on_frame_configure(self, event):
        self.review_items_canvas.configure(scrollregion=self.review_items_canvas.bbox("all"))
        self.menu_canvas.configure(scrollregion=self.menu_canvas.bbox("all"))


    def timeButton_click(self, minutes, name, frame, num):
        if minutes == 0:
            frame.pack_forget()
            print("#105 완료 " + num + " 가게에서 주문 취소 되셨습니다.")
            self.sock.send(("#105 완료 " + num + " 가게에서 주문 취소 되셨습니다.").encode())
        elif minutes == 1:
            frame.pack_forget()
            print("#105 완료 " + num+ " 가게에서 주문 완료 처리 하셨습니다.")
            self.sock.send(("#105 완료 " + num+ " 가게에서 주문 완료 처리 하셨습니다.").encode())
        elif minutes == 30 or minutes == 40:
            frame.pack_forget()
            self.sock.send(("#105 진행중 " + num+" "+ str(minutes)+"분 후 도착 예정입니다.").encode())




    def changeToComplete(self, name, frame):
        self.input_order_frame.pack_forget()
        self.sock.send(("#105 완료 " + name).encode())
        frame.pack_forget()





    def changeToCompleteState(self):
        self.orderlist_ing.pack_forget()
        self.orderlist_timeButton_cancel.pack_forget()
        self.input_order_frame.pack_forget()


        # self.input_order_frame = tk.Frame(self.orderlist_complete_frame, width=428, height=250, bg='white',
        #                                   relief='solid', bd=1)
        # self.input_order_frame.pack(side="top")
        # self.input_order_frame.pack_propagate(False)
        #
        # self.complete_label = tk.Label(self.input_order_frame, image=final_complete_img, relief='flat', bd=0)
        # self.complete_label.pack(side='top', anchor='e', padx=5, pady=5)
        #
        #
        #
        #
        # self.order_time_label = tk.Label(self.input_order_frame, text='13:22', font=('arial', 20, 'bold'),
        #                                  bg='white')
        # self.order_time_label.place(x=10, y=5)
        # self.order_delivery_pack = tk.Label(self.input_order_frame, text='포장', font=('arial', 16, 'bold'),
        #                                     bg='white', fg='#3bd1d1')
        # self.order_delivery_pack.place(x=25, y=40)
        # self.orderlist_label = tk.Label(self.input_order_frame, text='주문리스트1', font=('arial', 13, 'bold'),
        #                                 bg='white', wraplength=280)
        # self.orderlist_label.place(x=100, y=5)
        # self.orderlist_label = tk.Label(self.input_order_frame, text='주문리스트2', font=('맑은 고딕', 13), fg='gray',
        #                                 bg='white', wraplength=280)
        # self.orderlist_label.place(x=100, y=35)
        # self.orderlist_label = tk.Label(self.input_order_frame, text='주소1', font=('arial', 13, 'bold'), bg='white',
        #                                 wraplength=280)
        # self.orderlist_label.place(x=100, y=75)
        # self.orderlist_label = tk.Label(self.input_order_frame, text='주소2', font=('맑은 고딕', 13), bg='white',
        #                                 fg='gray', wraplength=280)
        # self.orderlist_label.place(x=100, y=105)
        # self.orderlist_label.pack_propagate(False)
        # self.order_price_label = tk.Label(self.input_order_frame, text="결제완료", font=('arial', 12, 'bold'),
        #                                   bg='white', relief="solid", bd=1)
        # self.order_price_label.place(x=205, y=5)
        # if self.order_price_label.cget("text") == "결제완료":
        #     self.order_price_label.config(fg="black")
        # elif self.order_price_label.cget("text") == "후불/현금":
        #     self.order_price_label.config(fg="red")
        # elif self.order_price_label.cget("text") == "후불/카드":
        #     self.order_price_label.config(fg="red")
        #
        # self.order_request_label = tk.Label(self.input_order_frame, text="요청사항", font=('arial', 13, 'bold'),
        #                                     bg='white')
        # self.order_request_label.place(x=15, y=165)
        # self.order_request_detail_label = tk.Label(self.input_order_frame, text="요청사항 내용",
        #                                            font=('arial', 10, 'bold'), bg='white')
        # self.order_request_detail_label.place(x=15, y=195)




    def change_orderList_bt(self, button_name):
        self.selected_button.set(button_name)  # 선택한 버튼 업데이트
        self.change_button_frame(button_name)
        self.sock.send("#107 ".encode())
        self.order_all_canvas.configure(scrollregion=self.order_all_canvas.bbox("all"))

    def change_button_frame(self, button_name=None):
        if button_name is None:
            selected = self.selected_button.get()
        else:
            selected = button_name

        if selected == 'before':
            self.order_ing_before_button.config(bg="white", fg="black")
            self.order_ing_ing_button.config(bg="lightgray", fg="grey")
            self.order_ing_after_button.config(bg="lightgray", fg="grey")
            self.orderlist_ing_frame.pack_forget()
            self.orderlist_complete_frame.pack_forget()
            self.orderlist_before_frame.pack()
            #self.orderlist_before_frame.pack_propagate(False)


        elif selected == 'ing':
            self.order_ing_before_button.config(bg="lightgray", fg="grey")
            self.order_ing_ing_button.config(bg="white", fg="black")
            self.order_ing_after_button.config(bg="lightgray", fg="grey")
            self.orderlist_before_frame.pack_forget()
            self.orderlist_complete_frame.pack_forget()
            self.orderlist_ing_frame.pack()
            #self.orderlist_ing_frame.pack_propagate(False)
        elif selected == 'complete':
            self.order_ing_before_button.config(bg="lightgray", fg="grey")
            self.order_ing_ing_button.config(bg="lightgray", fg="grey")
            self.order_ing_after_button.config(bg="white", fg="black")
            self.orderlist_before_frame.pack_forget()
            self.orderlist_ing_frame.pack_forget()
            self.orderlist_complete_frame.pack()
            #self.orderlist_complete_frame.pack_propagate(False)
        else:
            self.order_ing_before_button.config(bg="white", fg="black")
            self.order_ing_ing_button.config(bg="lightgray", fg="grey")
            self.order_ing_after_button.config(bg="lightgray", fg="grey")
            self.orderlist_ing_frame.pack_forget()
            self.orderlist_complete_frame.pack_forget()
            self.orderlist_before_frame.pack()
            #self.orderlist_before_frame.pack_propagate(False)

    # def move_items(self):
    #   if self.timeButton_click(30) or self.timeButton_click(40):
    #        self.orderlist_ing.pack_forget()
    #        self.orderlist_ing = tk.Label(self.orderlist_ing_frame, image=time_ing_img, width=62, height=31)
    #        self.orderlist_ing.pack(side='top', anchor='ne', padx=5, pady=5)
    #        self.orderlist_ing.pack_propagate(False)

    def open_owner_review_form(self):
        global review_form
        review_form = tk.Toplevel(self.master)
        Canvas_review_bg = tk.Canvas(review_form, bg='white', width=900, height=900)
        Canvas_review_bg.pack()
        root.withdraw()
        review_form.title('main - 리뷰관리')
        review_form.geometry('550x850')
        # main_form.back = tk.Button(main_form, text='뒤로가기', font=('', 20), command=self.close_main_form)
        # main_form.back.pack(side='right')
        review_form.shop = tk.Label(review_form, text='가게이름', font=('', 20), bg='white')
        review_form.shop.place(x=20, y=20)
        review_form.orderList = tk.Button(review_form, text='주문내역', font=('', 20), bg='white', bd=0,
                                          command=self.open_owner_main_form)
        review_form.orderList.place(x=460, y=20)
        review_form.view = tk.Button(review_form, text='리뷰관리', font=('', 20), bg='white', bd=0)
        review_form.view.place(x=580, y=20)
        review_form.menu = tk.Button(review_form, text='메뉴관리', font=('', 20), bg='white', bd=0,
                                     command=self.open_owner_menu_form)
        review_form.menu.place(x=700, y=20)

    def review_owner_notice(self):
        self.sock.send(("#98 "+self.user_store_name).encode())

    def create_owner_notice(self, owner_notice):
        self.notice_form = tk.Toplevel(self.master)
        self.notice_form.resizable(False, False)
        Canvas_notice_bg = tk.Canvas(self.notice_form, bg='white', width=900, height=900)
        Canvas_notice_bg.pack()

        root.withdraw()
        self.notice_form.title("사장님 공지")
        self.notice_form.geometry('550x540')
        self.master.withdraw()

        self.notice_form.owner_notice_top_frame = tk.Frame(Canvas_notice_bg, width=550, height=50, bg='#25c4be')
        self.notice_form.owner_notice_top_frame.pack()
        self.notice_form.owner_notice_top_frame.pack_propagate(False)

        self.shop = tk.Label(self.notice_form.owner_notice_top_frame, text=self.user_store_name, font=('맑은 고딕', 15),
                             bg='#25c4be', fg='white')
        self.shop.pack(side="right", padx=2)

        self.logo = tk.Label(self.notice_form.owner_notice_top_frame, image=baeminLogo_img, bd=0)
        self.logo.pack(side="left")

        self.notice_form.owner_notice_frame = tk.Frame(Canvas_notice_bg, width=550, height=850, bg="white")
        self.notice_form.owner_notice_frame.pack()
        self.notice_form.owner_notice_frame.pack_propagate(False)

        self.notice_form.owner_notice_owner_label = tk.Label(self.notice_form.owner_notice_frame,
                                                             font=('arial', 15, 'bold'), bg='white', fg='black',
                                                             text="사장님 공지")
        self.notice_form.owner_notice_owner_label.pack(side='top', anchor='w', padx=50, pady=15)

        scrollbar = tk.Scrollbar(self.notice_form.owner_notice_frame)
        scrollbar.pack(side='right', fill='y')


        self.owner_notice_text = tk.Text(self.notice_form.owner_notice_frame, font=('맑은 고딕', 10), width=60,
                                         height=20,
                                         bg='white', yscrollcommand=scrollbar.set)
        self.owner_notice_text.insert(tk.END,owner_notice)
        self.owner_notice_text.pack()
        scrollbar.config(command=self.owner_notice_text.yview)

        save_bt = tk.Button(self.notice_form.owner_notice_frame, text="저장하기", fg="white", bg="lightgray",
                            font=('arial', 13, 'bold'), relief='flat', width=9, bd=0, background="lightgray",
                            activebackground="lightgray", command=self.review_owner_notice_save)
        save_bt.pack(anchor='e', padx=61, pady=(20, 40))

    def review_owner_notice_save(self):
        notice_text_content = self.owner_notice_text.get("1.0", "end-1c")
        print(notice_text_content)
        self.sock.send(("#103 "+self.user_store_name+"||"+ notice_text_content).encode())
        self.notice_form.destroy()

    def review_owner_word(self):
        self.sock.send(("#99 "+self.user_store_name).encode())
    def create_owner_word(self, word):
        self.word_form = tk.Toplevel(self.master)
        self.word_form.resizable(False, False)
        Canvas_word_bg = tk.Canvas(self.word_form, bg='white', width=900, height=900)
        Canvas_word_bg.pack()

        root.withdraw()
        self.word_form.title("사장님 한마디")
        self.word_form.geometry('550x540')
        self.master.withdraw()

        self.word_form.owner_word_top_frame = tk.Frame(Canvas_word_bg, width=550, height=50, bg='#25c4be')
        self.word_form.owner_word_top_frame.pack()
        self.word_form.owner_word_top_frame.pack_propagate(False)

        self.shop = tk.Label(self.word_form.owner_word_top_frame, text=self.user_store_name, font=('맑은 고딕', 15),
                             bg='#25c4be', fg='white')
        self.shop.pack(side="right", padx=2)

        self.logo = tk.Label(self.word_form.owner_word_top_frame, image=baeminLogo_img, bd=0)
        self.logo.pack(side="left")

        self.word_form.owner_word_frame = tk.Frame(Canvas_word_bg, width=550, height=850, bg="white")
        self.word_form.owner_word_frame.pack()
        self.word_form.owner_word_frame.pack_propagate(False)

        self.word_form.owner_word_owner_label = tk.Label(self.word_form.owner_word_frame,
                                                         font=('arial', 15, 'bold'), bg='white', fg='black',
                                                         text="사장님 한마디")
        self.word_form.owner_word_owner_label.pack(side='top', anchor='w', padx=50, pady=15)

        scrollbar = tk.Scrollbar(self.word_form.owner_word_frame)
        scrollbar.pack(side='right', fill='y')
        self.owner_word_text = tk.Text(self.word_form.owner_word_frame, font=('맑은 고딕', 10), width=60,
                                       height=20,
                                       bg='white', yscrollcommand=scrollbar.set)
        self.owner_word_text.insert(tk.END,word)
        self.owner_word_text.pack()
        scrollbar.config(command=self.owner_word_text.yview)

        save_bt = tk.Button(self.word_form.owner_word_frame, text="저장하기", fg="white", bg="lightgray",
                            font=('arial', 13, 'bold'), relief='flat', width=9, bd=0, background="lightgray",
                            activebackground="lightgray", command=self.review_owner_word_save)
        save_bt.pack(anchor='e', padx=61, pady=(20, 40))

    def review_owner_word_save(self):
        word_text_content = self.owner_word_text.get("1.0", "end-1c")
        print(word_text_content)
        self.sock.send(("#104 " + self.user_store_name + "||" + word_text_content).encode())
        self.word_form.destroy()





    def review_write(self, frame, re_text,review_idx):
        text = re_text.get("1.0", tk.END)
        re_text.place_forget()
        self.review_label = tk.Label(frame, text=text, font=('맑은 고딕', 10), width=45, height=6,
                                     bg='#EBDDCC', wraplength=350)  # 리뷰 레이블
        self.review_label.place(x=110, y=200)
        self.sock.send(("#109 "+review_idx+"||"+text).encode())
        self.review_items_canvas.update_idletasks()
        #self.owner_review_list.append(self.review_label)


    def open_owner_menu_form(self, menu_data):
        global menu_form
        menu_form = tk.Toplevel(self.master)
        Canvas_review_bg = tk.Canvas(menu_form, bg='white', width=550, height=850)
        Canvas_review_bg.pack()
        root.withdraw()
        menu_form.title('main - 메뉴관리')
        menu_form.geometry('550x850')
        # main_form.back = tk.Button(main_form, text='뒤로가기', font=('', 20), command=self.close_main_form)
        # main_form.back.pack(side='right')
        menu_form.shop = tk.Label(menu_form, text='가게이름', font=('', 20), bg='white')
        menu_form.shop.place(x=20, y=20)
        menu_form.orderList = tk.Button(menu_form, text='주문내역', font=('', 20), bg='white', bd=0,
                                        command=self.open_owner_main_form)
        menu_form.orderList.place(x=460, y=20)
        menu_form.view = tk.Button(menu_form, text='리뷰관리', font=('', 20), bg='white', bd=0,
                                   command=self.open_owner_review_form)
        menu_form.view.place(x=580, y=20)
        menu_form.menu = tk.Button(menu_form, text='메뉴관리', font=('', 20), bg='white', bd=0)
        menu_form.menu.place(x=700, y=20)

        tmp_data = menu_data.split("메뉴클릭")

        # self.menu_cate_frame = tk.Frame(self.menu_frame, width=550, height=100, bg="lightgrey")
        # self.menu_cate_frame.place(y=21)
        # self.menu_cate_frame.pack_propagate(False)

        # menu_form.sign_up = tk.Button(menu_form, text='메뉴 등록', font=('', 20), bg='white', bd=0,
        #                              command=self.open_owner_menu_sign_up_form)
        # menu_form.sign_up.place(x=20, y=800)
        # menu_form.change = tk.Button(menu_form, text='수정', font=('', 20), bg='white', bd=0,
        #                             command=self.open_owner_menu_sign_up_form)
        # menu_form.change.place(x=600, y=800)
        # menu_form.change = tk.Button(menu_form, text='삭제', font=('', 20), bg='white', bd=0)
        # menu_form.change.place(x=700, y=800)
        # menu_form.food = tk.Label(menu_form, image=pizza_img, width=80, height=70, bg='white', bd=0)
        # menu_form.food.place(x=135, y=130)
        # menu_form.information = tk.Label(menu_form, text='메뉴 정보', font=('', 20), bg='white')
        # menu_form.information.place(x=300, y=130)
        # menu_cate_button = tk.Button(self.menu_cate_frame, text='카테고리1', font=('',12), bg='white', bd=1)
        # menu_cate_button.pack(side="left")

    def img_add(self):
        global menu_sign_up_form
        img_path = filedialog.askopenfilename(initialdir="\\", title="이미지 선택",
                                              filetypes=(("이미지 파일", "*.png *.jpg *.jpeg"), ("모든 파일", "*.*")))
        if img_path:
            self.image_path = img_path

            img = Image.open(img_path)
            width, height = menu_sign_up_form.imageAdd.winfo_width(), menu_sign_up_form.imageAdd.winfo_height()
            img.thumbnail((width, height))
            img.thumbnail((width, height))
            photo = ImageTk.PhotoImage(img)
            menu_sign_up_form.imageAdd.config(image=photo)
            menu_sign_up_form.imageAdd.image = photo

    def get_checked_menus(self):
        checked_menus = []
        for checkbox_var, checkbox in self.menu_checkbox:
            if checkbox_var.get() == 1:
                checked_menus.append((checkbox_var, checkbox))
        return checked_menus

    def edit_selected_menu(self, existing_info=None):
        checked_menus = self.get_checked_menus()
        if not checked_menus:
            tk.messagebox.showinfo("알림", "수정할 메뉴를 선택해주세요.")
            return

        global menu_sign_up__chagne_form
        menu_sign_up_change_form = tk.Toplevel(self.master)
        background = tk.Canvas(menu_sign_up_change_form, bg='white', width=650, height=850)
        background.pack()
        background.pack_propagate(False)
        Canvas_main_bg = tk.Canvas(background, bg='#25c4be', width=550, height=50)
        Canvas_main_bg.pack()
        Canvas_main_bg.pack_propagate(False)
        root.withdraw()
        menu_sign_up_change_form.title('main - 메뉴관리 - 메뉴수정')
        menu_sign_up_change_form.geometry('550x850')
        menu_sign_up_change_form.resizable(False, False)
        # main_form.back = tk.Button(main_form, text='뒤로가기', font=('', 20), command=self.close_main_form)
        # main_form.back.pack(side='right')
        font_instance = font.Font(family="맑은 고딕", size=15)
        self.shop = tk.Label(Canvas_main_bg, text=self.user_store_name, font=font_instance, bg='#25c4be', fg='white')
        self.shop.pack(side="right", padx=2)
        self.logo = tk.Label(Canvas_main_bg, image=baeminLogo_img, bd=0)
        self.logo.pack(side="left")
        # 메뉴명
        menu_sign_up_change_form.menuName = tk.Label(background, text='메뉴명', font=('맑은 고딕', 13), bd=0, bg='white')
        menu_sign_up_change_form.menuName.pack(anchor="w", padx=10, pady=5)
        menu_sign_up_change_form.menuName_entry = tk.Entry(background, font=('', 10), width=25, relief="solid", bd=1)
        menu_sign_up_change_form.menuName_entry.pack(anchor="w", padx=10, pady=5)
        # 카테고리 분류
        menu_sign_up_change_form.cate_type = tk.Label(background, text='카테고리 분류', font=('맑은 고딕', 13), bd=0, bg='white')
        menu_sign_up_change_form.cate_type.pack(anchor="w", padx=10, pady=5)
        menu_sign_up_change_form.cate_type_entry = tk.Entry(background, font=('', 10), width=25, relief="solid", bd=1)
        menu_sign_up_change_form.cate_type_entry.pack(anchor="w", padx=10, pady=5)
        # 가격
        menu_sign_up_change_form.price = tk.Label(background, text='가격', font=('맑은 고딕', 13), bd=0, bg='white')
        menu_sign_up_change_form.price.pack(anchor="w", padx=10, pady=5)
        menu_sign_up_change_form.price_entry = tk.Entry(background, font=('', 10), width=25, relief="solid", bd=1)
        menu_sign_up_change_form.price_entry.pack(anchor="w", padx=10, pady=5)
        # 메뉴설명
        menu_sign_up_change_form.content = tk.Label(background, text='메뉴설명', font=('맑은 고딕', 13), bd=0, bg='white')
        menu_sign_up_change_form.content.pack(anchor="w", padx=10, pady=5)
        menu_sign_up_change_form.price_text = tk.Text(background, font=('', 10), width=70, height=15, relief="solid",
                                                      bd=1)
        menu_sign_up_change_form.price_text.pack(anchor="w", padx=10, pady=5)
        # 메뉴 이미지
        menu_sign_up_change_form.information = tk.Label(background, text='메뉴 사진', font=('맑은 고딕', 13), bg='white')
        menu_sign_up_change_form.information.pack(anchor="w", padx=10, pady=5)
        menu_sign_up_change_form.imageAddButton = tk.Button(background, text='이미지 추가', font=('맑은 고딕', 10), width=11,
                                                            height=1, bd=1, relief='ridge', bg='white',
                                                            command=self.img_add)
        menu_sign_up_change_form.imageAddButton.place(x=110, y=492)
        menu_sign_up_change_form.imageAdd = tk.Label(background, text='이미지', font=('', 8), width=160, height=200,
                                                     bg='white')
        menu_sign_up_change_form.imageAdd.pack(anchor="w", padx=10, pady=5)
        # 수정
        menu_sign_up_change_form.sign_up = tk.Button(background, text='수정하기', font=('맑은 고딕', 15), bg='white', bd=0)
        menu_sign_up_change_form.sign_up.place(x=150, y=800)
        # 취소
        menu_sign_up_form.change = tk.Button(background, text='취소하기', font=('맑은 고딕', 15), bg='white',
                                             bd=0,
                                             command=self.menu_sgin_up_cancel)
        menu_sign_up_form.change.place(x=295, y=800)

        # 체크된 메뉴가 하나 이상인 경우에만 실행
        if len(checked_menus) > 0:
            # 여러 메뉴 중 첫 번째 체크된 메뉴의 정보를 가져옴
            first_menu_info = checked_menus[0]
            checkbox_var, checkbox = first_menu_info

            # 메뉴명 entry에 체크된 메뉴의 메뉴명 채우기
            menu_name = self.checkbox_widgets[0]['text']  # 체크된 메뉴의 메뉴명
            menu_sign_up_form.menuName_entry.delete(0, tk.END)
            menu_sign_up_form.menuName_entry.insert(0, menu_name)

            # 카테고리 entry에 체크된 메뉴의 카테고리 채우기
            category = self.checkbox_widgets[1]['text']  # 체크된 메뉴의 카테고리
            menu_sign_up_form.cate_type_entry.delete(0, tk.END)
            menu_sign_up_form.cate_type_entry.insert(0, category)

            # 가격 entry에 체크된 메뉴의 가격 채우기
            price = self.checkbox_widgets[3]['text']  # 체크된 메뉴의 가격
            menu_sign_up_form.price_entry.delete(0, tk.END)
            menu_sign_up_form.price_entry.insert(0, price)

            # 메뉴 설명 text에 체크된 메뉴의 설명 채우기
            description = self.checkbox_widgets[4]['text']  # 체크된 메뉴의 설명
            menu_sign_up_form.price_text.delete('1.0', tk.END)
            menu_sign_up_form.price_text.insert('1.0', description)

            # 이미지 추가 버튼을 눌렀을 때 이미지가 미리 표시되도록 하기 위해 이미지 경로 저장
            self.image_path = self.checkbox_widgets[2]['image_path']

            # 이미지 표시
            if self.image_path:
                img = Image.open(self.image_path)
                img = img.resize((160, 200), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)
                menu_sign_up_form.imageAdd.config(image=img)
                menu_sign_up_form.imageAdd.image = img

    def open_owner_menu_sign_up_form(self, existing_info=None):
        global menu_sign_up_form
        menu_sign_up_form = tk.Toplevel(self.master)
        self.background = tk.Canvas(menu_sign_up_form, bg='white', width=650, height=850)
        self.background.pack()
        self.background.pack_propagate(False)
        Canvas_main_bg = tk.Canvas(self.background, bg='#25c4be', width=550, height=50)
        Canvas_main_bg.pack()
        Canvas_main_bg.pack_propagate(False)
        root.withdraw()
        menu_sign_up_form.title('main - 메뉴관리 - 메뉴등록')
        menu_sign_up_form.geometry('550x850')
        menu_sign_up_form.resizable(False, False)
        # main_form.back = tk.Button(main_form, text='뒤로가기', font=('', 20), command=self.close_main_form)
        # main_form.back.pack(side='right')
        font_instance = font.Font(family="맑은 고딕", size=15)
        self.shop = tk.Label(Canvas_main_bg, text=self.user_store_name, font=font_instance, bg='#25c4be', fg='white')
        self.shop.pack(side="right", padx=2)
        self.logo = tk.Label(Canvas_main_bg, image=baeminLogo_img, bd=0)
        self.logo.pack(side="left")
        # 메뉴명
        menu_sign_up_form.menuName = tk.Label(self.background, text='메뉴명', font=('맑은 고딕', 13), bd=0, bg='white')
        menu_sign_up_form.menuName.pack(anchor="w", padx=10, pady=15)
        menu_sign_up_form.menuName_entry = tk.Entry(self.background, font=('', 10), width=25, relief='solid', bd=1)
        menu_sign_up_form.menuName_entry.pack(anchor="w", padx=10, pady=5)
        # 가격
        menu_sign_up_form.price = tk.Label(self.background, text='가격', font=('맑은 고딕', 13), bd=0, bg='white')
        menu_sign_up_form.price.pack(anchor="w", padx=10, pady=15)
        menu_sign_up_form.price_entry = tk.Entry(self.background, font=('', 10), width=25, relief='solid', bd=1)
        menu_sign_up_form.price_entry.pack(anchor="w", padx=10, pady=5)
        # 메뉴설명
        menu_sign_up_form.content = tk.Label(self.background, text='메뉴설명', font=('맑은 고딕', 13), bd=0, bg='white')
        menu_sign_up_form.content.pack(anchor="w", padx=10, pady=15)
        menu_sign_up_form.price_text = tk.Text(self.background, font=('', 10), width=70, height=15, relief='solid',
                                               bd=1)
        menu_sign_up_form.price_text.pack(anchor="w", padx=10, pady=5)
        # 메뉴 이미지
        menu_sign_up_form.information = tk.Label(self.background, text='메뉴 사진', font=('맑은 고딕', 13), bg='white')
        menu_sign_up_form.information.pack(anchor="w", padx=10, pady=15)
        menu_sign_up_form.imageAddButton = tk.Button(self.background, text='이미지 추가', font=('맑은 고딕', 10), width=11,
                                                     height=1, bd=1, relief='ridge', bg='white', command=self.img_add)
        menu_sign_up_form.imageAddButton.place(x=110, y=500)
        menu_sign_up_form.imageAdd = tk.Label(self.background, font=('', 8), width=160, height=200,
                                              bg='white')
        menu_sign_up_form.imageAdd.pack(anchor="w", padx=10, pady=5)
        # 등록/취소
        menu_sign_up_form.sign_up = tk.Button(self.background, text='등록하기', font=('맑은 고딕', 15), bg='white', bd=0,
                                              command=self.register_new_menu)
        menu_sign_up_form.sign_up.place(x=150, y=800)

        menu_sign_up_form.change = tk.Button(self.background, text='취소하기', font=('맑은 고딕', 15), bg='white', bd=0,
                                             command=self.menu_sgin_up_cancel)
        menu_sign_up_form.change.place(x=295, y=800)

        if existing_info:
            menu_name = existing_info[0]
            image = existing_info[1]
            price = existing_info[2]
            description = existing_info[3]

            # 체크박스에 추가되는 정보
            self.checkbox_info = [menu_name, image, price, description]

            # 메뉴 체크박스 추가
            self.add_menu_checkbox(self.checkbox_info)

    def open_owner_information_origin_form(self):
        self.sock.send(("#101 " + self.user_store_name).encode())
        global owner_information_origin_form
        owner_information_origin_form = tk.Toplevel(self.master)
        owner_information_origin_form.title('사장님 - 정보/원산지')
        owner_information_origin_form.geometry('550x850')
        owner_information_origin_form.resizable(False, False)
        background = tk.Canvas(owner_information_origin_form, bg='white', width=650, height=850)
        background.pack()
        background.pack_propagate(False)
        Canvas_main_bg = tk.Canvas(background, bg='#25c4be', width=550, height=50)
        Canvas_main_bg.pack()
        Canvas_main_bg.pack_propagate(False)
        root.withdraw()

        self.logo = tk.Label(Canvas_main_bg, image=baeminLogo_img, bd=0)
        self.logo.place(x=10, y=5)

        # owner_information_origin_canvas = tk.Canvas(owner_information_origin_form, bg='white')
        # owner_information_origin_canvas.pack()

        # 가게이름
        owner_information_origin_form.rest_name = tk.Label(background, font=('Arial', 15, 'bold'),
                                                           bg='white', text=self.user_store_name)
        owner_information_origin_form.rest_name.pack(side='left', anchor='nw', padx=10, pady=10)

        line1 = tk.Frame(background, bg='lightgray', height=15, width=550)
        line1.place(x=0, y=110)

        # 상호명
        owner_information_origin_form.rest_spot_name = tk.Label(background, font=('맑은 고딕', 15),
                                                                bg='white', text='상호명')
        owner_information_origin_form.rest_spot_name.place(x=10, y=140)
        owner_information_origin_form.rest_spot_name2 = tk.Label(background, font=('맑은 고딕', 15),
                                                                 bg='white', text=self.user_store_name)
        owner_information_origin_form.rest_spot_name2.place(x=200, y=140)
        # 운영시간
        owner_information_origin_form.time = tk.Label(background, font=('맑은 고딕', 15), bg='white',
                                                      text='운영시간')
        owner_information_origin_form.time.place(x=10, y=230)
        owner_information_origin_form.time2 = tk.Label(background, font=('맑은 고딕', 15), bg='white',
                                                       text=self.owner_store_info[1])
        owner_information_origin_form.time2.place(x=200, y=230)
        # 휴무일
        owner_information_origin_form.breakTime = tk.Label(background, font=('맑은 고딕', 15), bg='white',
                                                           text='휴무일')
        owner_information_origin_form.breakTime.place(x=10, y=320)
        owner_information_origin_form.breakTime2 = tk.Label(background, font=('맑은 고딕', 15), bg='white',
                                                            text=self.owner_store_info[2])
        owner_information_origin_form.breakTime2.place(x=200, y=320)
        # 전화번호
        owner_information_origin_form.phoneNumber = tk.Label(background, font=('맑은 고딕', 15), bg='white',
                                                             text='전화번호')
        owner_information_origin_form.phoneNumber.place(x=10, y=410)
        owner_information_origin_form.phoneNumber2 = tk.Label(background, font=('맑은 고딕', 15), bg='white',
                                                              text=self.owner_store_info[3])
        owner_information_origin_form.phoneNumber2.place(x=200, y=410)
        # 배달지역
        owner_information_origin_form.area = tk.Label(background, font=('맑은 고딕', 15), bg='white',
                                                      text='배달지역')
        owner_information_origin_form.area.place(x=10, y=500)
        owner_information_origin_form.area2 = tk.Label(background, font=('맑은 고딕', 15), bg='white',
                                                       text=self.owner_store_info[4])
        owner_information_origin_form.area2.place(x=200, y=500)

        line2 = tk.Frame(background, bg='lightgray', height=15, width=550)
        line2.place(x=0, y=560)

        # 가게소개
        owner_information_origin_form.rest_introduce = tk.Label(background,
                                                                font=('Arial', 15, 'bold'), bg='white', text='가게소개')
        owner_information_origin_form.rest_introduce.place(x=10, y=600)
        owner_information_origin_form.rest_introduce2 = tk.Label(background, font=('맑은 고딕', 15),
                                                                 bg='white', text=self.owner_store_info[5],
                                                                 wraplength=550, justify="left")
        owner_information_origin_form.rest_introduce2.place(x=10, y=650)

    def add_menu_checkbox(self, menu_name, image_path, price, description):
        menu_checkbox_var = IntVar()
        menu_checkbox = (menu_checkbox_var, menu_name, image_path, price, description)

        self.menu_up_frame = tk.Frame(self.menu_inner_frame, width=550, bg='white')
        self.menu_up_frame.pack(side='top', fill='y', padx=110, pady=20)

        menu_up_checkbox = Checkbutton(self.menu_up_frame, variable=menu_checkbox_var, bg='white')
        menu_up_checkbox.grid(row=0, column=0)
        self.menu_checkbox.append((menu_checkbox_var, menu_up_checkbox))

        information = tk.Label(self.menu_up_frame, text=menu_name, font=('', 15), bg='white')
        information.grid(row=1, column=0)
        self.checkbox_widgets.append(information)

        if image_path:
            img = Image.open(image_path)
            img = img.resize((150, 130), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            food = tk.Label(self.menu_up_frame, image=img, width=150, height=130, bg='white', bd=0)
            food.image = img  # reference를 유지하기 위해 필요함
            food.grid(row=2, column=0)
            self.checkbox_widgets.append(food)

        price_label = tk.Label(self.menu_up_frame, text=price, font=('', 15), bg='white')
        price_label.grid(row=3, column=0)
        self.checkbox_widgets.append(price_label)

        menu_detail = tk.Label(self.menu_up_frame, text=description, font=('', 13), bg='white', fg='grey',
                               wraplength=350)
        menu_detail.grid(row=4, column=0)
        self.checkbox_widgets.append(menu_detail)

        self.menu_canvas.update_idletasks()  # 캔버스 내용 업데이트
        self.menu_canvas.config(scrollregion=self.menu_canvas.bbox("all"))  # 스크롤 영역 업데이트

    def register_new_menu(self):
        menu_name = menu_sign_up_form.menuName_entry.get()
        image_path = self.image_path
        price = menu_sign_up_form.price_entry.get()
        description = menu_sign_up_form.price_text.get("1.0", tk.END)

        self.add_menu_checkbox(menu_name, image_path, price, description)

        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        image_encoded = base64.b64encode(image_data)
        image_str = image_encoded.decode("utf-8")

        self.info_str = ', '.join(map(str, [menu_name, image_str, price, description]))
        self.info_str = '"' + self.info_str + '"'

        self.sock.send(("#102 " + self.user_store_name + self.info_str).encode())
        menu_sign_up_form.destroy()
        print("#102 " + self.user_store_name + self.info_str)

    def menu_delete(self):
        checkbox_to_delete = []
        for checkbox_var, checkbox in self.menu_checkbox:
            if checkbox_var.get() == 1:
                response = tk.messagebox.askquestion("확인", "해당 메뉴를 삭제하시겠습니까?")
                if response == 'yes':
                    checkbox_to_delete.append((checkbox_var, checkbox))

        if not checkbox_to_delete:
            tk.messagebox.showinfo("알림", "삭제할 메뉴를 선택해주세요.")
            return

        for checkbox_var, checkbox in checkbox_to_delete:
            # 삭제할 체크박스와 관련된 위젯 모두 삭제
            widgets_to_delete = []
            for widget in self.checkbox_widgets:
                if isinstance(widget, tk.Widget) and isinstance(checkbox, tk.Widget):
                    if widget.master == checkbox.master:
                        widgets_to_delete.append(widget)
                        widget.destroy()
                        # 이미지 위젯 제거
                        if hasattr(widget, 'image'):
                            widget.image = None
            self.checkbox_widgets = [widget for widget in self.checkbox_widgets if widget not in widgets_to_delete]

            checkbox.destroy()  # 체크박스를 삭제
            self.menu_checkbox.remove((checkbox_var, checkbox))  # 리스트에서도 제거

        # # 삭제된 메뉴 아래에 있는 메뉴들의 위치 조정
        # index = self.menu_inner_frame.grid_slaves().index(checkbox)  # 삭제된 메뉴의 인덱스
        # for widget in self.menu_inner_frame.grid_slaves():  # 그리드 슬레이브들을 순회하며
        #     if self.menu_inner_frame.grid_slaves().index(widget) > index:  # 삭제된 메뉴 아래에 위치한 경우
        #         widget.grid_forget()  # 잠시 숨기고
        #         widget.grid(row=self.menu_inner_frame.grid_location(widget)[1] - 1, column=0, sticky="w")  # 한 칸 위로 이동

        self.menu_canvas.update_idletasks()  # 캔버스 내용 업데이트
        self.menu_canvas.config(scrollregion=self.menu_canvas.bbox("all"))  # 스크롤 영역 업데이트

    def menu_sgin_up_cancel(self):
        global menu_sign_up_form

        response = tk.messagebox.askquestion("확인", "정말로 취소하시겠습니까?")

        if response == 'yes':
            menu_sign_up_form.destroy()
    def rcvMsg(self, sock):
        while True:
            try:
                self.data = sock.recv(2072576)
                print(self.data.decode()[:4])
                if "정상_유저" in self.data.decode():
                    self.user_id = self.data.decode().split()[1]
                    tkinter.messagebox.showinfo("", "로그인 성공!")
                    self.create_main_form()
                    self.user_login=True
                if "정상_사장님" in self.data.decode():
                    self.user_store_name = self.data.decode().split('#')[0]
                    self.user_store_name = self.user_store_name[7:]
                    tkinter.messagebox.showinfo("", "로그인 성공!")
                    self.open_owner_main_form(self.data.decode().split('#')[1])
                    self.owner_login=True
                elif self.data.decode() == "비정상":
                    tkinter.messagebox.showinfo("", "아이디 및 비밀번호를 확인해주세요")
                elif "카테고리"in self.data.decode():
                    self.store_info = self.data.decode()[5:]
                    print(self.data.decode()[5:])
                    self.create_select_store(self.store_info)
                elif "가게정보 및 메뉴" == self.data.decode()[:9]:
                    self.store_info_info_menu = self.data.decode()[9:]
                    self.set_menu(self.store_info_info_menu)
                elif "메뉴클릭" in self.data.decode():
                    print("들어오기는해?")
                    self.create_menu_click_form(self.data.decode()[5:])
                elif "사장메뉴" in self.data.decode():
                    self.display_menu_info_a = self.data.decode()[5:].split("메뉴정보")
                    for menu_data_str in self.display_menu_info_a:
                        self.display_menu_info = menu_data_str.split("||")

                    self.menu_up_checkbox.grid(row=0, column=0)
                    self.information = tk.Label(self.menu_up_frame, text=self.display_menu_info[0], font=('', 15),
                                                bg='white')
                    self.information.grid(row=1, column=0)
                    self.checkbox_widgets.append(self.information)

                    try:
                        food_menu_img = self.display_menu_info[1]
                        if food_menu_img != "None":
                            food_tmpImg = food_menu_img[2:-1]
                            food_tmpImg = food_tmpImg.encode()
                            decode_image_data = base64.b64decode(food_tmpImg)
                            image = Image.open(io.BytesIO(decode_image_data))
                            image = image.resize((150, 150))
                            self.tk_image = ImageTk.PhotoImage(image)
                            food_img_label = tk.Label(self.menu_up_frame, image=self.tk_image, bg='white')
                            food_img_label.image = self.tk_image  # Keep a reference to avoid garbage collection
                            food_img_label.grid(row=2, column=0)
                            self.checkbox_widgets.append(self.tk_image)
                    except Exception as e:
                        print("An error occurred:", e)
                    self.price = tk.Label(self.menu_up_frame, text=self.display_menu_info[3], font=('', 15), bg='white')
                    self.price.grid(row=3, column=0)
                    self.checkbox_widgets.append(self.price)
                    self.menu_detail = tk.Label(self.menu_up_frame, text=self.display_menu_info[2], font=('', 13),
                                                bg='white',
                                                fg='grey', wraplength=350)
                    self.menu_detail.grid(row=4, column=0)
                    self.checkbox_widgets.append(self.menu_detail)
                elif "my배민" in self.data.decode():
                    self.mybaemin = self.data.decode()[5:]
                    self.a = self.mybaemin.split('||')
                    self.addr.configure(text=self.a[3])
                elif "사장님가게정보" in self.data.decode():
                    self.owner_store_info_a = self.data.decode()[9:]
                    self.owner_store_info = self.owner_store_info_a.split("||")
                    print(self.owner_store_info)
                elif "사장님공지" in self.data.decode():
                    self.owner_notice = self.data.decode()[6:]
                    self.create_owner_notice(self.owner_notice)
                elif "사장님한마디" in self.data.decode():
                    self.owner_word = self.data.decode()[7:]
                    self.create_owner_word(self.owner_word)
                elif "주문도착" == self.data.decode():
                    if self.owner_login:
                        tkinter.messagebox.showinfo("", "주문이 도착했습니다!")
                elif "업데이트오더" in self.data.decode():
                    self.update_order_frame(self.data.decode()[7:], 0)
                elif "손님알림" in self.data.decode():
                    if self.user_login:
                        tkinter.messagebox.showinfo("", self.data.decode()[5:])
                elif "주문내역" == self.data.decode()[:4]:
                    self.order_form(self.data.decode()[5:])
                elif "리뷰사장님" == self.data.decode()[:5]:
                    print()
                    self.create_review_info(self.data.decode()[6:])

            except Exception:
                pass

    def change_loc_left(self):
        buttons = [main_form.testbut1, main_form.testbut2, main_form.testbut3, main_form.testbut4, main_form.testbut7,
                   main_form.testbut8, main_form.testbut9, main_form.testbut10
            ,main_form.testbut11, main_form.testbut12, main_form.testbut13, main_form.testbut14, main_form.testbut15,
                   main_form.testbut16, main_form.testbut17]
        for button in buttons:
            current_x = button.winfo_x()
            if current_x < -540 and button != main_form.testbut1:
                return
        for button in buttons:
            current_x = button.winfo_x()
            new_x = current_x - 80
            button.place(x=new_x, y=95)

    def change_loc_right(self):
        buttons = [main_form.testbut1, main_form.testbut2, main_form.testbut3, main_form.testbut4, main_form.testbut7,
                   main_form.testbut8, main_form.testbut9, main_form.testbut10
            ,main_form.testbut11, main_form.testbut12, main_form.testbut13, main_form.testbut14, main_form.testbut15,
                   main_form.testbut16, main_form.testbut17]
        for button in buttons:
            current_x = button.winfo_x()
            if current_x > 1020 and button != main_form.testbut17:
                # testbut11 버튼의 x 좌표가 920 이상인 경우 모든 버튼의 이동 중단
                return
        for button in buttons:
            current_x = button.winfo_x()
            new_x = current_x + 80
            button.place(x=new_x, y=95)
    def create_main_form(self):
        global main_form
        main_form = tk.Toplevel(self.master)
        main_form.resizable(0,0)
        self.main_frame = tk.Frame(main_form, bg='white', width=550, height=625)
        self.up_main_frame = tk.Frame(main_form, bg='white', width=550, height=250)
        self.down_main_frame = tk.Frame(main_form, bg='white', width=550, height=75)
        root.withdraw()
        main_form.title('배달의민족')
        main_form.geometry('550x850')
        self.main_form()
        self.main_form_up()
        self.main_form_down()

    def main_form_up(self):
        self.sock.send(('#5 ' + self.user_id).encode())

        self.up_main_frame.place(x=0, y=0)
        font_instance1 = font.Font(family="Arial Black", size=10, weight='bold')
        font_instance2 = font.Font(family="Arial Black", size=14, weight='bold')
        main_form.store_del = tk.Label(self.up_main_frame, text="가게 배달",font=font_instance2, bg='white')
        main_form.store_del.place(x=0,y=0)
        self.addr = tk.Label(self.up_main_frame, text="", font=font_instance1, bg='white')
        self.addr.place(x=20, y=50)
        main_form.home = tk.Button(self.up_main_frame, bg='white', bd=0, image=del_home_img, width=30, height=30, command=self.main_form)
        main_form.home.place(x=470, y=10)
        main_form.basket = tk.Button(self.up_main_frame, image=del_basket_img, bg='white', width=30, height=30, bd=0,command=self.go_basket)
        main_form.basket.place(x=510, y=5)
        main_form.advertistment = tk.Label(self.up_main_frame,  image=ad1_img)
        main_form.advertistment.place(x=-2, y=77)
        # 메인 폼

    def main_form(self):
        if hasattr(self, 'basket_frame'):  # hasattr은 객체가 속성을 갖는지 판단 self에서 basket_frame이 있으면 true 없으면 false 반환
            self.basket_frame.place_forget()
            self.up_basket_frame.place_forget()
            self.down_basket_frame.place_forget()
        if hasattr(self, 'select_store_frame'):
            self.select_store_frame.place_forget()
        if hasattr(self, 'up_select_store_frame'):
            self.up_select_store_frame.place_forget()
        if hasattr(self, 'choice_menu_frame'):
            self.choice_menu_frame.place_forget()
        if hasattr(self, 'up_choice_menu_frame'):
            self.up_choice_menu_frame.place_forget()
        if hasattr(self, 'search_frame'):
            self.search_frame.place_forget()
        if hasattr(self, 'up_search_frame'):
            self.up_search_frame.place_forget()
        if hasattr(self, 'up_info_frame'):
            self.up_info_frame.place_forget()
            self.info_frame.place_forget()
            self.down_info_frame.place_forget()
        if hasattr(self, 'total_order'):
            self.total_order.pack_forget()
            # self.up_total_order.pack_forget()
        if hasattr(self, 'repair_form_frame'):
            self.repair_form_frame.place_forget()
            self.up_repair_form_frame.place_forget()
            self.down_repair_form_frame.place_forget()
        if hasattr(self, 'canvas_menu_click'):
            self.canvas_menu_click.pack_forget()
        if hasattr(self, 'select_store_frame'):
            self.select_store_frame.place_forget()
            self.up_select_store_frame.place_forget()
            self.canvas_select_store.pack_forget()
        if hasattr(self, 'menu_frame21'):
            self.menu_click_frame1.pack_forget()
        self.main_form_up()
        self.main_form_down()
        self.main_frame.place(x=0, y=250)
        main_form.coup = tk.Label(self.main_frame, width=97, height=69, image=del_coup_img, bg='white').place(x=30, y=20)
        main_form.lowtip = tk.Label(self.main_frame, width=99, height=74, image=del_lowtip_img, bg='white').place(x=155, y=20)
        main_form.reorder = tk.Label(self.main_frame, width=99, height=70, image=del_reorder_img, bg='white').place( x=280, y=20)
        main_form.nice = tk.Label(self.main_frame, width=99, height=70, image=del_nice_img, bg='white').place(x=410, y=20)
        main_form.live = tk.Button(self.main_frame, width=90, height=71, image=del_pinglive_img, bg='white', bd=0).place(x=35, y=120)
        main_form.one = tk.Button(self.main_frame, width=70, height=90, image=del_one_img, bg='white',bd=0).place(x=180,y=110)
        main_form.hansik = tk.Button(self.main_frame, width=71, height=90, bg='white', image=korea_img, bd=0, command=lambda: self.choice_store('한식',0)).place(x=315, y=110)
        main_form.bunsik = tk.Button(self.main_frame, width=49, height=71, bg='white', image=del_bunski_img, bd=0, highlightthickness=0,command=lambda: self.choice_store('분식',0)).place(x=460,y=115)
        main_form.dessert = tk.Button(self.main_frame, width=71, height=71, bg='white', image=del_dessert_img, bd=0, highlightthickness=0,command=lambda: self.choice_store('디저트',0)).place(x=35, y=420)
        main_form.illsik = tk.Button(self.main_frame, width=86, height=71, bg='white', image=japan_img, bd=0, command=lambda: self.choice_store('일식',0)).place(x=30, y=220)
        main_form.chicken = tk.Button(self.main_frame, width=64, height=71, bg='white', image=chicken_img, bd=0, command=lambda: self.choice_store('치킨',0)).place(x=185, y=220)
        main_form.pizza = tk.Button(self.main_frame, width=60, height=71, bg='white', image=pizza_img, bd=0, command=lambda: self.choice_store('피자',0)).place(x=320, y=220)
        main_form.yangsik = tk.Button(self.main_frame, width=72, height=71, bg='white', image=usa_img, bd=0,command=lambda: self.choice_store('아시안',0)).place(x=445, y=215)
        main_form.jungsik = tk.Button(self.main_frame, width=60, height=71, bg='white', image=china_img, bd=0).place(x=190, y=420)
        main_form.jokbal = tk.Label(self.main_frame, width=73, height=71, bg='white', image=del_jokbal_img,  bd=0, highlightthickness=0).place(x=35,
                                                                                                                  y=320)
        main_form.yasik = tk.Label(self.main_frame, width=54, height=71, bg='white', image=del_yasik_img).place(x=190,
                                                                                                                y=320)
        main_form.soup = tk.Label(self.main_frame, width=61, height=71, bg='white', image=del_soup_img).place(x=318,
                                                                                                              y=320)
        main_form.lunch = tk.Label(self.main_frame, width=64, height=71, bg='white', image=del_lunch_img).place(x=450,
                                                                                                                y=320)
        main_form.fastfood = tk.Button(self.main_frame, width=73, height=71, bg='white', image=del_fastfood_img,command=lambda: self.choice_store('패스트푸드',0),bd=0,highlightthickness=0).place(
            x=313, y=320)

    def search(self):
        self.down_main_frame.place_forget()
        self.main_frame.place_forget()
        self.up_main_frame.place_forget()
        self.search_frame = tk.Frame(main_form, bg='white', width=550, height=1500)
        self.search_frame.place(x=0, y=70)
        self.up_search_frame = tk.Frame(main_form, bg='white', width=550, height=70)
        self.up_search_frame.place(x=0, y=0)
        search_form_home = tk.Button(self.up_search_frame, image=del_arrow_img, width=40, height=40, bg='white', bd=0, command=self.main_form)
        search_form_home.place(x=10, y=15)
        self.search_form_entry = tk.Entry(self.up_search_frame, font=('', 25))
        self.search_form_entry.place(x=70, y=20)
        main_form.basket = tk.Button(self.up_search_frame, image=del_basket_img, bg='white', width=40, height=40, bd=0,
                                     command=self.go_basket)
        main_form.basket.place(x=490, y=20)
        self.search_form_entry.bind("<KeyRelease>", self.perform_search)
    def perform_search(self, event):
        query = self.search_form_entry.get()
        search_results = [item for item in self.searchable_items if query in item]
        self.clear_search_results()
        if search_results:
            self.scrollbar_search = tk.Scrollbar(self.search_frame, orient="vertical")
            self.scrollbar_search.pack(side='right', fill='y')
            self.canvas_search = tk.Canvas(self.search_frame, yscrollcommand=self.scrollbar_search.set, bg='white', width=550,height=1000)
            self.canvas_search.pack(expand=True, fill='both')
            self.total_height = 0
            self.widget_height = 100
            for idx, result in enumerate(search_results):
                label = tk.Label(self.canvas_search, image=del_glass_img, width=50, height=50, bg='white')
                btn2 = tk.Button(self.canvas_search, text=result, width=15, height=3, bg='white',anchor='w',bd=0,font=('',9))
                self.canvas_search.create_window((10, 70 + self.total_height), window=label, anchor='nw')
                self.canvas_search.create_window((160, 70 + self.total_height), window=btn2, anchor='nw')
                self.total_height += self.widget_height

            self.canvas_search.configure(scrollregion=(0,0,0,self.total_height))
            self.scrollbar_search.config(command=self.canvas_search.yview)

            self.canvas_search.update_idletasks()
            self.canvas_search.config(scrollregion=self.canvas_search.bbox("all"))
            self.canvas_search.bind("<Configure>", self.on_canvas_configures3)
            self.canvas_search.bind_all("<MouseWheel>", self.on_mousewheels3)

        else:
            label = tk.Label(self.search_frame, text="검색 결과가 없어요.\n 다른 검색어를 입력해보세요.", font=('', 20), bg='white')
            label.place(x=100, y=500)
            main_form_cat = tk.Label(self.search_frame, image=del_cat_img, bg='white')
            main_form_cat.place(x=150, y=250)

        if query == '':
            self.clear_search_results()
            self.canvas_search.update_idletasks()
    def clear_search_results(self):
        for widget in self.search_frame.winfo_children():
            widget.destroy()
    def on_canvas_configures3(self, event):
        self.canvas_search.config(scrollregion=self.canvas_search.bbox("all"))

    def on_mousewheels3(self, event):
        self.canvas_search.yview_scroll(-1 * (event.delta // 120), "units")


    def main_form_down(self):
        self.down_main_frame.place(x=0, y=775)
        main_form.search_btn = tk.Button(self.down_main_frame, width=75, height=75, image=del_search_img, bg='white', bd=0, command=self.search).place(x=0, y=3)
        main_form.deliverystore = tk.Label(self.down_main_frame, width=75, height=75, image=del_deliverystore_img, bg='white').place(x=118, y=0)
        main_form.pick = tk.Label(self.down_main_frame, width=75, height=75, image=del_pick_img, bg='white').place( x=237, y=0)
        main_form.order_check = tk.Button(self.down_main_frame, width=75, height=75, image=del_ordered_img, bg='white', bd=0, command=self.total_order_form).place(x=357, y=1)  # 주문내역 버튼
        main_form.my_delivery = tk.Button(self.down_main_frame, width=75, height=75, image=del_mydelivery_img, bg='white', bd=0, command=self.my_info).place(x=475, y=0)  # my배민 버튼

    def plus_order(self):
        if self.request_entry.get() == "":
            tkinter.messagebox.showinfo("", "요청사항을 입력해주세요")
        else:
            now = datetime.now()
            ordertime = str(now.hour) + ":" + str(now.minute)
            weekday_list = ['월', '화', '수', '목', '금', '토', '일']
            weekday = now.weekday()
            order_date = "0" + str(now.month) + "-" + str(now.day) + "({})".format(weekday_list[weekday])
            privateKey = self.a[0] + str(random.randint(1, 1000))
            for idx, frame in enumerate(self.basket_list):  # iiiiiiiiiiiiii
                self.plz_entry.append(self.request_entry.get())
                send_order_info = (self.name + "||" + self.a[3] + "||" + self.a[0] + "||" + self.a[2] +
                                   "||배달||" + self.plz_entry[idx] + "||접수대기||" + ordertime + "||" + self.text_name[
                                       idx] + "||" + order_date + "||" + privateKey)
                print("주문 정보 {}: {}".format(idx + 1, send_order_info))
                self.sock.send(("#7 " + send_order_info).encode())
                self.sock.send(("#8 " + self.a[0] + "||" + self.name + "||" + self.text_name[idx] + "||" + str(
                    self.text_price[idx]) + "||" + order_date + "||가게 확인중||" + privateKey).encode())

                print(self.plz_entry[idx])
            for frame in self.basket_list:
                frame.place_forget()
            self.basket_list.clear()
            if not self.basket_list:
                self.basket_text.place(x=150, y=450)
                self.basket_image.place(x=175, y=200)
                self.button_more.place(x=180, y=500)

    def total_order_form(self):
        if hasattr(self, 'main_form'):
            self.main_frame.place_forget()
            self.up_main_frame.place_forget()
            self.down_main_frame.place_forget()
        if hasattr(self, 'basket_frame'):
            self.up_basket_frame.place_forget()
            self.basket_frame.place_forget()
            self.down_basket_frame.place_forget()
        self.sock.send(("#9 " + self.a[0]).encode())
        if hasattr(self, 'total_order'):
            self.total_order.pack(expand=True, fill='both')

    def canvasupdate(self):
        self.total_order.update()

    def click_star(self, click_star):
        self.rating_num ="5"
        if click_star == 1:
            self.review_form_star2.configure(image=star2)
            self.review_form_star3.configure(image=star2)
            self.review_form_star4.configure(image=star2)
            self.review_form_star5.configure(image=star2)
            self.rating_num ="1"
        if click_star == 2:
            self.review_form_star2.configure(image=star1)
            self.review_form_star3.configure(image=star2)
            self.review_form_star4.configure(image=star2)
            self.review_form_star5.configure(image=star2)
            self.rating_num ="2"
        if click_star == 3:
            self.review_form_star2.configure(image=star1)
            self.review_form_star3.configure(image=star1)
            self.review_form_star4.configure(image=star2)
            self.review_form_star5.configure(image=star2)
            self.rating_num ="3"
        if click_star == 4:
            self.review_form_star2.configure(image=star1)
            self.review_form_star3.configure(image=star1)
            self.review_form_star4.configure(image=star1)
            self.review_form_star5.configure(image=star2)
            self.rating_num ="4"

        if click_star == 5:
            self.review_form_star2.configure(image=star1)
            self.review_form_star3.configure(image=star1)
            self.review_form_star4.configure(image=star1)
            self.review_form_star5.configure(image=star1)
            self.rating_num ="5"

    def on_text_click(self,event):
        if self.review_form_text.get("1.0", tk.END).strip() == '음식의 맛, 양, 포장 상태 등 음식에 대한 솔직한 리뷰를 남겨주세요. (선택)':
            self.review_form_text.delete("1.0", tk.END)
            self.review_form_text.config(fg='black')

    def on_focus_out(self,event):
        if self.review_form_text.get("1.0", tk.END).strip() == '':
            self.review_form_text.insert("1.0", '음식의 맛, 양, 포장 상태 등 음식에 대한 솔직한 리뷰를 남겨주세요. (선택)')
            self.review_form_text.config(fg='grey')

    def send_review(self,text):
        tkinter.messagebox.showinfo("", "리뷰 등록 성공!")
        self.review_form.destroy()
        self.sock.send(("#11 "+text).encode())


    def create_review_write_form(self, store_name, menu_name):
        self.review_form=tk.Toplevel(main_form)
        self.review_form.geometry("450x500")
        self.review_form.title("리뷰작성")
        self.review_form.configure(bg="white")
        font_instance1 = font.Font(family="Arial Black", size=12, weight='bold')
        self.review_form_label1 = tk.Label(self.review_form, text="리뷰쓰기", font=font_instance1,bg='white')
        self.review_form_label1.place(relx=0.5, y=15, anchor='center')
        self.review_form_store_name = tk.Label(self.review_form, text=store_name, font=font_instance1, bg='white')
        self.review_form_store_name.place(relx=0.5, y=75, anchor='center')

        self.review_form_star1 = tk.Label(self.review_form, image=star1, bg='white')
        self.review_form_star1.place(x=120,y=96)
        self.review_form_star2 = tk.Label(self.review_form, image=star1, bg='white')
        self.review_form_star2.place(x=160, y=96)
        self.review_form_star3 = tk.Label(self.review_form, image=star1, bg='white')
        self.review_form_star3.place(relx=0.5, y=120, anchor='center')
        self.review_form_star4 = tk.Label(self.review_form, image=star1, bg='white')
        self.review_form_star4.place(x=245, y=96)
        self.review_form_star5 = tk.Label(self.review_form, image=star1, bg='white')
        self.review_form_star5.place(x=285, y=96)

        self.review_form_star1.bind("<Button-1>", lambda event, index=1: self.click_star(index))
        self.review_form_star2.bind("<Button-1>", lambda event, index=2: self.click_star(index))
        self.review_form_star3.bind("<Button-1>", lambda event, index=3: self.click_star(index))
        self.review_form_star4.bind("<Button-1>", lambda event, index=4: self.click_star(index))
        self.review_form_star5.bind("<Button-1>", lambda event, index=5: self.click_star(index))

        self.review_form_text = tk.Text(self.review_form, width=48, height=12, bd=2, fg='gray',font=('',12))
        self.review_form_text.place(x=30, y=160)
        self.review_form_text.insert("1.0", '음식의 맛, 양, 포장 상태 등 음식에 대한 솔직한 리뷰를 남겨주세요. (선택)')
        self.review_form_text.bind('<FocusIn>', self.on_text_click)
        self.review_form_text.bind('<FocusOut>', self.on_focus_out)

        self.review_form_menu_name = tk.Label(self.review_form, text=menu_name, font=font_instance1, bg='white')
        self.review_form_menu_name.place(relx=0.5, y=390, anchor='center')



        self.review_form_com_btn = tk.Button(self.review_form,image=review_com_img, bg='white',bd=0,highlightthickness=0, command=lambda : self.send_review(self.rating_num+"||"+store_name+"||"+self.review_form_text.get("1.0", "end").strip()+"||"+menu_name+"||"+self.a[0]+"||"+" "+"||null"))
        self.review_form_com_btn.place(relx=0.5, y=450, anchor='center')

    def order_form(self, data):
        if not hasattr(self, 'total_order'):
            self.scrollbar_order = tk.Scrollbar(main_form, orient="vertical")
            self.total_order = tk.Canvas(main_form, yscrollcommand=self.scrollbar_order.set, bg='#f6f6f6', width=550)
            self.total_order.pack(expand=True, fill='both')
            self.up_total_order = tk.Frame(self.total_order, bg='white', width=550, height=100)
            self.total_order.create_window((0, 0), window=self.up_total_order, anchor='nw')
            main_form.right = tk.Button(self.up_total_order, bg='white', bd=0, image=del_right_img, width=20, height=20,
                                        command=self.total_right)
            main_form.right.place(x=400, y=20)
            main_form.left = tk.Button(self.up_total_order, bg='white', bd=0, image=del_left_img,
                                       command=self.total_left, width=20, height=20)
            main_form.left.place(x=150, y=20)
            main_form.home = tk.Button(self.up_total_order, bg='white', bd=0, image=del_home_img, width=40, height=40,
                                       command=self.main_form)
            main_form.home.place(x=460, y=10)
            main_form.basket = tk.Button(self.up_total_order, image=del_basket_img, bg='white', width=40, height=40,
                                         bd=0, command=self.go_basket)
            main_form.basket.place(x=510, y=7)
            main_form.text_lb = tk.Label(self.up_total_order, text='주문내역', font=('', 20), bg='white')
            main_form.text_lb.place(x=20, y=20)
            main_form.testbut_a = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='배달/포장', bd=0,
                                            font=('', 15))
            main_form.testbut_a.place(x=0, y=50)
            main_form.testbut_b = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='B마트', bd=0,
                                            font=('', 15))
            main_form.testbut_b.place(x=170, y=50)
            main_form.testbut_c = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='배민스토어', bd=0,
                                            font=('', 15))
            main_form.testbut_c.place(x=340, y=50)
            main_form.testbut_d = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='대용량특가', bd=0,
                                            font=('', 15))
            main_form.testbut_d.place(x=510, y=50)
            main_form.testbut_e = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='전국별미', bd=0,
                                            font=('', 15))
            main_form.testbut_e.place(x=680, y=50)
        else:
            self.total_order.pack(expand=True, fill='both')

        order_down_Frame = tk.Frame(self.total_order, bg='#f6f6f6', width=550, height=300)
        order_frame_list = []
        self.menu_img_list = []
        splitData = data.split("#")
        order_list = []
        for i in range(len(splitData)):
            order_list.append(splitData[i].split("||"))
        y = 0
        print(order_list[0][5])
        font_instance1 = font.Font(family="Arial Black", size=12, weight='bold')
        for i in range(len(order_list) - 1):
            order_list_Frame = tk.Frame(order_down_Frame, bg='white', width=550, height=190)
            order_frame_list.append(order_list_Frame)

            order_list_img = tk.Canvas(order_list_Frame, width=80, height=80, bg='white')
            store_img = order_list[i][4]
            tmpImg = store_img[2:-1]
            tmpImg = tmpImg.encode()
            decoded_image_data = base64.b64decode(tmpImg)
            image = Image.open(io.BytesIO(decoded_image_data))
            image = image.resize((80, 80))
            tk_image = ImageTk.PhotoImage(image)
            order_list_img.create_image(0, 0, anchor=tk.NW, image=tk_image)
            self.menu_img_list.append(tk_image)
            order_store_name_la = tk.Label(order_list_Frame, text=order_list[i][1], bg='white', font=font_instance1)
            order_store_name_la.place(x=130, y=50)
            order_menu_name_la = tk.Label(order_list_Frame, text=order_list[i][2] + " " + order_list[i][3], bg='white')
            order_menu_name_la.place(x=130  , y=90)

            order_date_la = tk.Label(order_list_Frame, text=order_list[i][5] + " " + order_list[i][6], bg='white')
            if order_list[i][6] == "배달완료":
                order_date_la.configure(fg='gray')
                order_list_review_btn = tk.Button(order_list_Frame, width=500, height=50, image=review_btn_img,
                                               command=lambda : self.create_review_write_form(order_list[i][1],order_list[i][2]),
                                               bd=0, bg='white')
                order_list_review_btn.place(x=30, y=135)
            elif order_list[i][6] == "취소주문":
                order_date_la.configure(fg='red')
                order_list_Frame.configure(height=130)
            elif "30분" in order_list[i][6] or "40분" in order_list[i][6]:
                order_date_la.configure(fg='blue')
                order_list_Frame.configure(height=130)


            order_list_Frame.place(x=0, y=y)
            order_list_img.place(x=30, y=40)

            order_date_la.place(x=30, y=10)
            y += 200

        order_down_Frame.configure(height=y)
        self.total_order.create_window((0, 100), window=order_down_Frame, anchor='nw')

        self.total_order.update_idletasks()

        self.total_order.config(scrollregion=self.total_order.bbox("all"))
        self.total_order.bind("<Configure>", self.on_order_canvas_configure)
        self.total_order.bind_all("<MouseWheel>", self.on_order_mousewheel)
    ##-----------------------------------------------------------------------------
        #     self.scrollbar_order = tk.Scrollbar(main_form, orient="vertical")
        #     self.total_order = tk.Canvas(main_form, yscrollcommand=self.scrollbar_order.set, bg='#f6f6f6', width=550)
        #     self.total_order.pack(expand=True, fill='both')
        #     self.up_total_order = tk.Frame(self.total_order, bg='white', width=550, height=100)
        #     self.total_order.create_window((0, 0), window=self.up_total_order, anchor='nw')
        #
        #     main_form.right = tk.Button(self.up_total_order, bg='white', bd=0, image=del_right_img, width=20, height=20,
        #                                 command=self.total_right)
        #     main_form.right.place(x=400, y=20)
        #     main_form.left = tk.Button(self.up_total_order, bg='white', bd=0, image=del_left_img,
        #                                command=self.total_left, width=20, height=20)
        #     main_form.left.place(x=150, y=20)
        #     main_form.home = tk.Button(self.up_total_order, bg='white', bd=0, image=del_home_img, width=40, height=40,
        #                                command=self.main_form)
        #     main_form.home.place(x=460, y=10)
        #     main_form.basket = tk.Button(self.up_total_order, image=del_basket_img, bg='white', width=40, height=40,
        #                                  bd=0,
        #                                  command=self.go_basket)
        #     main_form.basket.place(x=510, y=7)
        #     main_form.text_lb = tk.Label(self.up_total_order, text='주문내역', font=('', 20), bg='white')
        #     main_form.text_lb.place(x=20, y=20)
        #     main_form.testbut_a = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='배달/포장', bd=0,
        #                                     font=('', 15))
        #     main_form.testbut_a.place(x=0, y=50)
        #     main_form.testbut_b = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='B마트', bd=0,
        #                                     font=('', 15))
        #     main_form.testbut_b.place(x=170, y=50)
        #     main_form.testbut_c = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='배민스토어', bd=0,
        #                                     font=('', 15))
        #     main_form.testbut_c.place(x=340, y=50)
        #     main_form.testbut_d = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='대용량특가', bd=0,
        #                                     font=('', 15))
        #     main_form.testbut_d.place(x=510, y=50)
        #     main_form.testbut_e = tk.Button(self.up_total_order, bg='white', width=15, height=2, text='전국별미', bd=0,
        #                                     font=('', 15))
        #     main_form.testbut_e.place(x=680, y=50)
        # else:
        #     pass
        #
        # order_down_Frame = tk.Frame(self.total_order, bg='#f6f6f6', width=550, height=300)
        # order_frame_list = []
        # self.menu_img_list = []
        # splitData = data.split("#")
        # order_list = []
        # for i in range(len(splitData)):
        #     order_list.append(splitData[i].split("||"))
        # y = 0
        # print(order_list[0][5])
        # font_instance1 = font.Font(family="Arial Black", size=12,weight='bold')
        # for i in range(len(order_list)-1):
        #     print(y)
        #     order_list_Frame = tk.Frame(order_down_Frame, bg='white', width=550, height=130)
        #     order_frame_list.append(order_list_Frame)
        #     order_list_img = tk.Canvas(order_list_Frame, width=80, height=80, bg='white')
        #     store_img = order_list[i][4]
        #     tmpImg = store_img[2:-1]
        #     tmpImg = tmpImg.encode()
        #     decoded_image_data = base64.b64decode(tmpImg)
        #     image = Image.open(io.BytesIO(decoded_image_data))
        #     image = image.resize((80, 80))
        #     tk_image = ImageTk.PhotoImage(image)
        #     order_list_img.create_image(0, 0, anchor=tk.NW, image=tk_image)
        #     self.menu_img_list.append(tk_image)
        #     order_store_name_la = tk.Label(order_list_Frame, text=order_list[i][1], bg='white', font=font_instance1)
        #     order_store_name_la.place(x=130, y=50)
        #     order_menu_name_la = tk.Label(order_list_Frame, text=order_list[i][2] +" "+order_list[i][3], bg='white')
        #     order_menu_name_la.place(x=130, y=90)
        #     review_form_btn = tk.Button(order_list_Frame, image=review_btn_img, width=500, bd=0,highlightthickness=0, command=lambda : self.create_review_write_form(order_list[i][1],order_list[i][2]))
        #
        #     order_date_la = tk.Label(order_list_Frame, text=order_list[i][5]+" "+order_list[i][6], bg='white')
        #     order_list_Frame.place(x=0, y=y)
        #     order_list_img.place(x=30, y=40)
        #     order_date_la.place(x=30, y=10)
        #     if order_list[i][6] == "배달완료":
        #         order_date_la.configure(fg='gray')
        #         review_form_btn.place(x=30, y=130)
        #         order_list_Frame.configure(height=190)
        #         y += 200
        #     elif order_list[i][6] == "취소주문":
        #         order_date_la.configure(fg='red')
        #         y += 140
        #     elif "30분" in order_list[i][6] or "40분" in order_list[i][6]:
        #         order_date_la.configure(fg='blue')
        #         y += 140
        #
        # order_down_Frame.configure(height=y)
        # self.total_order.create_window((0, 100), window=order_down_Frame, anchor='nw')
        #
        # self.total_order.update_idletasks()
        #
        # self.total_order.config(scrollregion=self.total_order.bbox("all"))
        # self.total_order.bind("<Configure>", self.on_order_canvas_configure)
        # self.total_order.bind_all("<MouseWheel>", self.on_order_mousewheel)


##-----------------------------------------------------------------------------
        # main_form_label = tk.Frame(self.total_order, bg='white', width=550, height=200)
        # main_form_label_canvas = tk.Label(main_form_label, width=80, height=80, bg='white', bd=0,
        #                                   image=self.tk_image_store[4])  # --------
        #
        # #main_form_label_button =
        # main_form_label_menu_name = tk.Label(main_form_label, width=30, height=5, text=self.name, font=('', 15),
        #                                      bg='white')
        # main_form_label_explain = tk.Label(main_form_label, width=35, height=2,
        #                                    text=self.key + ' ' + str(self.total_price) + '원', bg='white')
        # main_form_label_review_write = tk.Button(main_form_label, width=43, height=2, text='리뷰쓰기', bg='white',
        #                                          command=self.go_review_write, fg=login_color, bd=1, font=('', 15),
        #                                          highlightbackground=login_color)
        # #main_form_label_button.place(x=500, y=10)
        # main_form_label_canvas.place(x=30, y=30)
        # main_form_label_menu_name.place(x=110, y=5)
        # main_form_label_explain.place(x=150, y=90)
        # main_form_label_review_write.place(x=30, y=130)
        # self.basket_text.place(x=150, y=450)
        # self.basket_image.place(x=175, y=200)
        # self.button_more.place(x=180, y=500)
        # self.labels_list.insert(0, main_form_label)  # 새로운 위젯을 리스트의 처음에 추가
        # self.update_widget_positions()  # 위젯 위치 업데이트


    def on_order_canvas_configure(self, event):
        self.total_order.config(scrollregion=self.total_order.bbox("all"))

    def on_order_mousewheel(self, event):
        self.total_order.yview_scroll(-1 * (event.delta // 120), "units")

    def order_delete(self,label):
        label.destroy()  # 레이블을 삭제합니다.
        self.labels_list.remove(label)  # 리스트에서도 제거합니다.
        self.update_widget_positions()
    def update_widget_positions(self):
        for idx, label in enumerate(self.labels_list):
            label.place(x=0, y=idx * 210)

    def total_right(self):
        buttons = [main_form.testbut_a, main_form.testbut_b, main_form.testbut_c, main_form.testbut_d,
                   main_form.testbut_e]
        for button in buttons:
            current_x = button.winfo_x()
            if current_x > 340 and button != main_form.testbut_e:
                return
        for button in buttons:
            current_x = button.winfo_x()
            new_x = current_x + 170
            button.place(x=new_x, y=50)

    def open_repair_form(self):
        self.up_info_frame.place_forget()
        self.info_frame.place_forget()
        self.down_info_frame.place_forget()
        self.sock.send(("내정보 수정하기").encode())
        self.repair_form_frame = tk.Frame(main_form, width=550, height=550, bg='white')
        self.up_repair_form_frame = tk.Frame(main_form, width=550, height=150, bg='white')
        self.down_repair_form_frame = tk.Frame(main_form, width=550, height=150, bg='white')
        self.repair_form_frame.place(x=0, y=150)
        self.up_repair_form_frame.place(x=0, y=0)
        self.down_repair_form_frame.place(x=0, y=700)
        main_form.repair_msg = tk.Label(self.up_repair_form_frame, text='수정하기', font=('', 50), bg='white')
        main_form.repair_msg.place(x=140, y=30)
        main_form.addr_entry = tk.Entry(self.repair_form_frame, font=('', 25), bg='white')
        main_form.addr_entry.place(x=200, y=400, width=200, height=30)
        main_form.addr_label = tk.Label(self.repair_form_frame, font=('', 10), bg='white', text='주소')
        main_form.addr_label.place(x=20, y=400)
        main_form.phonenum_entry = tk.Entry(self.repair_form_frame, font=('', 25), bg='white')
        main_form.phonenum_entry.place(x=200, y=200, width=200, height=30)
        main_form.phonenum_label = tk.Label(self.repair_form_frame, font=('', 10), bg='white', text='전화번호')
        main_form.phonenum_label.place(x=20, y=200)
        main_form.repair_btn = tk.Button(self.down_repair_form_frame, font=('', 25), text='수정하기',
                                         command=self.repair_info)
        main_form.repair_btn.place(x=50, y=50)
        main_form.cancel_btn = tk.Button(self.down_repair_form_frame, font=('', 25), text='취소하기', command=self.my_info)
        main_form.cancel_btn.place(x=300, y=50)

    def repair_info(self):
        # self.sock.send(('#? '+self.user_id).encode()) #<- (self.~~) 이거는 보낼 정보
        addr = main_form.addr_entry.get()
        phonenum = main_form.phonenum_entry.get()
        print(self.a)
        if (addr or phonenum) and (addr.isalpha() or phonenum.isdigit()):
            # self.sock.send(('#?? '+addr+phonenum).encode())
            tk.messagebox.showinfo('.', '수정되었습니다')
            print(addr, phonenum)
            self.up_repair_form_frame.place_forget()
            self.down_repair_form_frame.place_forget()
            self.repair_form_frame.place_forget()
            self.sock.send(("#10 "+self.a[0]+"||"+addr+"||"+phonenum).encode())
        else:
            tk.messagebox.showinfo('', '잘못작성했거나 작성하지 않았음')
    def total_left(self):
        buttons = [main_form.testbut_a, main_form.testbut_b, main_form.testbut_c, main_form.testbut_d,
                   main_form.testbut_e]
        for button in buttons:
            current_x = button.winfo_x()
            if current_x < 0 and button != main_form.testbut_a:
                return
        for button in buttons:
            current_x = button.winfo_x()
            new_x = current_x - 170
            button.place(x=new_x, y=50)
    def my_info(self):
        self.sock.send(('#5 ' + self.user_id).encode())
        self.up_info_frame = tk.Frame(main_form, bg='white', width=550, height=100)
        self.up_info_frame.place(x=0, y=0)
        self.info_frame = tk.Frame(main_form, bg='white', width=550, height=625)
        self.info_frame.place(x=0, y=100)
        self.down_info_frame = tk.Frame(main_form, bg='gray', width=550, height=125)
        self.down_info_frame.place(x=0, y=725)
        main_form.home = tk.Button(self.up_info_frame, bg='white', bd=0, image=del_home_img, width=50, height=50,
                                   command=self.main_form)
        main_form.home.place(x=470, y=10)
        main_form.back = tk.Button(self.down_info_frame, text='로그아웃', width=20, height=5, font=('', 10),
                                   foreground=login_color, command=self.close_main_form)
        main_form.back.place(x=350, y=30)
        main_form.repair = tk.Button(self.down_info_frame, text='수정하기', width=20, height=5, font=('', 10),
                                     foreground=login_color, command=self.open_repair_form)
        main_form.repair.place(x=40, y=30)
        main_form.name_label = tk.Label(self.info_frame, text=self.a[0], font=('', 10), width=50, height=3)
        main_form.name_label.place(x=120, y=20)
        main_form.name_text_label = tk.Label(self.info_frame, text='이름', font=('', 13), width=10, height=3, bg='white')
        main_form.name_text_label.place(x=3, y=10)
        main_form.birth_label = tk.Label(self.info_frame, text=self.a[1], font=('', 10), width=50, height=3)
        main_form.birth_label.place(x=120, y=320)
        main_form.birth_text_label = tk.Label(self.info_frame, text='생년월일', font=('', 15), width=10, height=3,
                                              bg='white')
        main_form.birth_text_label.place(x=3, y=310)
        main_form.phone_label = tk.Label(self.info_frame, text=self.a[2], font=('', 10), width=50, height=3)
        main_form.phone_label.place(x=120, y=120)
        main_form.phone_text_label = tk.Label(self.info_frame, text='전화번호', font=('', 13), width=10, height=3,
                                              bg='white')
        main_form.phone_text_label.place(x=3, y=110)
        main_form.addr_label = tk.Label(self.info_frame, text=self.a[3], font=('', 10), width=50, height=3)
        main_form.addr_label.place(x=120, y=220)
        main_form.addr_text_label = tk.Label(self.info_frame, text='주소', font=('', 15), width=10, height=3, bg='white')
        main_form.addr_text_label.place(x=3, y=210)
        main_form.rank_label = tk.Label(self.info_frame, text=self.a[4], font=('', 10), width=50, height=3)
        main_form.rank_label.place(x=120, y=420)
        main_form.rank_text_label = tk.Label(self.info_frame, text='등급', font=('', 15), width=10, height=3, bg='white')
        main_form.rank_text_label.place(x=3, y=410)
    def choice_store(self, category,num):
        if num == 0:
            self.sock.send(("#3 "+category).encode())
        else:
            self.sock.send(("#3 " + category).encode())
            self.scrollbar.pack_forget()

    def open_main_form(self):
        self.sock.send(("#1 "+self.ID_entry.get()+self.pw_entry.get()).encode())

    def onEnter(self, event):
        self.open_main_form()

    def close_main_form(self):
        self.user_store_name = ""
        main_form.destroy()
        self.master.deiconify()
    def open_join_form(self):
        global join_form
        join_form = tk.Toplevel(self.master)
        join_form.configure(bg='white')
        canavs_join_bg = tk.Canvas(join_form,width=550,height=200,bd=0, bg="white")
        canavs_join_bg.create_image(275,100,image=add_user_from)
        canavs_join_bg.pack()
        #root.withdraw()
        join_form.title('회원가입')
        join_form.geometry('550x850')
        join_form.name = tk.Label(join_form, image=join_name,bg='white')
        join_form.name.place(x=70,y=205)
        join_form.birth = tk.Label(join_form, image=join_birth,bg='white')
        join_form.birth.place(x=15, y=290)
        join_form.phonenum = tk.Label(join_form, image=join_phone,bg='white')
        join_form.phonenum.place(x=15, y=380)
        join_form.addr = tk.Label(join_form, image=join_addr,bg='white')
        join_form.addr.place(x=70, y=470)
        join_form.join_id = tk.Label(join_form, image=join_id,bg='white')
        join_form.join_id.place(x=70, y=560)
        join_form.join_pw = tk.Label(join_form, image=join_pw,bg='white')
        join_form.join_pw.place(x=70, y=650)
        join_form.regist = tk.Button(join_form,text='등록하기',font=('',30),command = self.regist_ok,bg='white',bd=0)
        join_form.regist.place(x=70,y=740)
        join_form.cancel = tk.Button(join_form,text='취소',font=('',40),command=self.cancel,bg='white',bd=0)

        # border_frame = tk.Frame(self.master, bd=2, relief=tk.SUNKEN, bg='red')
        # border_frame.place(x=300, y=210, width=500, height=50)
        # # Entry 위젯을 Frame 위젯에 배치
        # self.idid = tk.Entry(border_frame, font=('', 30))
        # self.idid.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        # border_frame.pack()

        self.name_entry = tk.Entry(join_form,font=('',30))
        self.name_entry.place(x=180, y=215, width=350, height=50)
        self.birth_entry = tk.Entry(join_form, font=('', 30))
        self.birth_entry.place(x=180, y=290, width=350, height=50)
        self.phonenum_entry = tk.Entry(join_form, font=('', 30))
        self.phonenum_entry.place(x=180, y=380, width=350, height=50)
        self.addr_entry = tk.Entry(join_form, font=('', 30))
        self.addr_entry.place(x=180, y=470, width=350, height=50)
        self.user_id_entry = tk.Entry(join_form, font=('', 30))
        self.user_id_entry.place(x=180, y=560, width=350, height=50)
        self.user_pw_entry = tk.Entry(join_form, font=('', 30))
        self.user_pw_entry.place(x=180, y=650, width=350, height=50)

    def regist_ok(self):
        name = self.name_entry.get()
        birth = self.birth_entry.get()
        phonenum = self.phonenum_entry.get()
        addr = self.addr_entry.get()
        ID = self.user_id_entry.get()
        PW = self.user_pw_entry.get()
        s = " "
        if name and birth and phonenum and addr and ID and PW:
            tkinter.messagebox.showinfo("","등록되었습니다")
            self.sock.send(("#2"+s+name+s+birth+s+phonenum+s+addr+s+ID+s+PW).encode())
            join_form.withdraw()
        else:
            tkinter.messagebox.showinfo("에러","입력사항을 전부 입력해주세요.")
    def cancel(self):
        join_form.withdraw()

    def back_menu(self):
        self.select_store_frame.place(x=0,y=0)

    def choice_menu_info_ri(self, frame):
        if frame == 1:
            self.canvas_menu.itemconfigure(self.menu_ch_frame_window, state='normal')
            self.canvas_menu.itemconfigure(self.info_ch_frame_window, state='hidden')
            self.canvas_menu.itemconfigure(self.ri_ch_frame_window, state='hidden')

            self.menu_ch_btn.configure(image=l_img)
            self.info_ch_btn.configure(image=c_bimg)
            self.ri_ch_btn.configure(image=r_bimg)

            self.canvas_menu.config(scrollregion=self.canvas_menu.bbox("all"))
            self.canvas_menu.bind("<Configure>", self.on_canvas_configure)
            self.canvas_menu.bind_all("<MouseWheel>", self.on_mousewheel)

        elif frame == 2:
            self.canvas_menu.itemconfigure(self.menu_ch_frame_window, state='hidden')
            self.canvas_menu.itemconfigure(self.info_ch_frame_window, state='normal')
            self.canvas_menu.itemconfigure(self.ri_ch_frame_window, state='hidden')

            self.menu_ch_btn.configure(image=l_bimg)
            self.info_ch_btn.configure(image=c_img)
            self.ri_ch_btn.configure(image=r_bimg)

            self.canvas_menu.config(scrollregion=self.canvas_menu.bbox("all"))
            self.canvas_menu.bind("<Configure>", self.on_canvas_configure)
            self.canvas_menu.bind_all("<MouseWheel>", self.on_mousewheel)
        elif frame == 3:
            self.canvas_menu.itemconfigure(self.menu_ch_frame_window, state='hidden')
            self.canvas_menu.itemconfigure(self.info_ch_frame_window, state='hidden')
            self.canvas_menu.itemconfigure(self.ri_ch_frame_window, state='normal')

            self.menu_ch_btn.configure(image=l_bimg)
            self.info_ch_btn.configure(image=c_bimg)
            self.ri_ch_btn.configure(image=r_img)

            self.canvas_menu.config(scrollregion=self.canvas_menu.bbox("all"))
            self.canvas_menu.bind("<Configure>", self.on_canvas_configure)
            self.canvas_menu.bind_all("<MouseWheel>", self.on_mousewheel)



    def set_menu(self, info_data):
        info_f_snans = font.Font(family="Microsoft Sans Serif", size=11)
        self.canvas_select_store.pack_forget()

        data_info_menu = info_data.split("###")

        splitData = data_info_menu[0].split("||")
        splitData2 = data_info_menu[2].split("||")
        splitData3 = data_info_menu[3].split("##")
        print(splitData)

        #if splitData



        self.home_img = PhotoImage(file='del_home.png')
        self.cart_img = PhotoImage(file='del_basket.png')
        self.back_img = PhotoImage(file='back.png')

        self.scrollbar = tk.Scrollbar(main_form, orient="vertical")
        #self.scrollbar.pack(side="right", fill="y")

        self.canvas_menu = tk.Canvas(main_form, yscrollcommand=self.scrollbar.set, bg='white', width=550)
        self.canvas_menu.pack(expand=True, fill='both')
        self.scrollbar.config(command=self.canvas_menu.yview)

        self.menu_frame1 = tk.Frame(self.canvas_menu, bg='white', width=550, height=40)

        font_instance1 = font.Font(family="Arial Black", size=11,weight='bold')
        store_name = tk.Label(self.menu_frame1, text=splitData[0], bg='white',font=font_instance1)
        store_name.place(x=40, y=7)
        cart_btn = tk.Button(self.menu_frame1, image=self.cart_img, bd=0, highlightthickness=0, command=self.go_basket)
        cart_btn.place(x=495, y=2)
        home_btn = tk.Button(self.menu_frame1, image=self.home_img, bd=0, highlightthickness=0, command=self.back_click)
        home_btn.place(x=463, y=8)
        back_btn = tk.Button(self.menu_frame1, image=self.back_img, bd=0, highlightthickness=0, command=lambda: self.choice_store(splitData[1],1))
        back_btn.place(x=0, y=0)

        self.menu_frame2_img_list=[]
        self.menu_frame2 = tk.Canvas(self.canvas_menu, bg='white', width=550, height=300)
        menu_frame2_img = splitData[20]

        tmpImg = menu_frame2_img[2:-2]
        tmpImg = tmpImg.encode()
        decoded_image_data = base64.b64decode(tmpImg)
        image = Image.open(io.BytesIO(decoded_image_data))
        image = image.resize((550, 300))
        tk_image = ImageTk.PhotoImage(image)
        self.menu_frame2.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.menu_frame2_img_list.append(tk_image)

        self.menu_frame3 = tk.Frame(self.canvas_menu, bg='white', width=550, height=450)
        font_instance2 = font.Font(family="Arial Black", size=18, weight='bold')
        store_title = tk.Label(self.menu_frame3, text=splitData[0], font=font_instance2, bg='white')
        store_title.place(relx=0.5, rely=0.05, anchor='center')
        store_rating_img = tk.Label(self.menu_frame3, bg="white", image=rating_5_img)
        store_rating_img.place(relx=0.45, rely=0.17, anchor='center')

        font_instance_rating = font.Font(size=15, weight='bold')
        store_rating_la = tk.Label(self.menu_frame3, bg="white", text=splitData[16], font=font_instance_rating)
        store_rating_la.place(relx=0.67, rely=0.17, anchor='center')

        font_instance_lala = font.Font(size=13)
        store_lala = tk.Label(self.menu_frame3, bg="white", text="최근리뷰 92 ㅣ 최근사장님댓글 109", font=font_instance_lala,fg='gray')
        store_lala.place(relx=0.5, rely=0.27, anchor='center')

        store_lala = tk.Label(self.menu_frame3, bg="white", image=co_img)
        store_lala.place(relx=0.5, rely=0.44, anchor='center')

        self.store_del_btn = (tk.Button(self.menu_frame3, width=275, height=50, image=del_order_btn_img, command=lambda: self.store_del_or_po(1),bd=0,highlightthickness=0))
        self.store_del_btn.place(x=0, y=240)
        self.store_po_btn = (tk.Button(self.menu_frame3, width=275, height=50, image=po_order_noc_btn_img,command=lambda: self.store_del_or_po(2),bd=0,highlightthickness=0))
        self.store_po_btn.place(x=275, y=240)
        self.store_po_frame = tk.Frame(self.menu_frame3, width=550, height=140, bg='white')
        self.store_po_frame.place(x=0,y=300)
        self.store_po_frame_la1 = tk.Label(self.store_po_frame, text="최소 주문 금액", bg='white', font=info_f_snans)
        self.store_po_frame_la1.place(x=25, y=15)
        self.store_po_frame_tx1 = tk.Label(self.store_po_frame, text="없음", bg='white', font=info_f_snans)
        self.store_po_frame_tx1.place(x=145, y=15)
        self.store_po_frame_la2 = tk.Label(self.store_po_frame, text="이용방법", bg='white', font=info_f_snans)
        self.store_po_frame_la2.place(x=25, y=45)
        self.store_po_frame_tx2 = tk.Label(self.store_po_frame, text="포장", bg='white', font=info_f_snans)
        self.store_po_frame_tx2.place(x=145, y=45)
        self.store_po_frame_la3 = tk.Label(self.store_po_frame, text="픽업시간", bg='white', font=info_f_snans)
        self.store_po_frame_la3.place(x=25, y=75)
        self.store_po_frame_tx3 = tk.Label(self.store_po_frame, text="5~25분", bg='white', font=info_f_snans)
        self.store_po_frame_tx3.place(x=145, y=75)
        self.store_po_frame_la4 = tk.Label(self.store_po_frame, text="위치안내", bg='white', font=info_f_snans)
        self.store_po_frame_la4.place(x=25, y=105)
        self.store_po_frame_tx4 = tk.Label(self.store_po_frame, text=splitData[14], bg='white', font=info_f_snans)
        self.store_po_frame_tx4.place(x=145, y=105)
        self.store_del_frame = tk.Frame(self.menu_frame3, width=550, height=140, bg='white')
        self.store_del_frame.place(x=0, y=300)

        self.store_del_frame_la1 = tk.Label(self.store_del_frame, text="최소 주문 금액", bg='white',font=info_f_snans)
        self.store_del_frame_la1.place(x=25, y=15)
        self.store_del_frame_la2 = tk.Label(self.store_del_frame, text="결제방법", bg='white',font=info_f_snans)
        self.store_del_frame_la2.place(x=25, y=45)
        self.store_del_frame_la3 = tk.Label(self.store_del_frame, text="배달시간", bg='white',font=info_f_snans)
        self.store_del_frame_la3.place(x=25, y=75)
        self.store_del_frame_la4 = tk.Label(self.store_del_frame, text="배달팁", bg='white',font=info_f_snans)
        self.store_del_frame_la4.place(x=25, y=105)


        self.delivery_time = splitData[17]
        self.delivety_tip = splitData[18]
        self.name = splitData[0]

        self.minOder = splitData[3]
        self.store_del_frame_tx1 = tk.Label(self.store_del_frame, text=splitData[3], bg='white',font=info_f_snans)
        self.store_del_frame_tx1.place(x=145, y=15)
        self.store_del_frame_tx2 = tk.Label(self.store_del_frame, text="바로결제, 만나서결제", bg='white',font=info_f_snans)
        self.store_del_frame_tx2.place(x=145, y=45)
        self.store_del_frame_tx3 = tk.Label(self.store_del_frame, text=splitData[17], bg='white',font=info_f_snans)
        self.store_del_frame_tx3.place(x=145, y=75)
        self.store_del_frame_tx4 = tk.Label(self.store_del_frame, text=splitData[18], bg='white',font=info_f_snans)
        self.store_del_frame_tx4.place(x=145, y=105)

        self.menu_frame4 = tk.Frame(self.canvas_menu, bg='white', width=550, height=70)

        self.menu_ch_btn = tk.Button(self.menu_frame4, image=l_img, command=lambda: self.choice_menu_info_ri(1),width=184,height=70,bd=0,highlightthickness=0)
        self.menu_ch_btn.place(x=0, y=0)
        self.info_ch_btn = tk.Button(self.menu_frame4, image=c_bimg,command=lambda: self.choice_menu_info_ri(2),width=183,height=70,bd=0,highlightthickness=0)
        self.info_ch_btn.place(x=184, y=0)
        self.ri_ch_btn = tk.Button(self.menu_frame4, image=r_bimg,command=lambda: self.choice_menu_info_ri(3),width=183,height=70,bd=0,highlightthickness=0)
        self.ri_ch_btn.place(x=367, y=0)


        self.menu_ch_frame = tk.Frame(self.canvas_menu, bg='#F6F6F6', width=550, height=400)
        #menu frame1

        splitMenu = data_info_menu[1].split("##")
        menu_list = []
        for i in range(len(splitMenu)):
            menu_list.append(splitMenu[i].split("||"))

        menu_frame_list = []
        self.menu_img_list=[]

        y = 0
        for i in range(len(menu_list)):
            menu_frame = tk.Frame(self.menu_ch_frame, width=550, height=120, borderwidth=1, bg='white')
            menu_frame.place(x=2, y=y)
            menu_frame_list.append(menu_frame)

            menu_name = menu_list[i][2]
            font_instance_names = font.Font(family="Arial Black", size=11, weight='bold')
            menu_names = tk.Label(menu_frame, text=menu_name, bg='white', font=font_instance_names)
            menu_names.place(x=10, y=10)

            menu_description = menu_list[i][3]
            menu_descriptions = tk.Label(menu_frame, text=menu_description, bg='white', font=("",9), fg='gray')
            menu_descriptions.place(x=10, y=45)

            menu_price = menu_list[i][5]
            menu_price1 = tk.Label(menu_frame, text=menu_price, bg='white', font=font_instance_names)
            menu_price1.place(x=10, y=75)

            menu_img_can = tk.Canvas(menu_frame, width=100, height=100, bg='white')
            menu_img_can.place(x=420, y=10)

            menu_img = menu_list[i][1]
            if menu_list[i][1] != "None":
                tmpImg = menu_img[2:-1]
                tmpImg = tmpImg.encode()
                decoded_image_data = base64.b64decode(tmpImg)
                image = Image.open(io.BytesIO(decoded_image_data))
                image = image.resize((100, 100))
                tk_image = ImageTk.PhotoImage(image)
                menu_img_can.create_image(0, 0, anchor=tk.NW, image=tk_image)
                self.menu_img_list.append(tk_image)

                self.tk_image = ImageTk.PhotoImage(image)
                self.tk_image_menu.insert(0, self.tk_image)
                menu_img_can.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
                self.menu_img_list.append(self.tk_image)



            menu_frame_list[i].bind('<Button-1>', lambda event, arg1=f'{menu_name}', arg2=f'{splitData[0]}': self.click_menu(arg1, arg2))

            y += 130

        self.menu_ch_frame.configure(height=y)


        #----------------------info frame1
        self.info_ch_frame = tk.Frame(self.canvas_menu, bg='#F6F6F6', width=550, height=1500)
        info_ch_frame_heignt = 0
        info_f_cate_font = font.Font(family="Arial Black", size=15, weight='bold')

        info_frame1 = tk.Frame(self.info_ch_frame, bg='white', width=550, height=210)
        info_frame1.place(x=0, y=0)

        info_f1_storename = tk.Label(info_frame1, text=splitData[0],bg='white', font=info_f_cate_font)
        info_f1_storename.place(x=15, y=15)


        info_f1_business_name_la = tk.Label(info_frame1, text="상호명", bg='white', font=info_f_snans)
        info_f1_operating_time_la = tk.Label(info_frame1, text="운영시간", bg='white', font=info_f_snans)
        info_f1_closed_day_la = tk.Label(info_frame1, text="휴무일", bg='white', font=info_f_snans)
        info_f1_phone_la = tk.Label(info_frame1, text="전화번호", bg='white',font=info_f_snans)
        info_f1_delivery_area_la = tk.Label(info_frame1, text="배달지역", bg='white',font=info_f_snans)

        info_f1_business_name_la.place(x=15, y=60)
        info_f1_operating_time_la.place(x=15, y=90)
        info_f1_closed_day_la.place(x=15, y=120)
        info_f1_phone_la.place(x=15, y=150)
        info_f1_delivery_area_la.place(x=15, y=180)

        info_f_business_name = tk.Label(info_frame1, text=splitData[0], bg='white', font=info_f_snans).place(x=125,y=60)
        info_f_operating_time= tk.Label(info_frame1, text=splitData[4], bg='white', font=info_f_snans).place(x=125,y=90)
        info_f_closed_day= tk.Label(info_frame1, text=splitData[5], bg='white', font=info_f_snans).place(x=125,y=120)
        info_f_phone= tk.Label(info_frame1, text=splitData[6], bg='white', font=info_f_snans).place(x=125,y=150)
        info_f_delivery_area= tk.Label(info_frame1, text=splitData[7], bg='white', font=info_f_snans).place(x=125,y=180)
        info_ch_frame_heignt += 220
        #----------------------info frame2
        info_frame2 = tk.Frame(self.info_ch_frame, bg='white', width=550, height=200)
        info_frame2.place(x=0, y=info_ch_frame_heignt)

        info_f2_store_introduction_label = tk.Label(info_frame2, text="가게 소개", bg='white', font=info_f_cate_font)
        info_f2_store_introduction_label.place(x=15, y=15)

        info_f2_store_introduction_text = tk.Label(info_frame2, text=splitData[8], bg='white', font=info_f_snans,wraplength=500)
        info_f2_store_introduction_text.place(x=15, y=60)

        info_f2_height = info_f2_store_introduction_text.winfo_reqheight()
        info_frame2.configure(height=info_f2_height + 80)
        info_ch_frame_heignt += 90 + info_f2_height
        # ----------------------info frame3
        info_frame3 = tk.Frame(self.info_ch_frame, bg='white', width=550)
        info_frame3.place(x=0, y= info_ch_frame_heignt)

        info_f3_store_introduction_label = tk.Label(info_frame3, text="안내 및 혜택", bg='white', font=info_f_cate_font)
        info_f3_store_introduction_label.place(x=15, y=15)

        info_f3_store_introduction_text = tk.Label(info_frame3, text=splitData[9], bg='white', font=info_f_snans, wraplength=500)
        info_f3_store_introduction_text.place(x=15, y=60)

        info_f3_height = info_f3_store_introduction_text.winfo_reqheight()
        info_frame3.configure(height=info_f3_height + 80)
        info_ch_frame_heignt += info_f3_height + 90

        # ----------------------info frame4
        info_frame4 = tk.Frame(self.info_ch_frame, bg='white', width=550, height=100)
        info_frame4.place(x=0, y=info_ch_frame_heignt)

        info_f4_store_introduction_label = tk.Label(info_frame4, text="가게 인증내역", bg='white', font=info_f_cate_font)
        info_f4_store_introduction_label.place(x=15, y=15)
        info_f4_store_certification_details_la = tk.Label(info_frame4, text="CESCO", bg='white', font=info_f_snans).place(x=15, y=60)
        info_f4_store_certification_details = tk.Label(info_frame4, text=splitData[10], bg='white', font=info_f_snans).place(x=125, y=60)
        info_ch_frame_heignt += 110

        # ----------------------info frame5
        info_frame5 = tk.Frame(self.info_ch_frame, bg='white', width=550, height=150)
        info_frame5.place(x=0, y=info_ch_frame_heignt)
        household_statistics = splitData[15].split(',')

        info_f5_household_statistics_label = tk.Label(info_frame5, text="가게 통계", bg='white', font=info_f_cate_font)
        info_f5_household_statistics_label.place(x=15, y=15)
        info_f5_household_statistics_la1 = tk.Label(info_frame5, text="최근 주문수", bg='white',font=info_f_snans).place(x=15, y=60)
        info_f5_household_statistics1 = tk.Label(info_frame5,text=household_statistics[0]+"+",  bg='white',font=info_f_snans).place(x=125, y=60)
        info_f5_household_statistics_la2 = tk.Label(info_frame5, text="전체 주문수", bg='white', font=info_f_snans).place(x=15, y=90)
        info_f5_household_statistics2 = tk.Label(info_frame5, text=household_statistics[1] + "+", bg='white',font=info_f_snans).place(x=125, y=90)
        info_f5_household_statistics_la3 = tk.Label(info_frame5, text="찜", bg='white', font=info_f_snans).place(x=15, y=120)
        info_f5_household_statistics3 = tk.Label(info_frame5, text=household_statistics[2], bg='white',font=info_f_snans).place(x=125, y=120)

        info_ch_frame_heignt += 160

        # ----------------------info frame6
        info_frame6 = tk.Frame(self.info_ch_frame, bg='white', width=550, height=270)
        info_frame6.place(x=0, y=info_ch_frame_heignt)
        info_f6_data = splitData[11].split("//")
        if splitData[2] == "임광식" or splitData[2] == "김호준":
            info_f6_delivery_tip_information = tk.Label(info_frame6, text="배달팁 안내", bg='white', font=info_f_cate_font)
            info_f6_delivery_tip_information.place(x=15, y=15)
            info_f6_delivery_tip_information_la1 = tk.Label(info_frame6, text="• "+info_f6_data[0], bg='white', font=info_f_snans).place(x=15, y=60)
            info_f6_delivery_tip_information_la2 = tk.Label(info_frame6, text="• "+info_f6_data[1], bg='white', font=info_f_snans).place(x=15, y=90)

            info_f6_delivery_tips_for_each_order = tk.Label(info_frame6, text="주문금액 별 배달팁", bg='white', font=info_f_cate_font)
            info_f6_delivery_tips_for_each_order.place(x=15, y=140)
            for i in range(3,(len(info_f6_data))):
                pass #여기에 금액표 개수만큼 늘리는거 수정하자 일단 다른거 부터 ㄱㄱ
            #info_f6_delivery_tips_for_each_order_la1 = tk.Label(info_frame6, text="• " + info_f6_data[2], bg='white', font=info_f_snans).place(x=15, y=185)
            #info_f6_delivery_tips_for_each_order_la2 = tk.Label(info_frame6, text="• " + info_f6_data[3], bg='white', font=info_f_snans).place(x=15, y=215)

        info_ch_frame_heignt += 280


        # ----------------------info frame7
        info_frame7 = tk.Frame(self.info_ch_frame, bg='white', width=550, height=200)
        info_frame7.place(x=0, y=info_ch_frame_heignt)
        info_f7_Business_information = tk.Label(info_frame7, text="사업자 정보", bg='white', font=info_f_cate_font)
        info_f7_Business_information.place(x=15, y=15)
        info_f7_Business_information_la1 = tk.Label(info_frame7, text="대표자명", bg='white', font=info_f_snans).place(x=15, y=60)
        info_f7_Business_information_tx1 = tk.Label(info_frame7, text=splitData[2], bg='white',font=info_f_snans).place(x=125, y=60)
        info_f7_Business_information_la2 = tk.Label(info_frame7, text="상호명", bg='white', font=info_f_snans).place(x=15, y=90)
        info_f7_Business_information_tx2 = tk.Label(info_frame7, text=splitData[0], bg='white',font=info_f_snans).place(x=125, y=90)
        info_f7_Business_information_la3 = tk.Label(info_frame7, text="사업자 주소", bg='white', font=info_f_snans).place(x=15,y=120)
        info_f7_Business_information_tx3 = tk.Label(info_frame7, text=splitData[14], bg='white', font=info_f_snans).place(x=125, y=120)
        info_f7_Business_information_la4 = tk.Label(info_frame7, text="사업자등록번호", bg='white', font=info_f_snans).place(x=15,y=150)
        info_f7_Business_information_tx4 = tk.Label(info_frame7, text=splitData[12], bg='white',font=info_f_snans).place(x=125, y=150)

        info_ch_frame_heignt += 210
        self.info_ch_frame.configure(height=info_ch_frame_heignt)

        # ----------------------info frame8
        info_frame8 = tk.Frame(self.info_ch_frame, bg='white', width=550, height=100)
        info_frame8.place(x=0, y=info_ch_frame_heignt)

        info_f8_country_of_origin_notation = tk.Label(info_frame8, text="원산지 표기", bg='white', font=info_f_cate_font)
        info_f8_country_of_origin_notation.place(x=15, y=15)
        info_f8_country_of_origin_notation_tx = tk.Label(info_frame8, text=splitData[13], bg='white',font=info_f_snans).place(x=15, y=60)

        info_ch_frame_heignt += 100
        self.info_ch_frame.configure(height=info_ch_frame_heignt)

        #

        # ----------------------rev framer1
        self.ri_ch_frame = tk.Frame(self.canvas_menu, bg='#F6F6F6', width=550, height=800)

        re_frame_height = 0
        rev_f_cate_font = font.Font(family="Arial Black", size=15, weight='bold')

        rev_frame1 = tk.Frame(self.ri_ch_frame, bg='white', width=550, height=210)
        rev_frame1.place(x=0, y=0)
        rev_f1_title = tk.Label(rev_frame1, text="사장님 공지", bg='white', font=rev_f_cate_font)
        rev_f1_title.place(x=15, y=15)
        rev_frame1_text = tk.Label(rev_frame1, text=splitData2[2], bg='white', font=info_f_snans,
                                                   wraplength=500)
        rev_frame1_text.place(x=15, y=60)

        rev_frame1_height = rev_frame1_text.winfo_reqheight()
        rev_frame1.configure(height=rev_frame1_height + 80)
        re_frame_height += rev_frame1_height + 90


        # ----------------------rev framer2
        rev_frame2 = tk.Frame(self.ri_ch_frame, bg='white', width=550, height=160)
        rev_frame2.place(x=0, y=re_frame_height)
        # rev_f2_title = tk.Label(rev_frame2, text="별점정보", bg='white', font=rev_f_cate_font)
        # rev_f2_title.place(x=15, y=15)


        rev_rating_font = font.Font(size=25, weight='bold')
        rev_frame2_rating_la = tk.Label(rev_frame2, text="", bg='white', font=rev_rating_font)
        rev_frame2_rating_la.place(x=30, y=30)
        rev_frame3_img = tk.Label(rev_frame2, bg='white', image=rating_img55, wraplength=500)
        rev_frame3_img.place(x=20, y=80)

        rev_frame2_rating5_la = tk.Label(rev_frame2, text="5점", bg='white', font=info_f_snans)
        rev_frame2_rating5_la.place(x=200, y=10)
        rev_frame2_rating5_tx = tk.Label(rev_frame2, text="", bg='white', font=info_f_snans)
        rev_frame2_rating5_tx.place(x=230,y=10)
        rev_frame2_rating4_la = tk.Label(rev_frame2, text="4점", bg='white', font=info_f_snans)
        rev_frame2_rating4_la.place(x=200, y=40)
        rev_frame2_rating4_tx = tk.Label(rev_frame2, text="", bg='white', font=info_f_snans)
        rev_frame2_rating4_tx.place(x=230, y=40)
        rev_frame2_rating3_la = tk.Label(rev_frame2, text="3점", bg='white', font=info_f_snans)
        rev_frame2_rating3_la.place(x=200, y=70)
        rev_frame2_rating3_tx = tk.Label(rev_frame2, text="", bg='white', font=info_f_snans)
        rev_frame2_rating3_tx.place(x=230, y=70)
        rev_frame2_rating2_la = tk.Label(rev_frame2, text="2점", bg='white', font=info_f_snans)
        rev_frame2_rating2_la.place(x=200, y=100)
        rev_frame2_rating2_tx = tk.Label(rev_frame2, text="", bg='white', font=info_f_snans)
        rev_frame2_rating2_tx.place(x=230, y=100)
        rev_frame2_rating1_la = tk.Label(rev_frame2, text="1점", bg='white', font=info_f_snans)
        rev_frame2_rating1_la.place(x=200, y=130)
        rev_frame2_rating1_tx = tk.Label(rev_frame2, text="", bg='white', font=info_f_snans)
        rev_frame2_rating1_tx.place(x=230, y=130)

        re_frame_height += 170

        # ----------------------rev framer3
        rev_frame3 = tk.Frame(self.ri_ch_frame, bg='white', width=550, height=210)
        rev_frame3.place(x=0, y=re_frame_height)
        rev_f3_title = tk.Label(rev_frame3, text="사장님 한마디", bg='white', font=rev_f_cate_font)
        rev_f3_title.place(x=15, y=15)
        rev_frame3_text = tk.Label(rev_frame3, text=splitData2[3], bg='white', font=info_f_snans,
                                   wraplength=500)
        rev_frame3_text.place(x=15, y=60)


        rev_frame3_height = rev_frame1_text.winfo_reqheight()
        rev_frame3.configure(height=rev_frame3_height + 80)
        re_frame_height += rev_frame3_height + 90

        #
        print(re_frame_height)
        # ----------------------rev framer4
        rev_frame4 = tk.Frame(self.ri_ch_frame, bg='white', width=550, height=50)
        rev_frame4.place(x=0, y=re_frame_height)
        rev_f4_title = tk.Label(rev_frame4, text="최근 리뷰", bg='white', font=rev_f_cate_font)
        rev_f4_title.place(x=15, y=15)
        re_frame_height += 50
        #-------------------
        rev_frame5 = tk.Frame(self.ri_ch_frame, bg='#f6f6f6', width=550, height=210)
        rev_frame5.place(x=0, y=re_frame_height)
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        cnt5 = 0
        y = 0
        review_list = []
        for i in range(len(splitData3)):
            review_list.append(splitData3[i].split("||"))
        print(review_list)
        for i in range(len(review_list)):
            review_frame = tk.Frame(rev_frame5, width=550, height=400, bg='white')
            review_frame.place(x=0, y=y)
            self.baedali = tk.Label(review_frame, image=baedali_img, bd=0)
            self.baedali.place(x=10, y=15)
            self.name_label = tk.Label(review_frame, text=review_list[i][4], font=('맑은 고딕', 14), bg='white')
            self.name_label.place(x=80, y=15)
            self.grade = tk.Label(review_frame, text='평점:', font=('맑은 고딕', 12), bg='white')
            self.grade.place(x=80, y=50)
            self.grade_num = tk.Label(review_frame, text=review_list[i][0], font=('맑은 고딕', 12), bg='white')
            self.grade_num.place(x=120, y=50)
            self.grade_total_num = tk.Label(review_frame, text='/ 5', font=('맑은 고딕', 12), bg='white')
            self.grade_total_num.place(x=135, y=50)
            self.menuName = tk.Label(review_frame, text=review_list[i][3], font=('맑은 고딕', 12), bg='lightgray')
            self.menuName.place(x=10, y=100)
            self.reviewContent = tk.Label(review_frame, text=review_list[i][2], font=('맑은 고딕', 16),
                                          bg='white')
            self.reviewContent.place(x=10, y=140)
            if review_list[i][0] == '1':
                cnt1 += 1
            elif review_list[i][0] == '2':
                cnt2 += 1
            elif review_list[i][0] == '3':
                cnt3 += 1
            elif review_list[i][0] == '4':
                cnt4 += 1
            elif review_list[i][0] == '5':
                cnt5 += 1

            if review_list[i][5] != " ":
                text_content = review_list[i][5]
                self.review_label = tk.Label(review_frame, text=text_content, font=('맑은 고딕', 10), width=45,
                                             height=7,
                                             bg='#EBDDCC', wraplength=350)
                self.review_label.place(x=110, y=210)
                self.sajang_review = tk.Label(review_frame, image=sajang_img, bd=0)
                self.sajang_review.place(x=10, y=210)
                y += 410
            else:
                review_frame.configure(height=200)
                y += 210


        rating_aver = ((cnt1*1)+(cnt2*2)+(cnt3*3)+(cnt4*4)+(cnt5*5))/(cnt1+cnt2+cnt3+cnt4+cnt5)
        rating_aver=round(rating_aver, 2)
        rev_frame2_rating_la.configure(text=str(rating_aver))
        rev_frame2_rating5_tx.configure(text=str(cnt5))
        rev_frame2_rating4_tx.configure(text=str(cnt4))
        rev_frame2_rating3_tx.configure(text=str(cnt3))
        rev_frame2_rating2_tx.configure(text=str(cnt2))
        rev_frame2_rating1_tx.configure(text=str(cnt1))



        re_frame_height += y
        rev_frame5.configure(height=y)
        self.ri_ch_frame.configure(height=re_frame_height)



        self.canvas_menu.create_window((0, 0), window=self.menu_frame1, anchor='nw')
        self.canvas_menu.create_window((-1, 40), window=self.menu_frame2, anchor='nw')
        self.canvas_menu.create_window((0, 350), window=self.menu_frame3, anchor='nw')
        self.canvas_menu.create_window((0, 810), window=self.menu_frame4, anchor='nw')

        self.info_ch_frame_window = self.canvas_menu.create_window((0, 880), window=self.info_ch_frame, anchor='nw')
        self.ri_ch_frame_window = self.canvas_menu.create_window((0, 880), window=self.ri_ch_frame, anchor='nw')
        self.menu_ch_frame_window = self.canvas_menu.create_window((0, 880), window=self.menu_ch_frame, anchor='nw')
        self.canvas_menu.itemconfigure(self.info_ch_frame_window, state='hidden')
        self.canvas_menu.itemconfigure(self.ri_ch_frame_window, state='hidden')



        self.canvas_menu.update_idletasks()

        self.canvas_menu.config(scrollregion=self.canvas_menu.bbox("all"))
        self.canvas_menu.bind("<Configure>", self.on_canvas_configure)
        self.canvas_menu.bind_all("<MouseWheel>", self.on_mousewheel)  # 마우스 휠 이벤트 바인딩


    def store_del_or_po(self,num):
        if num == 1:
            self.store_po_frame.place_forget()
            self.store_del_frame.place(x=0, y=300)
            self.store_del_btn.configure(image=del_order_btn_img)
            self.store_po_btn.configure(image=po_order_noc_btn_img)
            self.del_order = True
            self.po_order = False
        elif num == 2:
            self.store_del_frame.place_forget()
            self.store_po_frame.place(x=0, y=300)
            self.store_del_btn.configure(image=del_order_noc_btn_img)
            self.store_po_btn.configure(image=po_order_btn_img)
            self.del_order = False
            self.po_order =True

    def on_canvas_configure(self, event):
        self.canvas_menu.config(scrollregion=self.canvas_menu.bbox("all"))

    def on_mousewheel(self, event):
        self.canvas_menu.yview_scroll(-1 * (event.delta // 120), "units")  # 마우스 휠 스크롤 기능 구현

    def go_basket(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.place_forget()
            self.down_main_frame.place_forget()
            self.up_main_frame.place_forget()
        if hasattr(self, 'up_search_frame'):
            self.search_frame.place_forget()
        if hasattr(self, 'search_frame'):
            self.search_frame.place_forget()
        if hasattr(self, 'total_order'):
            self.total_order.pack_forget()
        if hasattr(self, 'menu_frame21'):
            self.menu_click_frame1.pack_forget()
        if hasattr(self, 'select_store_frame'):
            self.select_store_frame.place_forget()
            self.up_select_store_frame.place_forget()
            self.canvas_select_store.pack_forget()
        if hasattr(self, 'up_info_frame'):
            self.up_info_frame.place_forget()
            self.info_frame.place_forget()
            self.down_info_frame.place_forget()
        if hasattr(self, 'repair_form_frame'):
            self.repair_form_frame.place_forget()
            self.up_repair_form_frame.place_forget()
            self.down_repair_form_frame.place_forget()
        if hasattr(self, 'canvas_menu_click'):
            self.canvas_menu_click.pack_forget()
            self.menu_frame2.pack_forget()
            self.canvas_menu.pack_forget()
        if not hasattr(self, 'basket_frame'):
            self.basket_frame = tk.Frame(main_form, bg='white', width=550, height=625)
            self.basket_frame.place(x=0, y=100)
            self.up_basket_frame = tk.Frame(main_form, bg='white', width=550, height=100)
            self.up_basket_frame.place(x=0, y=0)
            self.down_basket_frame = tk.Frame(main_form, bg='white', width=550, height=125)
            self.down_basket_frame.place(x=0, y=725)
            main_form.home = tk.Button(self.up_basket_frame, bg='white', bd=0, image=del_home_img, width=50, height=50,
                                       command=self.main_form)
            main_form.home.place(x=470, y=0)
            main_form_home = tk.Button(self.up_basket_frame, image=del_arrow_img, width=40, height=40, bg='white', bd=0,
                                       command=self.main_form)
            main_form_home.place(x=10, y=0)
            main_form.market_lable = tk.Label(self.up_basket_frame, text='장바구니', bg='white', font=('', 15))
            main_form.market_lable.place(x=230, y=15)
            main_form.order = tk.Button(self.down_basket_frame, bg=login_color, text='주문하기', bd=0, font=('', 20),
                                        foreground='white', width=15, height=3, command=self.plus_order)
            main_form.order.place(x=15, y=10)
            # main_form.cancel = tk.Button(self.down_basket_frame, bg=login_color, text='취소하기', bd=0, font=('', 20),
            #                              foreground='white', width=10, height=3)
            # main_form.cancel.place(x=365, y=10)
            self.basket_text = tk.Label(self.basket_frame, bg='white', text='장바구니가 텅 비었어요.', font=('', 15))
            self.basket_text.place(x=150, y=450)
            self.basket_image = tk.Label(self.basket_frame, bg='white', image=del_baket_cat_img)
            self.basket_image.place(x=175, y=200)
            self.button_more = tk.Button(self.basket_frame, bg='white', image=del_more_put_img, bd=0,
                                         command=self.main_form)
            self.button_more.place(x=180, y=500)
            main_form.right = tk.Button(self.up_basket_frame, bg='white', bd=0, image=del_right_img, width=20, height=20,
                                        command=self.total_right)
            main_form.right.place(x=400, y=20)
            main_form.left = tk.Button(self.up_basket_frame, bg='white', bd=0, image=del_left_img,
                                       command=self.total_left, width=20, height=20)
            main_form.left.place(x=150, y=20)
            main_form.testbut_a = tk.Button(self.up_basket_frame, bg='white', width=15, height=2, text='배달/포장', bd=0,
                                            font=('', 15))
            main_form.testbut_a.place(x=0, y=50)
            main_form.testbut_b = tk.Button(self.up_basket_frame, bg='white', width=15, height=2, text='B마트', bd=0,
                                            font=('', 15))
            main_form.testbut_b.place(x=170, y=50)
            main_form.testbut_c = tk.Button(self.up_basket_frame, bg='white', width=15, height=2, text='배민스토어', bd=0,
                                            font=('', 15))
            main_form.testbut_c.place(x=340, y=50)
            main_form.testbut_d = tk.Button(self.up_basket_frame, bg='white', width=15, height=2, text='대용량특가', bd=0,
                                            font=('', 15))
            main_form.testbut_d.place(x=510, y=50)
            main_form.testbut_e = tk.Button(self.up_basket_frame, bg='white', width=15, height=2, text='전국별미', bd=0,
                                            font=('', 15))
            main_form.testbut_e.place(x=680, y=50)
        else:
            self.basket_frame.place(x=0, y=100)
            self.up_basket_frame.place(x=0, y=0)
            self.down_basket_frame.place(x=0, y=725)

    def back_menu_set(self):
        self.canvas_menu_click.pack_forget()
        self.canvas_menu.pack(expand=True, fill='both')
        self.canvas_menu.config(scrollregion=self.canvas_menu.bbox("all"))
        self.canvas_menu.bind("<Configure>", self.on_canvas_configure)
        self.canvas_menu.bind_all("<MouseWheel>", self.on_mousewheel)

    def create_menu_click_form(self, menu_data):
        print("SSS",menu_data)
        tmp_data = menu_data.split("메뉴정보")
        split_menu_data = tmp_data[0].split("||")

        split_menu_click_data = tmp_data[1].split("#")
        split_menu_click_data_list = []

        for i in range(len(split_menu_click_data)):
            split_menu_click_data_list.append(split_menu_click_data[i].split("||"))
        list_cate = list(set(item[0] for item in split_menu_click_data_list))

        print("asdasdsad",split_menu_click_data_list)
        self.scrollbar1 = tk.Scrollbar(main_form, orient="vertical")
        self.canvas_menu_click = tk.Canvas(main_form, yscrollcommand=self.scrollbar1.set, bg='#F6F6F6', width=550)
        self.canvas_menu_click.pack(expand=True, fill='both')

        # 스크롤바 연결
        self.scrollbar1.config(command=self.canvas_menu_click.yview)

        self.menu_click_frame1 = tk.Frame(self.canvas_menu_click, bg='white', width=550, height=40)
        font_instance1 = font.Font(family="Arial Black", size=11, weight='bold')
        menu_name = tk.Label(self.menu_click_frame1, text=split_menu_data[0], bg='white', font=font_instance1)
        menu_name.place(x=40, y=7)
        cart_btn = tk.Button(self.menu_click_frame1, image=self.cart_img, bd=0, highlightthickness=0,command=self.go_basket)
        cart_btn.place(x=495, y=2)
        home_btn = tk.Button(self.menu_click_frame1, image=self.home_img, bd=0, highlightthickness=0,command=self.main_form)
        home_btn.place(x=463, y=8)
        back_btn = tk.Button(self.menu_click_frame1, image=self.back_img, bd=0, highlightthickness=0,
                             command=self.back_menu_set)
        back_btn.place(x=0, y=0)

        self.menu_click_frame2_img_list = []
        self.menu_click_frame2 = tk.Canvas(self.canvas_menu_click, bg='white', width=550, height=300)
        menu_frame2_img = split_menu_data[1]
        tmpImg = menu_frame2_img[2:-1]
        tmpImg = tmpImg.encode()
        decoded_image_data = base64.b64decode(tmpImg)
        image = Image.open(io.BytesIO(decoded_image_data))
        image = image.resize((550, 550))
        tk_image = ImageTk.PhotoImage(image)
        self.menu_click_frame2.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.menu_click_frame2_img_list.append(tk_image)

        self.menu_click_frame3 = tk.Frame(self.canvas_menu_click, bg='white', width=550, height=150)
        font_instance2 = font.Font(family="Arial Black", size=13, weight='bold')
        menu_name = tk.Label(self.menu_click_frame3, text=split_menu_data[0], bg='white', font=font_instance2)
        menu_name.place(x=10, y=10)
        menu_description = tk.Label(self.menu_click_frame3, text=split_menu_data[2], bg='white', font=('',10), fg='gray')
        menu_description.place(x=10, y=50)
        menu_price_la = tk.Label(self.menu_click_frame3, text="가격", bg='white', font=font_instance2)
        menu_price_la.place(x=10, y=110)
        menu_price_tx = tk.Label(self.menu_click_frame3, text=split_menu_data[3]+"원", bg='white', font=font_instance2)
        menu_price_tx.place(x=450, y=110)
        self.menu_click_frame4 = tk.Frame(self.canvas_menu_click, bg='#F6F6F6', width=550, height=550)
        menu_f_list = []
        self.store_main_images = []

        y = 0

        self.variable_dict = {}


        for i in range(len(list_cate)):
            self.menu_cate_frame = tk.Frame(self.menu_click_frame4, width=550, height=50, borderwidth=1, bg='white')
            self.menu_cate_frame.place(x=0, y=y)
            self.cate_name = tk.Label(self.menu_cate_frame, text=list_cate[i], bg='white', font=font_instance2)
            self.cate_name.place(x=10, y=5)
            self.variable_dict[list_cate[i]] = tk.StringVar()
            y += 50
            for j in range(len(split_menu_click_data_list)):
                if list_cate[i] == split_menu_click_data_list[j][0]:
                    self.menu_frame21 = tk.Frame(self.menu_click_frame4, width=550, height=40, borderwidth=1,
                                                 bg='white')
                    self.menu_frame21.place(x=0, y=y)
                    menu_f_list.append(self.menu_frame21)  # iiiiiiiiiiiiiiiiii
                    self.radio_test = tk.Radiobutton(self.menu_frame21, bg='white',
                                                     value=split_menu_click_data_list[j][1] + "||" +
                                                           split_menu_click_data_list[j][2],
                                                     variable=self.variable_dict[list_cate[i]],
                                                     command=self.radiobutton_click)
                    self.radio_test.place(x=10, y=7)
                    menu_la1 = tk.Label(self.menu_frame21, text=split_menu_click_data_list[j][1], bg='white',
                                        font=('', 10))
                    menu_la1.place(x=40, y=8)
                    menu_la2 = tk.Label(self.menu_frame21, text="+" + split_menu_click_data_list[j][2] + "원",
                                        bg='white',
                                        font=('', 10))
                    menu_la2.place(x=480, y=8)
                    y += 40
                    self.radio_test.select()

            y += 10

        self.menu_click_frame4.configure(height=y)

        self.menu_click_frame6 = tk.Frame(self.canvas_menu_click, bg='white', width=550, height=60)

        self.canvas_menu_click.create_window((0, 0), window=self.menu_click_frame1, anchor='nw')
        self.canvas_menu_click.create_window((-1, 40), window=self.menu_click_frame2, anchor='nw')
        self.canvas_menu_click.create_window((0, 340), window=self.menu_click_frame3, anchor='nw')
        self.canvas_menu_click.create_window((0, 500), window=self.menu_click_frame4, anchor='nw')
        self.canvas_menu_click.create_window((0, 500+y+10), window=self.menu_click_frame6, anchor='nw')

        self.canvas_menu_click.config(scrollregion=self.canvas_menu_click.bbox("all"))
        self.canvas_menu_click.bind("<Configure>", self.on_canvas_configure4)
        self.canvas_menu_click.bind_all("<MouseWheel>", self.on_mousewheel4)

        self.amount = split_menu_data[3]

        self.menu_click_frame5 = tk.Canvas(self.canvas_menu_click, bg='white', width=550, height=80, highlightthickness=0)
        self.menu_click_frame5.pack(side="bottom")
        self.menu_click_frame5.create_line(0, 0, 550, 0, fill="black", width=2)
        self.menu_click_frame5_la1 = tk.Label(self.menu_click_frame5, text="배달최소주문금액", fg='grey',bg='white',font=("",11))
        self.menu_click_frame5_la1.place(x=10, y=13)
        self.menu_click_frame5_la2 = tk.Label(self.menu_click_frame5, text=self.minOder ,bg='white',font=("",11))
        self.menu_click_frame5_la2.place(x=10,y=40)
        self.menu_click_frame5_btn = tk.Button(self.menu_click_frame5, text=self.amount+"원 담기", bg='#2AC1BC', width=32, height=2, fg="white", font=("Arial Black", 13),
                                               bd=0, highlightthickness=0, command=lambda: self.basket_in_menu(split_menu_data[0]))

        self.menu_click_frame5_btn.place(x=150, y=10)
    def radiobutton_click(self):
        self.selected_values = {}
        for category, var in self.variable_dict.items():
            selected_value = var.get()
            menu_name, price = selected_value.split("||")
            self.selected_values[category] = (menu_name, price)
        prices = [int(value[1]) for value in self.selected_values.values()]
        self.total_price = sum(prices)+int(self.amount)

        self.menu_click_frame5_btn.configure(text= str(self.total_price)+"원 담기")

    def basket_in_menu(self, menu_name):
        self.canvas_menu_click.pack_forget()
        self.canvas_menu.pack(expand=True, fill='both')
        self.canvas_menu.config(scrollregion=self.canvas_menu.bbox("all"))
        self.canvas_menu.bind("<Configure>", self.on_canvas_configure)
        self.canvas_menu.bind_all("<MouseWheel>", self.on_mousewheel)

        self.basket[menu_name] = self.selected_values.copy()
        self.basket[menu_name]['가격'] = self.total_price

        self.go_basket()
        self.value_list = []
        self.key_list = []
        self.text = ''
        if hasattr(self, 'basket_text'):
            self.basket_text.place_forget()
            self.basket_image.place_forget()
            self.button_more.place_forget()
        for self.key, value in self.basket.items():
            for sub_key, sub_value in value.items():
                self.key_list.insert(-1, sub_key)
                self.value_list.insert(-1, sub_value)
        self.basket_frame_frame = tk.Frame(self.basket_frame, width=500, height=450, highlightcolor='black',borderwidth=5,relief=RIDGE,bg='white')
        self.basket_frame_frame.place(x=20, y=20)
        self.basket_delete = tk.Button(self.basket_frame_frame, width=10, height=3, text='삭제',
                                       command=lambda frame=self.basket_frame_frame: self.basket_remove(frame), bd=0,bg='white')
        self.basket_delete.place(x=400, y=380)
        self.basket_frame_label = tk.Label(self.basket_frame_frame, text=menu_name, font=('', 25),bg='white')
        self.basket_frame_delivery = tk.Label(self.basket_frame_frame, text=self.delivery_time + ' 후 도착', font=('', 8),bg='white')
        self.basket_frame_label1 = tk.Label(self.basket_frame_frame, font=('', 13),bg='white')
        for i in range(len(self.value_list)):
            self.text += str(self.key_list[i] + ':' + str(self.value_list[i])) + '\n'
            if isinstance(self.value_list[i],int):
                self.text_price.append(self.value_list[i])
                self.text_name.append(menu_name)
        self.basket_frame_label1.config(text=self.text, anchor='nw',bg='white')
        self.text = ''
        self.basket = {}
        self.request_la = tk.Label(self.basket_frame_frame, text="요청사항",bg='white')
        self.request_entry = tk.Entry(self.basket_frame_frame, font=('', 13))
        if menu_name == ('반반 : L'):
            self.basket_frame_img = tk.Label(self.basket_frame_frame, width=150, height=150,
                                             image=self.tk_image_menu[2],bg='white')
        if menu_name == ('콤비네이션'):
            self.basket_frame_img = tk.Label(self.basket_frame_frame, width=150, height=150,
                                             image=self.tk_image_menu[1],bg='white')
        if menu_name == ('교동찜닭 : 소(반마리)'):
            self.basket_frame_img = tk.Label(self.basket_frame_frame, width=150, height=150,
                                             image=self.tk_image_menu[2],bg='white')
        if menu_name == ('돈소바세트'):
            self.basket_frame_img = tk.Label(self.basket_frame_frame, width=150, height=150,
                                             image=self.tk_image_menu[1],bg='white')
        if menu_name == ('불고기버거세트'):
            self.basket_frame_img = tk.Label(self.basket_frame_frame, width=150, height=150,
                                             image=self.tk_image_menu[2], bg='white')
        if menu_name == ('핫크리스피버거세트'):
            self.basket_frame_img = tk.Label(self.basket_frame_frame, width=150, height=150,
                                             image=self.tk_image_menu[1], bg='white')
        self.basket_store_name = tk.Label(self.basket_frame_frame, text=self.name, font=('', 12),bg='white')
        self.basket_store_name.place(x=40, y=10)
        if self.name == ('피자의생명은치즈다 대전서구점'):
            self.basket_store_img = tk.Label(self.basket_frame_frame, image=self.tk_image_store[6], width=20, height=20,bg='white')
        if self.name == ('교동찜닭 대전서구점'):
            self.basket_store_img = tk.Label(self.basket_frame_frame, image=self.tk_image_store[0], width=20, height=20,bg='white')
        if self.name == ('센카츠'):
            self.basket_store_img = tk.Label(self.basket_frame_frame, image=self.tk_image_store[0], width=20, height=20,bg='white')
        if self.name == ('롯데리아 대전시청점'):
            self.basket_store_img = tk.Label(self.basket_frame_frame, image=self.tk_image_store[0], width=20, height=20,bg='white')
        self.basket_store_img.place(x=10, y=10)
        self.basket_frame_img.place(x=330, y=80)
        self.basket_frame_label1.place(x=0, y=150)
        # self.basket_frame_label2.place(x=0, y=190)
        # self.basket_frame_label3.place(x=0, y=230)
        # self.basket_frame_label4.place(x=0, y=310)
        self.request_la.place(x=0, y=350)
        self.request_entry.place(x=100, y=350)
        # self.basket_frame_label5.place(x=0, y=270)
        self.basket_frame_label.place(x=0, y=100)

        self.basket_frame_delivery.place(x=10, y=50)
        self.basket_list.insert(0, self.basket_frame_frame)  # 새로운 위젯을 리스트의 처음에 추가
        self.update_frame_positions()  # 위젯 위치 업데이트
        self.store_name.insert(0, self.name) #xxxxxxxxxxxxxxxxx
        if len(self.store_name) >= 2 and self.store_name[0] != self.store_name[1]:
            for frame in self.basket_list:
                frame.destroy()
                self.basket_list.remove(frame)
                self.update_frame_positions()
                del self.store_name[0]

    def basket_remove(self, frame):
        if frame in self.basket_list:
            frame.destroy()  # 레이블을 삭제합니다.
            self.basket_list.remove(frame)  # 리스트에서도 제거합니다.
            self.update_frame_positions()
            del self.store_name[0]
            if not self.basket_list:
                self.basket_text.place(x=150, y=450)
                self.basket_image.place(x=175, y=200)
                self.button_more.place(x=180, y=500)

    def update_frame_positions(self):
        for idx, label in enumerate(self.basket_list):
            label.place(x=30, y=idx * 500)


    def on_canvas_configure4(self, event):
        self.canvas_menu_click.config(scrollregion=self.canvas_menu_click.bbox("all"))

    def on_mousewheel4(self, event):
        self.canvas_menu_click.yview_scroll(-1 * (event.delta // 120), "units")

    def click_store(self, store_name):
        self.sock.send(("#4 "+store_name).encode())

    def click_menu(self, menu_name, store_name):
        self.canvas_menu.pack_forget()
        self.sock.send(("#6 "+menu_name+"||"+store_name).encode())

    def back_click(self):
        self.canvas_select_store.pack_forget()
        if hasattr(self, 'canvas_menu'):
            self.canvas_menu.pack_forget()
        self.main_form()
        self.main_form_up()
        self.main_form_down()

    def create_select_store(self, store_data):
        self.up_main_frame.place_forget()
        self.main_frame.place_forget()
        self.down_main_frame.place_forget()
        self.backk_img = PhotoImage(file='back.png')
        if hasattr(self, 'canvas_select_store'):
            self.canvas_select_store.pack_forget()

        self.scrollbar_select_store = tk.Scrollbar(main_form, orient="vertical")

        self.canvas_select_store = tk.Canvas(main_form, yscrollcommand=self.scrollbar_select_store.set, bg='white', width=550)
        self.canvas_select_store.pack(expand=True, fill='both')
        self.scrollbar_select_store.config(command=self.canvas_select_store.yview)

        self.select_store_frame = tk.Frame(self.canvas_select_store, bg='#F6F6F6', width=550, height=700)
        self.up_select_store_frame = tk.Frame(self.canvas_select_store, bg='white', width=550, height=150)

        back_btn = tk.Button(self.up_select_store_frame, image=self.backk_img,command=self.back_click,bd=0,highlightthickness=0)
        back_btn.place(x=0,y=5)
        self.up_store_label = tk.Label(self.up_select_store_frame, text='종류', font=('', 25), bg='white').place(x=50, y=10)
        self.home = tk.Button(self.up_select_store_frame, bg='white', bd=0, image=del_home_img, width=30,
                              height=30, command=self.main_form)
        main_form.home.place(x=470, y=10)
        main_form.basket = tk.Button(self.up_select_store_frame, image=del_basket_img, bg='white', width=30, height=30,
                                     bd=0, command=self.go_basket)
        main_form.basket.place(x=510, y=7)
        main_form.testbut1 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='족발,보쌈', bd=0)
        main_form.testbut1.place(x=0, y=95)
        main_form.testbut2 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='찜,탕,찌개', bd=0)
        main_form.testbut2.place(x=80, y=95)
        main_form.testbut3 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='일식', bd=0,command=lambda: self.choice_store('일식',0))
        main_form.testbut3.place(x=160, y=95)
        main_form.testbut4 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='피자', bd=0,command=lambda: self.choice_store('피자',0))
        main_form.testbut4.place(x=240, y=95)
        main_form.testbut5 = tk.Button(self.up_select_store_frame, bg='white', image=del_right_img, bd=0, width=30,
                                       height=30, command=self.change_loc_left)
        main_form.testbut5.place(x=500, y=65)
        main_form.testbut6 = tk.Button(self.up_select_store_frame, bg='white', image=del_left_img, bd=0, width=30,
                                       height=30, command=self.change_loc_right)
        main_form.testbut6.place(x=15, y=65)
        main_form.testbut7 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='고기,구이', bd=0)
        main_form.testbut7.place(x=320, y=95)
        main_form.testbut8 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='야식', bd=0)
        main_form.testbut8.place(x=400, y=95)
        main_form.testbut9 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='양식', bd=0)
        main_form.testbut9.place(x=480, y=95)
        main_form.testbut10 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='치킨', bd=0,command=lambda: self.choice_store('치킨',0))
        main_form.testbut10.place(x=560, y=95)
        main_form.testbut11 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='중식', bd=0)
        main_form.testbut11.place(x=640, y=95)
        main_form.testbut12 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='아시안', bd=0,command=lambda: self.choice_store('아시안',0))
        main_form.testbut12.place(x=720, y=95)
        main_form.testbut13 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='한식', bd=0,command=lambda: self.choice_store('한식',0))
        main_form.testbut13.place(x=800, y=95)
        main_form.testbut14 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='도시락', bd=0)
        main_form.testbut14.place(x=880, y=95)
        main_form.testbut15 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='분식', bd=0,command=lambda: self.choice_store('분식',0))
        main_form.testbut15.place(x=960, y=95)
        main_form.testbut16 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='디저트', bd=0,command=lambda: self.choice_store('디저트',0))
        main_form.testbut16.place(x=1040, y=95)
        main_form.testbut17 = tk.Button(self.up_select_store_frame, bg='white', width=10, height=3, text='패스트푸드', bd=0,command=lambda: self.choice_store('패스트푸드',0))
        main_form.testbut17.place(x=1120, y=95)



        main_form.home = tk.Button(self.up_select_store_frame, text='홈', font=('', 20), bg='white', bd=0,
                                   command=self.main_form)
        main_form.home.place(x=600, y=20)
        main_form.basket = tk.Button(self.up_select_store_frame, text='장바구니', font=('', 20), bg='white', bd=0,
                                     command=lambda: self.go_basket)
        main_form.basket.place(x=700, y=20)


        global select_store_form
        store = store_data.split("|")
        store_list = []
        self.store_main_images = []

        print("len",len(store))

        y = 0
        for i in range(len(store)):
            store_frame = tk.Frame(self.select_store_frame,width=550,height=110, borderwidth=1, bg='white')
            store_frame.place(x=0, y=y)
            store_list.append(store_frame)

            store_name = store[i].split(',')[0]

            font_instance_names = font.Font(family="Arial Black", size=12, weight='bold')
            store_names = tk.Label(store_frame, text=store_name, bg='white', font=font_instance_names)
            store_names.place(x=100, y=3)


            store_star_img = tk.Label(store_frame, image=star_img, bg='white')
            store_star_img.place(x=97, y=25)

            store_rating = store[i].split(',')[1]
            font_instance_rating = font.Font(family="Arial Black", size=10,weight='bold')
            store_ratings = tk.Label(store_frame, text=store_rating, bg='white',font=font_instance_rating)
            store_ratings.place(x=122, y=28)


            store_deli_time = store[i].split(',')[2]
            store_deli_times = tk.Label(store_frame, text=store_deli_time, bg='white')
            store_deli_times.place(x=100, y=53)


            store_deli_tip = store[i].split(',')[3]
            store_deli_tips = tk.Label(store_frame, text=store_deli_tip, bg='white')
            store_deli_tips.place(x=200, y=53)

            store_min_la = tk.Label(store_frame, text="최소주문", bg='white',fg="gray")
            store_min_la.place(x=100, y=78)

            store_min = store[i].split(',')[4]
            store_mins = tk.Label(store_frame, text=store_min, bg='white')
            store_mins.place(x=150, y=78)

            store_main_img = tk.Canvas(store_frame, width=80,height=80,bg='white')
            store_main_img.place(x=10, y=10)

            store_img = store[i].split(',')[5]
            if store[i].split(',')[5] != "None":
                tmpImg = store_img[2:-1]
                tmpImg = tmpImg.encode()
                decoded_image_data = base64.b64decode(tmpImg)
                image = Image.open(io.BytesIO(decoded_image_data))
                image = image.resize((80, 80))
                tk_image = ImageTk.PhotoImage(image)
                store_main_img.create_image(0, 0, anchor=tk.NW, image=tk_image)
                self.store_main_images.append(tk_image)
                self.tk_image = ImageTk.PhotoImage(image)
                self.tk_image_store.insert(0, self.tk_image)
                store_main_img.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
                self.store_main_images.append(self.tk_image)

            y += 113
            store_list[i].bind('<Button-1>', lambda event, arg=f'{store_name}': self.click_store(arg))

        self.select_store_frame.configure(height=y)
        self.canvas_select_store.create_window((0, 0), window=self.up_select_store_frame, anchor='nw')
        self.canvas_select_store.create_window((0, 150), window=self.select_store_frame, anchor='nw')

        self.canvas_select_store.update_idletasks()

        self.canvas_select_store.config(scrollregion=self.canvas_select_store.bbox("all"))
        self.canvas_select_store.bind("<Configure>", self.on_canvas_configure2)
        self.canvas_select_store.bind_all("<MouseWheel>", self.on_mousewheel2)
        self.canvas_menu.pack_forget()
    def on_canvas_configure2(self, event):
        self.canvas_select_store.config(scrollregion=self.canvas_select_store.bbox("all"))

    def on_mousewheel2(self, event):
        self.canvas_select_store.yview_scroll(-1 * (event.delta // 120), "units")  # 마우스 휠 스크롤 기능 구현

    def go_select_store(self, data):
        pass
        # self.up_main_frame.place_forget()
        # self.main_frame.place_forget()
        # self.select_store_frame = tk.Frame(main_form, bg='gray', width=900, height=550)
        # self.select_store_frame.place(x=0, y=150)
        # self.up_select_store_frame = tk.Frame(main_form, bg='silver', width=900, height=150)
        # self.up_select_store_frame.place(x=0, y=0)
        # global select_store_form
        # label11 = tk.Label(self.select_store_frame, text=data)
        # label11.pack()
        #
        # # self.store_but1 = tk.Button(self.select_store_frame, text='가게1번', bg='white', font=('', 30), width=25, height=2,
        # #                             bd=0, command=self.choice_memu).place(x=250, y=40)
        # # canvas_store1_img = tk.Canvas(self.select_store_frame, bg='red', width=100, height=100, bd=0)
        # # canvas_store1_img.place(x=50, y=40)
        # # self.store_but2 = tk.Button(self.select_store_frame, text='가게2번', bg='white', font=('', 30), width=25, height=2,
        # #                             bd=0, command=self.choice_memu).place(x=250, y=140)
        # # canvas_store2_img = tk.Canvas(self.select_store_frame, bg='blue', width=100, height=100, bd=0)
        # # canvas_store2_img.place(x=50, y=140)
        # # self.store_but3 = tk.Button(self.select_store_frame, text='가게3번', bg='white', font=('', 30), width=25, height=2,
        # #                             bd=0, command=self.choice_memu).place(x=250, y=240)
        # # canvas_store1_img = tk.Canvas(self.select_store_frame, bg='yellow', width=100, height=100, bd=0)
        # # canvas_store1_img.place(x=50, y=240)
        # # self.store_but4 = tk.Button(self.select_store_frame, text='가게4번', bg='white', font=('', 30), width=25, height=2,
        # #                             bd=0, command=self.choice_memu).place(x=250, y=340)
        # # canvas_store1_img = tk.Canvas(self.select_store_frame, bg='gray', width=100, height=100, bd=0)
        # # canvas_store1_img.place(x=50, y=340)
        # # self.store_but5 = tk.Button(self.select_store_frame, text='가게5번', bg='white', font=('', 30), width=25, height=2,
        # #                             bd=0, command=self.choice_memu).place(x=250, y=440)
        # # canvas_store1_img = tk.Canvas(self.select_store_frame, bg='brown', width=100, height=100, bd=0)
        # # canvas_store1_img.place(x=50, y=440)
        # self.up_store_label = tk.Label(self.up_select_store_frame, text='종류', font=('', 60), bg='silver').place(x=20,
        #                                                                                                         y=20)
        # main_form.home = tk.Button(self.up_select_store_frame, text='홈', font=('', 20), bg='white', bd=0,
        #                            command=self.main_form)
        # main_form.home.place(x=600, y=20)
        # main_form.basket = tk.Button(self.up_select_store_frame, text='장바구니', font=('', 20), bg='white', bd=0,
        #                              command=lambda: self.go_basket('main'))
        # main_form.basket.place(x=700, y=20)
    def go_review(self):
        if hasattr(self,'total_order'):
            self.total_order.place_forget()
            self.up_total_order.place_forget()
        self.up_review_frame_user = tk.Frame(width=550,height=100,bg='silver')
        self.review_frame_user = tk.Frame(width=550,height=750,bg='yellow')
        self.up_review_frame_user.place(x=0,y=0)
        self.review_frame_user(x=0,y=100)
    def go_review_write(self):
        if hasattr(self,'total_order'):
            self.total_order.place_forget()
            self.up_total_order.place_forget()
        self.review_write_frame = tk.Frame(main_form,height=850,width=550,bg='white')
        self.write_frame= tk.Frame(self.review_write_frame,width=450,height=200,bg='blue')
        self.review_write_frame.place(x=0,y=0)
        self.write_frame.place(x=50,y=250)
        self.write_entry = tk.Text(self.write_frame,font=('',20))
        self.write_entry.place(x=0,y=0)
        self.review_img_regist = tk.Button(self.review_write_frame,height=50,width=50,command=self.review_img,bg='white',image=del_camera_img,bd=0)
        self.review_img_regist.place(x=50,y=475)
        self.img_use_canvas = tk.Canvas(self.review_write_frame,height=80,width=80,bg='white',bd=0)
        self.img_use_canvas.place(x=150,y=475)
        self.complete_btn = tk.Button(self.review_write_frame,height=3,width=30,bg=login_color,text='완료',font=('',20),fg='white',command=self.make_review)
        self.complete_btn.place(x=30,y=740)
        self.gohome_btn = tk.Button(self.review_write_frame,command=self.main_form,image=del_arrow_img,bd=0,bg='white')
        self.gohome_btn.place(x=10,y=10)
        print('fffffff')
    def review_img(self):
        global review_img_reg
        img_path = filedialog.askopenfilename(initialdir="\\", title="이미지 선택",
                                        filetypes=(("이미지 파일", "*.png *.jpg *.jpeg"), ("모든 파일", "*.*")))
        if img_path:
            self.image_path = img_path

            # 캔버스의 크기 가져오기
            canvas_width = self.img_use_canvas.winfo_width()
            canvas_height = self.img_use_canvas.winfo_height()

            # 이미지 불러오기 및 크기 조절
            img = Image.open(img_path)
            img.thumbnail((canvas_width, canvas_height))

            # 이미지를 캔버스에 추가
            review_img_reg = ImageTk.PhotoImage(img)
            self.img_use_canvas.create_image(0, 0, anchor='nw', image=review_img_reg)
            self.img_use_canvas.image = review_img_reg
    def go_total_review(self):
        if hasattr(self,'up_info_frame'):
            self.up_info_frame.place_forget()
            self.info_frame.place_forget()
            self.down_info_frame.place_forget()
        if not hasattr(self, 'total_review_frame'):
            self.total_review_frame = tk.Frame(main_form,width=550,height=850,bg='blue')
            self.up_total_review_frame = tk.Frame(main_form,width=550,height=100,bg='green')
            self.up_total_review_frame.place(x=0,y=0)
            self.total_review_frame.place(x=0,y=100)
            self.user_review_count = tk.Label(self.total_review_frame,text='내가 쓴 총 리뷰' + str(int(random.uniform(0, 20))) + '개', font=('', 25))
            self.user_review_count.place(x=10, y=300)
            self.user_review_gohome = tk.Button(self.up_total_review_frame,command=self.main_form)
            self.user_review_gohome.place(x=300,y=20)
        else:
            self.total_review_frame.place(x=0,y=100)
            self.up_total_review_frame.place(x=0,y=0)
    def make_review(self):
        self.go_total_review()
        self.make_review_frame = tk.Frame(self.total_review_frame,width=550,height=100,bg='black')
        self.review_list.insert(0, self.make_review_frame)  # 새로운 위젯을 리스트의 처음에 추가
        self.update_review_positions()  # 위젯 위치 업데이트
        self.delete_btn = tk.Button(self.make_review_frame,width=3,height=2,command=lambda:self.review_delete(self.make_review_frame))
        self.delete_btn.place(x=300,y=20)
        print(self.review_list)
    def review_delete(self,frame):
        frame.destroy()
        self.review_list.remove(frame)
        self.update_review_positions()
    def update_review_positions(self):
        for idx, label in enumerate(self.review_list):
            label.place(x=0, y=idx * 200)


    def choice_memu(self, origin):
        pass

    def choice_info(self, origin):
        pass

    def go_review(self, origin):
        pass
    def go_main_from(self):
        pass


form = form(root)
root.protocol("WM_DELETE_WINDOW", form.on_main_form_close)
form.master.mainloop()


