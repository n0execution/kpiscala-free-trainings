from parsers import fb_parser, tg_parser
from time import sleep
from bot import bot, config


while(True):
    print('checking telegram...')
    tg_parser.check_posts(bot)
    print('checking facebook...')
    fb_parser.check_posts(bot)
    print('checked')
    sleep(60)
