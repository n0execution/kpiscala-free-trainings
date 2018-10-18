from project import config
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from datetime import datetime


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

    for i in range(10):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)


def write_registration_date(post_date):
    with open('registration_date.txt', 'w') as f:
        f.write(post_date)


def get_page_html():
    driver.get('https://www.facebook.com/kpiclimbing/')
    scroll_down()
    return driver.page_source


def get_all_posts():
    html = get_page_html()
    soup = BeautifulSoup(html, 'lxml')
    posts_block = soup.find_all('div', class_='_1xnd')[2].find('div', class_='_4-u2 _3xaf _3-95 _4-u8')
    posts = posts_block.find_all('div', class_='_5va1 _427x')
    return posts


def check_posts():
    for post in get_all_posts():
        post_text = post.find('div', class_='_5pbx userContent _3576').get_text()
        post_date = post.find('abbr')['title']

        if config.keyword in post_text:
            write_registration_date(post_date)
            print('New registration')
