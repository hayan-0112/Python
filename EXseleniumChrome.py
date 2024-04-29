import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

selector=''

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://mcea.co.kr/sub3-3/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6Mzt9&page=4')
time.sleep(3)
target=driver.find_elements(By.CLASS_NAME, 'text')
print(len(target))
print(target[14])


temp=[]
for i in range(len(target)):
    if '스프링' in target[i].text:
        temp.append(target[i].text)
for i in temp:
    print(i)