from telegram import Update
from telegram.ext import CallbackContext

def start (update: Update, context: CallbackContext):
  update.message.reply_text('Hello!')

def fruit(update: Update, context: CallbackContext):
  fruit = context.args[0]

  if fruit == "🍎":
    update.message.reply_photo(photo=open('./img/maca.jpg', 'rb'))
  elif fruit == "🍌":
    update.message.reply_photo(photo=open('./img/banana.jpg', 'rb'))

def echo_type(update: Update, context: CallbackContext):
  arg = context.args[0]

  context.user_data['echo'] = arg

def echo (update: Update, context: CallbackContext):
  if context.user_data['echo'] == 'reversed':
    update.message.reply_text(update.message.text[::-1])
    return
  
  update.message.reply_text(update.message.text)

def unknown (update: Update, context: CallbackContext):
  update.message.reply_photo(photo=open('./img/ata.jpg', 'rb'))