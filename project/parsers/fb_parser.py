from project import config
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome(config.DRIVER_PATH)


def get_page_html():
    driver.get('https://www.facebook.com/kpiclimbing/')
    driver.execute_script("window.scrollTo(0, 3600)")
    return driver.page_source


def get_all_posts():
    html = get_page_html()
    soup = BeautifulSoup(html, 'lxml')
    posts = soup.find('div', class_='_1xnd').find_all('div', class_='_4-u2 _4-u8')
