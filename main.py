import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

# ✅ Cargar tokens desde variables de entorno
TOKEN = os.getenv("TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# ✅ Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy FARIEBOT GLOBAL 24/7.\n"
        "Comandos disponibles:\n"
        "/clima <ciudad> - Consulta el clima\n"
        "/trafico - Consulta el tráfico\n"
        "/vuelos - Consulta vuelos\n"
        "/radar - Información de radar"
    )

# ✅ Comando /clima
async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Por favor escribe /clima <ciudad>")
        return
    ciudad = " ".join(context.args)
    try:
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={OPENWEATHER_API_KEY}&lang=es&units=metric"
        )
        data = response.json()
        if response.status_code == 200:
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            await update.message.reply_text(
                f"Clima en {ciudad}: {weather}, temperatura: {temp}°C"
            )
        else:
            await update.message.reply_text(f"No pude obtener el clima de {ciudad}.")
    except Exception as e:
        await update.message.reply_text(f"Error al consultar clima: {e}")

# ✅ Comando /trafico
async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de tráfico: [Aquí integrarías la API real].")

# ✅ Comando /vuelos
async def vuelos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de vuelos: [Aquí integrarías la API real].")

# ✅ Comando /radar
async def radar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Información de radar: [Aquí integrarías la API real].")

# ✅ Configuración de la aplicación
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clima", clima))
    app.add_handler(CommandHandler("trafico", trafico))
    app.add_handler(CommandHandler("vuelos", vuelos))
    app.add_handler(CommandHandler("radar", radar))

    app.run_polling()

if __name__ == "__main__":
    main()
