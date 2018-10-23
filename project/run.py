from time import sleep

from bot import bot, config
from parsers import fb_parser, tg_parser


while(True):
    try:
        print('checking telegram...')
        tg_parser.check_posts(bot)
        print('checking facebook...')
        fb_parser.check_posts(bot)
        print('checked')
    except Exception as e:
        print('ERROR:', e)
        break
    sleep(60)
