import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ FARIEBOT GLOBAL 24/7 activo. Usa /clima <ciudad> para consultar el clima.")

async def clima(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor indica una ciudad. Ejemplo: /clima Bogotá")
        return
    ciudad = " ".join(context.args)
    await update.message.reply_text(f"🌤 Clima en {ciudad}: (consulta real aquí)")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("clima", clima))

if __name__ == "__main__":
    app.run_polling()
