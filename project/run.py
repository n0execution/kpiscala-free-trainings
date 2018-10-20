from parsers import fb_parser
from time import sleep
from bot import bot, config


while(True):
    fb_parser.check_posts(bot)
    print('checked')
    sleep(60)
