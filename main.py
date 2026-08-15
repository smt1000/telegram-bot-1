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


# ============================================================
# IMAGE
# ============================================================

IMAGE_URL = "YOUR_IMAGE_URL"


# =========================
# TEXT BETWEEN QUESTIONS
# =========================

QUESTION_1_INTRO = (
    "Welcome to the questionnaire!\n\n"
    "Read the situation carefully and choose the response "
    "you think is most appropriate."
)

QUESTION_1_AFTER = (
    "Thank you for your answer!\n\n"
    "Let's continue to the next situation."
)

QUESTION_2_INTRO = (
    "Now let's look at another situation.\n\n"
    "Think carefully before choosing your answer."
)


# ============================================================
# SCORE CATEGORIES
# ============================================================

CATEGORIES = [
    "Emily",
    "Sophie",
    "Grace",
    "Charlotte",
    "Honest",
    "Independence",
    "ECompatibility",
    "SCompatibility",
    "GCompatibility",
    "CCompatibility"
]


# ============================================================
# QUESTION 1 SCORES
# ============================================================

QUESTION_1_SCORES = {

    "q1_1": {
        "Emily": 1,
        "Sophie": 0,
        "Grace": 1,
        "Charlotte": 1,
        "Honest": 1,
        "Independence": 1,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 1,
        "CCompatibility": 5,
    },

    "q1_2": {
        "Emily": 1,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 2,
        "Independence": 0,
        "ECompatibility": 5,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q1_3": {
        "Emily": 0,
        "Sophie": 1,
        "Grace": 1,
        "Charlotte": 1,
        "Honest": 1,
        "Independence": 2,
        "ECompatibility": 0,
        "SCompatibility": 5,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q1_4": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 2,
        "Charlotte": 1,
        "Honest": 3,
        "Independence": 1,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 10,
        "CCompatibility": 0,
    }
}


# ============================================================
# QUESTION 2 SCORES
# ============================================================

QUESTION_2_SCORES = {

    "q2_1": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q2_2": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q2_3": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q2_4": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    }
}


# ============================================================
# QUESTION 3 SCORES
# ============================================================

QUESTION_3_SCORES = {

    "q3_1": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q3_2": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q3_3": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q3_4": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    }
}


# ============================================================
# QUESTION 4 SCORES
# ============================================================

QUESTION_4_SCORES = {

    "q4_1": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q4_2": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q4_3": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q4_4": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 0,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    }
}


# ============================================================
# ALL QUESTION SCORES
# ============================================================

ALL_SCORES = {
    1: QUESTION_1_SCORES,
    2: QUESTION_2_SCORES,
    3: QUESTION_3_SCORES,
    4: QUESTION_4_SCORES,
}

for question_number in range(5, 99):
    ALL_SCORES[question_number] = {}



# ============================================================
# USER SCORES
# ============================================================

user_scores = {}


def create_new_score():
    """Create a new score dictionary with all categories at 0."""

    return {
        category: 0
        for category in CATEGORIES
    }


# ============================================================
# QUESTION 1
# ============================================================

@bot.message_handler(commands=["start"])
def start(message):

    # Create/reset user's scores
    user_id = message.from_user.id
    user_scores[user_id] = create_new_score()

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I’d like to help.",
            callback_data="q1_1"
        ),
        types.InlineKeyboardButton(
            "2. I’m not really a leadership person.",
            callback_data="q1_2"
        ),
        types.InlineKeyboardButton(
            "3. I’ll try it once.",
            callback_data="q1_3"
        ),
        types.InlineKeyboardButton(
            "4. Why do you want me there?",
            callback_data="q1_4"
        )
    )

    # Download the image
    try:
        response = requests.get(
            IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        print("Image status:", response.status_code)
        print("Image type:", response.headers.get("Content-Type"))

        photo = BytesIO(response.content)
        photo.name = "question1.jpg"

        bot.send_photo(
            message.chat.id,
            photo
        )

    except Exception as e:
        print("IMAGE ERROR:", e)

        bot.send_message(
            message.chat.id,
            f"Could not load the image.\n\nError: {e}"
        )

        return
		

    # Question text
	bot.send_message(
        message.chat.id,
        
		QUESTION_1_INTRO
    )
    bot.send_message(
        message.chat.id,
        "Emily asks whether Daniel wants to join the student council.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )
	


# ============================================================
# QUESTION 1 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q1_")
)
def question_1_answer(call):

    answers = {
        "q1_1": "I’d like to help.",
        "q1_2": "I’m not really a leadership person.",
        "q1_3": "I’ll try it once.",
        "q1_4": "Why do you want me there?"
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # Get the score dictionary for this answer
    points = QUESTION_1_SCORES.get(call.data)

    if points:

        # Add each category's points
        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n"
        f"{answer}\n\n"
        f"Current scores:\n\n"
        f"Emily: {user_scores[user_id]['Emily']}\n"
        f"Sophie: {user_scores[user_id]['Sophie']}\n"
        f"Grace: {user_scores[user_id]['Grace']}\n"
        f"Charlotte: {user_scores[user_id]['Charlotte']}\n\n"
        f"Honest: {user_scores[user_id]['Honest']}\n"
        f"Independence: {user_scores[user_id]['Independence']}\n\n"
        f"ECompatibility: {user_scores[user_id]['ECompatibility']}\n"
        f"SCompatibility: {user_scores[user_id]['SCompatibility']}\n"
        f"GCompatibility: {user_scores[user_id]['GCompatibility']}\n"
        f"CCompatibility: {user_scores[user_id]['CCompatibility']}"
    )


# ============================================================
# START BOT
# ============================================================

print("Bot is running...")

bot.delete_webhook(drop_pending_updates=True)
bot.infinity_polling()
