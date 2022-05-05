import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
import keyboard

warnings.filterwarnings("ignore", category=DeprecationWarning)


def customspam():
    with open('config.json', 'r') as json_file:
        json_load = json.load(json_file)
        url = (json_load['url'])
        msg = (json_load['msg'])
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver.get(url)
    time.sleep(1)
    while True:
        try:
            time.sleep(.5)
            driver.find_element(By.XPATH, """/html/body/div/div[3]/div/div[1]/div[2]/form""").click()
            keyboard.write(msg)
            driver.find_element(By.XPATH, """/html/body/div/div[3]/div/div[2]/div/div[2]""").click()
            time.sleep(.5)
            driver.refresh()
        except Exception as e:
            pass


if __name__ == "__customspam__":
    customspam()
