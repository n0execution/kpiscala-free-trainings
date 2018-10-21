from telethon import TelegramClient, sync
import config


def check_posts(bot):
    client = TelegramClient('session_name', config.API_ID, config.API_HASH)
    with client:
        for message in client.iter_messages('kpiclimbing', limit=20):
            print(message.message)
