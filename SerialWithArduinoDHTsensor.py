import serial
import time
ser = serial.Serial('COM3', 9600)

try:
    while True:
        line = ser.readline().decode().strip()
        #ser.write() ser.write()로 아두이노에 데이터 전송 가능 , encode()후 전송
        if line.startswith('Temperature'):
            print("Received:", line)
        time.sleep(0.1)
except KeyboardInterrupt:
    ser.close()