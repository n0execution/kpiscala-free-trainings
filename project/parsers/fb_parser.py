from project import config
from selenium import webdriver


driver = webdriver.Chrome(config.DRIVER_PATH)


def get_page_html():
    driver.get('https://www.facebook.com/kpiclimbing/')
    return driver.page_source
