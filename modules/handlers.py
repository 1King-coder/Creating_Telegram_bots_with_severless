def get_chat_id (update):
  return update.effective_chat.id

def start (update, context):
  context.bot.send_message(
    chat_id=get_chat_id(update),
    text="Hello! i am a test bot!"
  )

def echo (update, context):
  context.bot.send_message(
    chat_id=get_chat_id(update),
    text=update.message.text
  )

def reverse_echo (update, context):
  context.bot.send_message(
    chat_id=get_chat_id(update),
    text=update.message.text[::-1]
  )

def unknown (update, context):
  context.bot.send_message(
    chat_id=get_chat_id(update),
    text="I do not know what to do with this command goujujin-sama"
  )