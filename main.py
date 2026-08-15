import os
import telebot
from telebot import types
from dotenv import load_dotenv
import requests
from io import BytesIO

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing from your .env file")

bot = telebot.TeleBot(TOKEN)

# Question 1 image
IMAGE_URL = "https://www.google.com/search?client=firefox-b-d&hs=IQ7&sca_esv=83613a3736d28f94&sxsrf=APpeQnvKi8YQHTaXtg8mSOSu41aNo4y3-A:1786827237694&udm=2&fbs=ABfTbFVJO0ctw5DBIgF--R-NkTdwaeIxnKtn4hyO9aK-HrUEjLnKeVoeg_5IfRVof07sBuPJI26VeyZqjAK-ICpQd1rVRJfWs_-MJwVlQmfLoBujQuwrWV7PtH3MtITqqc5jBrHVEK7fFKjFfZJNFPVHNi4YpVM5TqeSko4aMQn7tyhQ5Cigje2t1pvpCN62RX7YlxpE27uYv-c1Mnpz0lIJfpRHrkY65hOrqFNuKSPEY_T1X9EinKbcHjR1OmEeaI2vystVZuDG&q=anime+girl&sa=X&ved=2ahUKEwjkjZyWwqOWAxUlVKQEHfmQGEwQtKgLegQIERAB&biw=1280&bih=595&dpr=1.5#sv=CAMSVhoyKhBlLUQ1VV9tdUhSWVgteG9NMg5ENVVfbXVIUllYLXhvTToOaVNGRURsWnd5YzFUa00gBCocCgZtb3NhaWMSEGUtRDVVX211SFJZWC14b00YADABGAcgtY-V9w9KCBABGAEgASgB"


@bot.message_handler(commands=["start"])
def start(message):

    # Create answer buttons
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I’d like to help.",
            callback_data="q1_1"
        )
    )

    keyboard.add(
        types.InlineKeyboardButton(
            "2. I’m not really a leadership person.",
            callback_data="q1_2"
        )
    )

    keyboard.add(
        types.InlineKeyboardButton(
            "3. I’ll try it once.",
            callback_data="q1_3"
        )
    )

    keyboard.add(
        types.InlineKeyboardButton(
            "4. Why do you want me there?",
            callback_data="q1_4"
        )
    )

    # Download image from URL
    try:
        response = requests.get(IMAGE_URL, timeout=15)
        response.raise_for_status()

        photo = BytesIO(response.content)
        photo.name = "question1.jpg"

        # Send image
        bot.send_photo(
            message.chat.id,
            photo
        )

    except Exception as e:
        print(f"Image error: {e}")

    # Send question and buttons
    bot.send_message(
        message.chat.id,
        "Emily asks whether Daniel wants to join the student council.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("q1_"))
def question_1_answer(call):

    answers = {
        "q1_1": "I’d like to help.",
        "q1_2": "I’m not really a leadership person.",
        "q1_3": "I’ll try it once.",
        "q1_4": "Why do you want me there?"
    }

    answer = answers.get(call.data)

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n{answer}"
    )


print("Bot is running...")

bot.delete_webhook(drop_pending_updates=True)
bot.infinity_polling()
import os
import telebot
from telebot import types
from dotenv import load_dotenv
load_dotenv()
import requests
import json
import time



TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing from your .env file")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I’d like to help.",
            callback_data="q1_1"
        )
    )

    keyboard.add(
        types.InlineKeyboardButton(
            "2. I’m not really a leadership person.",
            callback_data="q1_2"
        )
    )

    keyboard.add(
        types.InlineKeyboardButton(
            "3. I’ll try it once.",
            callback_data="q1_3"
        )
    )

    keyboard.add(
        types.InlineKeyboardButton(
            "4. Why do you want me there?",
            callback_data="q1_4"
        )
    )
	
	bot.send_message(
        message.chat.id,
        "Emily asks whether Daniel wants to join the student council.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )
	
	time.sleep(5)


    bot.send_message(
        message.chat.id,
        "Emily asks whether Daniel wants to join the student council.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("q1_"))
def question_1_answer(call):

    answers = {
        "q1_1": "I’d like to help.",
        "q1_2": "I’m not really a leadership person.",
        "q1_3": "I’ll try it once.",
        "q1_4": "Why do you want me there?"
    }

    answer = answers.get(call.data)

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n{answer}"
    )


print("Bot is running...")

bot.delete_webhook(drop_pending_updates=True)
bot.infinity_polling()
