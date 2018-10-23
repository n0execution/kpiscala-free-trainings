import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
print(bot.get_me())
