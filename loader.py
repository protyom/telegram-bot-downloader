from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
from secrets import TOKEN


def handle_message(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id
    if text == 'go':
        new_text = bot.send_message(chat_id='@colloc_tvims1', text="Ща бы догадаться как в чат писать")
    else:
        bot.send_message(chat_id=chat_id, text="На чат не похоже")


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=handle_message))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
