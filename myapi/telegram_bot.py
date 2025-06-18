import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from decouple import config
from asgiref.sync import sync_to_async


# Django setup (only needed if running outside manage.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')  
django.setup()

from myapi.models import TelegramUser

TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")

@sync_to_async
def save_user(user):
    TelegramUser.objects.get_or_create(
        telegram_id=user.id,
        defaults={
            "username": user.username or "",
            "first_name": user.first_name or ""
        }
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await save_user(user)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="You're registered!")


def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
