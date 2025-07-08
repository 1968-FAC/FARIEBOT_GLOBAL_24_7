from telegram import InputFile
from telegram.ext import ContextTypes
import os

def validar_archivo(archivo: InputFile) -> bool:
    extensiones_validas = ['.jpg', '.jpeg', '.png', '.gif']
    extension = os.path.splitext(archivo.name)[1].lower()
    return extension in extensiones_validas

async def enviar_archivo(bot, chat_id, archivo: InputFile, context: ContextTypes.DEFAULT_TYPE):
    if validar_archivo(archivo):
        await bot.send_document(chat_id=chat_id, document=archivo)
    else:
        await context.bot.send_message(chat_id=chat_id, text="Archivo no válido. Solo imágenes .jpg, .png, .gif.")
