import json
from telegram import Update, Bot
from telegram.ext import CommandHandler, Dispatcher, MessageHandler, Filters
from modules.handlers import *

def getTextInFile(file_path):
  file = open(file_path)
  text = file.readline()
  file.close()

  return text


class GenBot:
  def __init__(self, token, endpointUrl):
    self.bot = Bot(token)
    self.dispatcher = Dispatcher(self.bot, None, use_context=True)
    self.url = endpointUrl

    self.build()
  
  def build(self):
    self.dispatcher.add_handler(CommandHandler("start", start))
    self.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    self.dispatcher.add_handler(MessageHandler(Filters.command, unknown))


  def lambda_handler(self, event, context):
    self.dispatcher.process_update(Update.de_json(json.loads(event['body']), self.bot))
    return { 'statusCode': 200 }

def createBot():
  TESTINGBOT_TOKEN = getTextInFile('./env/TestingBot/token.txt')
  ENDPOINT_URL = getTextInFile('./env/endpointUrl.txt')

  TestingBot = GenBot(TESTINGBOT_TOKEN, ENDPOINT_URL)

  return TestingBot



  

 

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