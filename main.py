import logging
import os
import time
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Bot token yahan daalna
BOT_TOKEN = "8485690087:AAHK_GSRC7yQK82PNTdN2bBnGzbmFNu-0W0"

# Logger setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Reply message
AUTO_REPLY = "⚡️ Auto-Reply:\nMain abhi offline hoon. Aapka message mil gaya, jald hi jawab dunga."

def handle_message(update, context):
    chat_id = update.effective_chat.id
    text = update.message.text
    logging.info(f"Message from {chat_id}: {text}")
    
    context.bot.send_message(chat_id=chat_id, text=AUTO_REPLY)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    logging.info("Bot started...")
    updater.idle()

if __name__ == '__main__':
    main()
