#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uuid import uuid4
import re, json, requests
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, ParseMode
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '402368953:AAFBcA-TUEyR7-DQMxAzIA-IzPNahiWahfM'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Salut les moules! Qui veut du boobies ??')


def help(bot, update):
    update.message.reply_text('RTFM')

def random(bot, update):
    random_elo = json.loads(requests.get('http://ns3276663.ip-5-39-89.eu:58080/api/random').text)
    # marche pas
    cado = "http://ns3276663.ip-5-39-89.eu:58080/static/gifs/%s" % random_elo['gif']
    # marche 
    cado = "https://media.giphy.com/media/3ov9k4IWLQYD0VMnII/giphy.gif"
    cado = "https://media.giphy.com/media/l1J9LkBgw4fMVk59e/giphy.gif"
    chat_id = update.message.chat_id

    bot.send_document(chat_id=chat_id, document=cado)

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("random", random))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()