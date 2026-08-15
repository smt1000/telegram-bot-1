import os
import time
import telebot
from telebot import types
from dotenv import load_dotenv
from commands import register_commands

# Load environment variables
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

try:
    bot = telebot.TeleBot(TOKEN)

    # Register your existing commands
    register_commands(bot)

    # Store questionnaire answers temporarily
    user_answers = {}

    @bot.message_handler(commands=["start", "hello"])
    def send_welcome(message):
        """
        Start the questionnaire.
        """
        user_id = message.from_user.id

        # Reset previous answers
        user_answers[user_id] = {}

        # Create answer buttons
        markup = types.InlineKeyboardMarkup(row_width=1)

        markup.add(
            types.InlineKeyboardButton(
                "1. I’d like to help.",
                callback_data="answer_1"
            ),
            types.InlineKeyboardButton(
                "2. I’m not really a leadership person.",
                callback_data="answer_2"
            ),
            types.InlineKeyboardButton(
                "3. I’ll try it once.",
                callback_data="answer_3"
            ),
            types.InlineKeyboardButton(
                "4. Why do you want me there?",
                callback_data="answer_4"
            )
        )

        bot.send_message(
            message.chat.id,
            "Emily asks whether Daniel wants to join the student council.\n\n"
            "Choose Daniel's response:",
            reply_markup=markup
        )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("answer_"))
    def handle_answer(call):
        """
        Handle the user's questionnaire answer.
        """
        user_id = call.from_user.id

        answers = {
            "answer_1": "I’d like to help.",
            "answer_2": "I’m not really a leadership person.",
            "answer_3": "I’ll try it once.",
            "answer_4": "Why do you want me there?"
        }

        selected_answer = answers.get(call.data)

        if selected_answer:
            # Save the answer
            if user_id not in user_answers:
                user_answers[user_id] = {}

            user_answers[user_id]["question_1"] = selected_answer

            # Remove the buttons
            bot.edit_message_reply_markup(
                call.message.chat.id,
                call.message.message_id,
                reply_markup=None
            )

            # Confirm the answer
            bot.send_message(
                call.message.chat.id,
                f"Your answer:\n{selected_answer}\n\n"
                "Thank you! Question 1 is complete."
            )

        # Tell Telegram the button press was received
        bot.answer_callback_query(call.id)

    # Remove webhook to avoid conflicts with polling
    bot.delete_webhook(drop_pending_updates=True)

    print("Bot is running...")
    bot.polling()

except Exception as e:
    print(
        f"CRITICAL ERROR: Failed to initialize bot with provided token. "
        f"Error: {e}"
    )

    print(
        "The application will hang to prevent a restart loop. "
        "Please fix the TELEGRAM_BOT_TOKEN environment variable."
    )

    while True:
        time.sleep(3600)
