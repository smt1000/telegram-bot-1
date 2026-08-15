import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

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
	
	bot.send_photo(
        message.chat.id,
        "https://images.steamusercontent.com/ugc/965355694153811922/DF6B86B28B17363E7529D2980F1580D221B2B96D/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
		caption="Emily asks whether Daniel wants to join the student council.",
		reply_markup=keyboard
    )


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
