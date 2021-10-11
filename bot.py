import json
from telegram import Update, Bot
from telegram.ext import CommandHandler, Dispatcher, MessageHandler, Filters
from modules.handlers import *

def getToken(file_path):
  token_file = open(file_path)
  TOKEN = token_file.readline()
  token_file.close()

  return TOKEN

class GenBot:
  def __init__(self, token):
    self.bot = Bot(token)
    self.dispatcher = Dispatcher(self.bot, None, use_context=True)

    self.build()
  
  def build(self):
    self.dispatcher.add_handler(CommandHandler("start", start))
    self.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    self.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

  def lambda_handler(self, event, context):
    self.dispatcher.process_update(Update.de_json(json.loads(event['body']), self.bot))
    return { 'statusCode': 200 }

def main():
  TOKEN = getToken('./env/TestingBot/token.txt')

  TestingBot = GenBot(TOKEN)

 

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