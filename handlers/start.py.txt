# handlers/start.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    teclado = [
        ["🗂️ Categorías"],
        ["🛍️ Añadir tienda", "🎁 Sorteo", "🌟 Hazte VIP"]
    ]
    reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
    await update.message.reply_text(
        "¡Bienvenido a Ahorrify! 🤩\n"
        "Tu aliado para encontrar las mejores ofertas en tu ciudad.\n\n"
        "Solo sigue estos simples pasos:\n"
        "1. Elige la categoría donde quieres ahorrar.\n"
        "2. Selecciona tu ciudad.\n\n"
        "🎉 ¡Y listo! Comienza a ahorrar como nunca antes.",
        reply_markup=reply_markup
    )
