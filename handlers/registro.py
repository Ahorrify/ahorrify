# handlers/registro.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

async def handle_registro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛍️ Añadir tienda" or text == "➕ Añadir tienda":
        teclado = [["📝 Formulario"], ["⬅️ Regresar"]]
        reply_markup = ReplyKeyboardMarkup(teclado, resize_keyboard=True)
        await update.message.reply_text(
            "🛍️ Con Ahorrify puedes atraer nuevos clientes interesados en tus productos.\n\n"
            "📣 Nos encargamos de toda la publicidad por ti, incluyendo campañas profesionales con Meta Ads.\n\n"
            "🎁 Ofrecemos sorteos, regalos y promociones para atraer aún más usuarios al bot.\n\n"
            "📋 ¿Quieres impulsar tu negocio y llegar a miles de venezolanos que desean comprar?\n"
            "👉 Rellena este formulario y postúlate para formar parte de nuestra comunidad de tiendas aliadas:\n"
            "https://forms.gle/rntFoqhEcquEYEyS6",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
        return

    if text == "⬅️ Regresar":
        from handlers.start import start
        await start(update, context)
        return

    if text == "📝 Formulario":
        await update.message.reply_text("📋 Abre el formulario aquí:\nhttps://forms.gle/rntFoqhEcquEYEyS6")
        return
