import time

import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

selector=''
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

singer={}

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.melon.com/chart/index.htm")
time.sleep(3)
target=driver.find_elements(By.CLASS_NAME, 'rank02')
print(len(target))
print(target[14])
temp=[]
for i in range(len(target)):
    sing = target[i].text
    if len(sing.split(','))>1:
        for i in sing.split(','):
            if i not in singer:
                singer[i] = 1
            else:
                a=singer[i]
                b=a+1
                singer[sing] = b
    else:
        if sing not in singer:
            singer[sing] = 1
        else:
            a = singer[sing]
            b = a + 1
            singer[sing] = b

ratio = list(singer.values())
labels= list(singer.keys())

plt.pie(ratio, labels=labels, autopct='%.1f%%') #explode 칸 강조
plt.show()