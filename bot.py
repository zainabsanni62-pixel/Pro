import os
import time
import telebot
from datetime import datetime

# Your bot token from BotFather
BOT_TOKEN = "8586657993:AAEfnDGBdLkLCtIJb_dpngCi7Luxlv8hirs"
CHAT_ID = -8586657993  # Replace with your group ID

bot = telebot.TeleBot(BOT_TOKEN)

def send_check_in():
    current_time = datetime.now().strftime("%I:%M %p")
    message = f"⏰ Hourly check-in ({current_time})!\n\nWhat are you currently working on, Great Minds?"
    bot.send_message(CHAT_ID, message)

if __name__ == "__main__":
    print("PurposeBot is now running...")
    while True:
        current_minute = datetime.now().minute
        current_second = datetime.now().second

        # Send at the start of every hour (e.g., 8:00, 9:00, etc.)
        if current_minute == 0 and current_second < 5:
            send_check_in()
            time.sleep(60)  # Wait a minute to avoid duplicate messages
        else:
            time.sleep(1)
