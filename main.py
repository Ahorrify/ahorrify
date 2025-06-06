# main.py
# -------------------------------------------------------
# Bot Ahorrify - Archivo principal (arranca la aplicación)
# -------------------------------------------------------

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)
from config import TOKEN
from handlers.start import start
from handlers.categorias import handle_categorias
from handlers.ciudades import handle_ciudad_seleccion
from handlers.callback_offers import callback_query_handler
from handlers.registro import handle_registro

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Handler para /start
    app.add_handler(CommandHandler("start", start))

    # Handlers para mensajes de texto (categorías, ciudades, registro)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_categorias))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_ciudad_seleccion))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_registro))

    # Handler para botones inline (“Ver otra oferta” y “Regresar”)
    app.add_handler(CallbackQueryHandler(callback_query_handler))

    # Confirmación en consola
    print("Bot en ejecución...")

    # Poner el bot a escuchar mensajes
    app.run_polling()

if __name__ == "__main__":
    main()
