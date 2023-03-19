from selenium import webdriver  # 웹수집 자동화를 위한 크롬 드라이버 호출
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, os
import urllib.request


driver = webdriver.Chrome()  # 크롬드라이버 위치 (크롬버전확인)
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element("name","q")
elem.send_keys("손흥민")
elem.send_keys(Keys.RETURN)

os.makedirs('손흥민', exist_ok=True)

SCROLL_PAUSE_TIME = 5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.execute_script("document.getElementById('smb').click();")
            driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(0.5)
        #//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img
        imgUrl = driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[2]/div[2]/div[2]/c-wiz/div/div[1]/div[2]/div[2]/div/a/img').get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, '손흥민/'+ str(count) + ".jpg")
        count = count + 1
    except:
        pass

driver.quit()