import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Obtén el token del entorno o colócalo directamente si lo deseas (no recomendado en producción)
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 FARIEBOT GLOBAL 24/7 activo.\n"
        "Comandos disponibles:\n"
        "/clima <ciudad> - Clima en tiempo real (demo)\n"
        "/vuelos - Consulta vuelos (próximamente)\n"
        "/trafico - Tráfico en tu zona (próximamente)"
    )

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Funcionalidad de clima en desarrollo 🌤️.")

async def vuelos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Funcionalidad de vuelos en desarrollo ✈️.")

async def trafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Funcionalidad de tráfico en desarrollo 🚗.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clima", clima))
    app.add_handler(CommandHandler("vuelos", vuelos))
    app.add_handler(CommandHandler("trafico", trafico))

    app.run_polling()

if __name__ == "__main__":
    main()
