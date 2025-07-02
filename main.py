import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 FARIEBOT GLOBAL 24/7 activo.\n"
        "Comandos disponibles:\n"
        "/clima <ciudad> - Consulta el clima\n"
    )

# Comando /clima
async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor indica una ciudad. Ejemplo: /clima Bogotá")
        return
    ciudad = " ".join(context.args)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        clima_text = f"🌡 {data['main']['temp']}°C, {data['weather'][0]['description'].capitalize()}"
        await update.message.reply_text(f"Clima en {ciudad}: {clima_text}")
    else:
        await update.message.reply_text("No se pudo obtener el clima. Verifica la ciudad.")

# Crear app
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("clima", clima))

if __name__ == "__main__":
    app.run_polling()
