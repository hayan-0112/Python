import serial
import time

# 시리얼 포트 설정
ser = serial.Serial('COM3', 9600)

# RGB 값을 입력받는 함수

try:
    while True:
        # RGB 값을 입력받음
        rgb_values = input("rgb 입력: ")
        response = ser.write(rgb_values.encode().strip())


        # 결과를 시리얼 모니터로부터 읽어와서 출력
        print("Arduino response:", response)

        time.sleep(0.1)
except KeyboardInterrupt:
    ser.close()
