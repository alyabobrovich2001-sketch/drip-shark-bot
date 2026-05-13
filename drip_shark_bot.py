import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

# === НАСТРОЙКИ ===
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_CHAT_ID = 8815125744
# =================

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Мы — Drip Shark 🦈\n\n"
        "Оригинальный стритвир прямо из Рима 🇮🇹\n"
        "Stone Island, Carhartt, Nike, Adidas и не только.\n\n"
        "Напиши что тебя интересует — и мы свяжемся с тобой в ближайшее время 👇"
    )

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = update.message

    notification = (
        f"📦 Новый заказ!\n\n"
        f"👤 От: {user.full_name}"
        f"{f' (@{user.username})' if user.username else ''}\n"
        f"🆔 ID: {user.id}\n\n"
        f"💬 Сообщение:\n{message.text}"
    )

    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=notification
    )

    await message.reply_text(
        "Спасибо! Твой запрос принят!\n\n"
        "В ближайшее время свяжемся с тобой для уточнения деталей 🦈"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))
    print("Бот запущен ✅")
    app.run_polling()
