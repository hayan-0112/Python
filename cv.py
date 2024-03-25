import cv2
import numpy as np

image_path = "chicken.jpg"
image_array = cv2.imread(image_path) #Cv2영상처리 패키지

#imread : image read (이미지경로) image_array에 데이터 저장
print(image_array)
print(image_array.shape)
print(image_array.size)
print(image_array.dtype)
height, width, _ = image_array.shape
print(height)
print(width)
# print(_)
# widthhalf = width//2
# image_array[:,:widthhalf] = [0,0,0]
cv2.imshow("image result", image_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

# x=1
# y=1
# pix_v=image_array[y,x,0] #1,1픽셀의 B값 출력
#
# print("value", pix_v) #RGB값. 하지만 opencv는 거꾸로 뒤집어져서 나온다. 즉, BGR 값

#opencv로 불러온 이미지는 numpy배열 형태의 픽셀에 해당하는 B G R 값을 가진다.