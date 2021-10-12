def start (update, context):
  update.message.reply_text('Hello!')

def echo (update, context):
  update.message.reply_text(update.message.text)

def reverse_echo (update, context):
  context.bot.send_message(
    chat_id=update.effective_chat.id,
    text='.'
  )

def unknown (update, context):
  context.bot.send_message(
    chat_id=get_chat_id(update),
    text="I do not know what to do with this command goujujin-sama"
  )