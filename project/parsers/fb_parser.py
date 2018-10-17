from project import config
from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome(config.DRIVER_PATH)


def login():
    driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
    email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
    email.send_keys(config.EMAIL)

    password = driver.find_element_by_xpath("//input[@id='pass']")
    password.send_keys(config.PASSWORD)

    button = driver.find_element_by_xpath("//button[@id='loginbutton']")
    button.click()


def scroll_down():
    SCROLL_PAUSE_TIME = 0.5

    for i in range(5):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)


def get_page_html():
    driver.get('https://www.facebook.com/kpiclimbing/')
    scroll_down()
    return driver.page_source


def get_all_posts():
    html = get_page_html()
    soup = BeautifulSoup(html, 'lxml')
    posts = soup.find('div', class_='_1xnd').find_all('div', class_='_4-u2 _4-u8')
