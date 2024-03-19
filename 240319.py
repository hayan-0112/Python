import threading
import time
count = 0

def sum(low, high):
    total=0
    count=0
    for i in range(low, high):
        total += i
    print("subthread", total)
    while 1:
        count += 15
        time.sleep(5)
        print("\nsubthread 실행", count)

def sum2(low, high):
    print("sum2 thread")

x=threading.Thread(target=sum, args=(1,1000))
x.start()
listx=[]

def hello():
    print("hello")
while 1:
    if input("mainThread input prompt"):
        hello()
    time.sleep(0.2)