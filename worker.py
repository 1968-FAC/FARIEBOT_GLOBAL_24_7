import os
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)

def enviar_mensaje(chat_id, mensaje):
    bot.send_message(chat_id=chat_id, text=mensaje)

# Desactívalo si no quieres que se ejecute siempre
# enviar_mensaje(TU_CHAT_ID, "Mensaje automático del worker.")
