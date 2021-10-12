import json
from requests import get
from telegram import Update, Bot
from telegram.ext import CommandHandler, Dispatcher, MessageHandler, Filters, Updater
from modules.handlers import *
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def getTextInFile(file_path):
  file = open(file_path)
  text = file.readline()
  file.close()

  return text


class TestingBot:
  def __init__(self, token):
    self.bot = Updater(token=token)
    self.dispatcher = self.bot.dispatcher

    self.build()
  
  def build(self):
    self.dispatcher.add_handler(CommandHandler("start", start))
    self.dispatcher.add_handler(CommandHandler("fruta", fruta))
    self.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), reverse_echo))
    self.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    self.bot.start_polling()
    self.bot.idle()

def main():
  TESTINGBOT_TOKEN = getTextInFile('./env/TestingBot/token.txt')

  TestingBot(TESTINGBOT_TOKEN)

if __name__ == '__main__':
  main()

  

  # threads = []
  # conn = threading.Thread(target=getBot, args=(TOKEN,))

  # threads.append(conn)

  # for thread in threads:
  #   thread.start()

  # print ('threadei com sucesso')

  # executing = True
  # while executing:
  #   executing = False

  #   for thread in threads:
  #     if thread.is_alive():
  #       executing = True
  #       break