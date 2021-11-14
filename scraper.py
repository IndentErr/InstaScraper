'''!!!! MAKE IT SO INSTAGRAM DOESN'T BAN BOT. ADD DELAYS AND MORE HUMAN TIMINGS'!!!!'''
# no failsafe for incorrect input/typos
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

def login():
    login_id = 'Your id'
    login_pw = 'Your passowrd'
    id_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    id_login.send_keys(login_id)
    pw_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    pw_login.send_keys(login_pw)
    click_login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    click_login.click()
    time.sleep(2)
    click_save = driver.find_element_by_class_name("sqdOP.yWX7d.y3zKF")
    click_save.click()
    time.sleep(1)
    click_notification = driver.find_element_by_class_name("aOOlW.HoLwm")
    click_notification.click()

dest_influ = "https://hypeauditor.com/top-instagram-all-united-states/"


driver = webdriver.Firefox(service_log_path=os.devnull)
driver.get(dest_influ)

'''!!!! MAKE IT SO INSTAGRAM DOESN'T BAN BOT. ADD DELAYS AND MORE HUMAN TIMINGS'!!!!'''
# allows multiple inputs and sorts id_list running function per each
id_list = []
i = 1
while i <= 20:
    influ_xpath_1 = "/html/body/div/div/div/div[1]/div/div[2]/div/div[2]/table/tbody/tr["
    influ_xpath_middle = str(i)
    influ_xpath_2 = "]/td[3]/div/div[2]/a[1]/div[1]/div"

    influ_xpath_final = influ_xpath_1 + influ_xpath_middle + influ_xpath_2

    influ_name = (driver.find_element_by_xpath(influ_xpath_final)).text
    id_list.append(influ_name)
    i = i + 1
print(id_list)

driver.get("https://www.instagram.com/accounts/login/")

time.sleep(1)

login()
date_time = time.strftime('%c', time.localtime(time.time()))
for insta_id in id_list:
    driver.get("http://www.instagram.com/" + insta_id + "/")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    insta = soup.select(".v1Nh3.kIKUG._bz0w")
    File_name_external = ".KL4Bh"
    n = 1
    for i in insta:
        print("https://www.instagram.com/" + i.a['href'])
        imgUrl = i.select_one(File_name_external).img['src']
        with urlopen(imgUrl) as f : 
            #Creates directory per person if folder doesn't exist
            if not os.path.exists(f'./img/{insta_id}'):
                os.makedirs(f'./img/{insta_id}')
            with open(f'./img/{insta_id}/' + date_time + insta_id + str(n) + '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)

            n+=1
    # Random delay to simulate human browsing, may need subprocess such as navigating back to homepage and then new page.
    #time.sleep(random.randint(3,10))
    time.sleep(2)
driver.quit()
'''!!!! MAKE IT SO INSTAGRAM DOESN'T BAN BOT. ADD DELAYS AND MORE HUMAN TIMINGS'!!!!'''
