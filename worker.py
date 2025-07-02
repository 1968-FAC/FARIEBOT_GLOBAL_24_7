import os
from telegram import Bot
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)

# Ejemplo: enviar un mensaje automático
def enviar_mensaje(chat_id, mensaje):
    bot.send_message(chat_id=chat_id, text=mensaje)

# Ejemplo de uso (lo desactivas si no lo quieres de una vez ejecutando)
# enviar_mensaje(TU_CHAT_ID, "Mensaje automático del worker.")
