import schedule
import time

job1 = ""
job2 = ""
count = 0

def message1():
    print("스케쥴 실행 중")

def message2(text):
    print(text)

def stop():
    schedule.cancel_job(job1)

def start():
    global jop1
    global job2
    global count
    job1 = schedule.every(1).seconds.do(message1)
    job2 = schedule.every(3).seconds.do(message2, "3초 주기")

    while 1:
        schedule.run_pending()
        time.sleep(1)
        count = count + 1

start() #여기에 'start()'를 선언함으로써 while문을 빠져나오지 못하게 가능