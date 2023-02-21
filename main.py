from concurrent.futures import ThreadPoolExecutor
from random import choice
import time
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from seleniumwire import webdriver
import requests


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")
option1s = webdriver.ChromeOptions()

acc = 190 # cкок всего аккаунтов
thr = 3 # сколько одновременно регать

# Автор - https://t.me/rudtyt



f = open('proxy.txt', 'r')
i = 0
for line in f:
    i
    i += 1
with open("proxy.txt", "r") as f:
    proxy = f.read().split('\n')
    i = i - 1


def work(proxy):
    try:
        print("")
        # proxy1 = {
        #     "proxy": {
        #         "https": f"http://{proxy}"
        #     }
        # }
        # print(proxy)
        try:

            driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
            wait = WebDriverWait(driver, 30)
            driver.get("https://vrlps.co/jn00gf0/cp") # реф ссылка
            name = "".join([choice("abcdefghijklmnopqrstuvwxyz") for _ in range(15)])
            seco = "".join([choice("abcdefghijklmnopqrstuvwxyz") for _ in range(15)])
            iframe = driver.find_elements(By.TAG_NAME, 'iframe')[0]
            driver.switch_to.frame(iframe)
            wait.until(EC.element_to_be_clickable((By.ID, 'firstname'))).send_keys(name)
            wait.until(EC.element_to_be_clickable((By.ID, 'lastname'))).send_keys(seco)

            r = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
            mail = r.text
            mal = mail.replace('[', '').replace(']', '').replace('"', '')
            wait.until(EC.element_to_be_clickable((By.ID, 'email'))).send_keys(mal)
            wait.until(EC.element_to_be_clickable((By.ID, 'participationSubmitNoReferrer'))).click()
            j = 0
            while j == 0:
                try:
                    mails = mal.split("@")

                    h = requests.get(
                        f"https://www.1secmail.com/api/v1/?action=getMessages&login={mails[0]}&domain={mails[1]}")  # проверка письма
                    y = h.json()[0]["id"]

                    o = requests.get(
                        f'https://www.1secmail.com/api/v1/?action=readMessage&login={mails[0]}&domain={mails[1]}&id={y}')
                    t = o.json()["body"]
                    myString_list = [r.group("url") for r in
                                     (re.search("(?P<url>https?://[^\s]+)", i) for i in t.split(" ")) if
                                     r is not None]
                    confirm1 = myString_list[6]
                    confirm = confirm1.replace('"', '')
                    with open('link.txt', 'a') as file:
                        file.write(f'{confirm}\n')
                    j = 1
                    # driver.execute_script(f"window.open('{confirm}', 'new_window')")
                    # driver.switch_to.window(driver.window_handles[1])
                except:
                    pass


        except Exception as ex:
            print(ex)


    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()




if __name__ == '__main__':
    y = 0
    with ThreadPoolExecutor(max_workers=thr) as executor:
        for x in range(acc):
            executor.submit(work, proxy)
            y = y + 1
            time.sleep(1)








