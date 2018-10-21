from selenium import webdriver
from bs4 import BeautifulSoup
import time
from datetime import datetime
import config
from selenium.webdriver.chrome.options import Options
import helper_methods


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(config.DRIVER_PATH, chrome_options=options)


def login(driver):
    driver.get('https://www.facebook.com/login.php?login_attempt=1&lwv=110')
    email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
    email.send_keys(config.EMAIL)

    password = driver.find_element_by_xpath("//input[@id='pass']")
    password.send_keys(config.PASSWORD)

    button = driver.find_element_by_xpath("//button[@id='loginbutton']")
    button.click()


def scroll_down(driver):
    SCROLL_PAUSE_TIME = 0.5

    for i in range(5):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)


def get_page_html(driver):
    driver.get('https://www.facebook.com/kpiclimbing/')
    scroll_down(driver)
    return driver.page_source


def get_all_posts(driver):
    html = get_page_html(driver)
    soup = BeautifulSoup(html, 'lxml')
    posts_block = soup.find_all('div', class_='_1xnd')[2].find('div', class_='_4-u2 _3xaf _3-95 _4-u8')
    posts = posts_block.find_all('div', class_='_5va1 _427x')
    driver.quit()
    return posts


def check_posts(bot):
    driver = webdriver.Chrome(config.DRIVER_PATH, chrome_options=options)
    for post in get_all_posts(driver):
        post_text = post.find('div', class_='_5pbx userContent _3576').get_text()
        post_date = post.find('abbr')['title']
        registration_date = helper_methods.read_registration_date()
        message_text = '\n' + post_text + '\n' + '\n'.join(config.usernames)

        photo = open(config.PHOTO_PATH, 'rb')

        if config.keyword in post_text and helper_methods.get_datetime(registration_date) < helper_methods.get_datetime(post_date):
            helper_methods.write_registration_date(post_date)
            message = bot.send_photo(config.CHAT_ID,
                                     photo,
                                     caption=message_text,
                                     parse_mode='Markdown')
            bot.pin_chat_message(config.CHAT_ID, message.message_id)
