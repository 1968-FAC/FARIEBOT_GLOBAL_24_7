import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

def enviar_mensaje(chat_id, mensaje):
    bot.send_message(chat_id=chat_id, text=mensaje)
