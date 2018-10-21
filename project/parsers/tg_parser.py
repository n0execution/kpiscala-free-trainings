from telethon import TelegramClient, sync
import config
from helper_methods import *
from pytz import timezone


def check_posts(bot):
    client = TelegramClient('session_name', config.API_ID, config.API_HASH)
    registration_date = read_registration_date()

    with client:
        for message in client.iter_messages('kpiclimbing', limit=20):
            condition1 = config.keyword in message.message
            condition2 = get_datetime(registration_date).replace(tzinfo=timezone('Europe/Kiev')) < convert_date(message.date)

            if condition1 and condition2:
                write_registration_date(convert_date(message.date).strftime("%d.%m.%Y %H:%M"))

                message_text = '\n' + message.message
                photo = open(config.PHOTO_PATH, 'rb')

                message = bot.send_photo(config.CHAT_ID,
                                         photo,
                                         caption=message_text,
                                         parse_mode='Markdown')
                bot.send_message(config.CHAT_ID, '\n'.join(config.usernames))
                bot.pin_chat_message(config.CHAT_ID, message.message_id)
