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
# QUESTION 5 SCORES
# ============================================================

QUESTION_5_SCORES = {
    "q5_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q5_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q5_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q5_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 6 SCORES
# ============================================================

QUESTION_6_SCORES = {
    "q6_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q6_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q6_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q6_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 7 SCORES
# ============================================================

QUESTION_7_SCORES = {
    "q7_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q7_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q7_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q7_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 8 SCORES
# ============================================================

QUESTION_8_SCORES = {
    "q8_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q8_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q8_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q8_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 9 SCORES
# ============================================================

QUESTION_9_SCORES = {
    "q9_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q9_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q9_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q9_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 10 SCORES
# ============================================================

QUESTION_10_SCORES = {
    "q10_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q10_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q10_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q10_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 11 SCORES
# ============================================================

QUESTION_11_SCORES = {
    "q11_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q11_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q11_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q11_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 12 SCORES
# ============================================================

QUESTION_12_SCORES = {
    "q12_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q12_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q12_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q12_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 13 SCORES
# ============================================================

QUESTION_13_SCORES = {
    "q13_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q13_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q13_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q13_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 14 SCORES
# ============================================================

QUESTION_14_SCORES = {
    "q14_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q14_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q14_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q14_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 15 SCORES
# ============================================================

QUESTION_15_SCORES = {
    "q15_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q15_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q15_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q15_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 16 SCORES
# ============================================================

QUESTION_16_SCORES = {
    "q16_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q16_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q16_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q16_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 17 SCORES
# ============================================================

QUESTION_17_SCORES = {
    "q17_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q17_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q17_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q17_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 18 SCORES
# ============================================================

QUESTION_18_SCORES = {
    "q18_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q18_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q18_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q18_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 19 SCORES
# ============================================================

QUESTION_19_SCORES = {
    "q19_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q19_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q19_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q19_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 20 SCORES
# ============================================================

QUESTION_20_SCORES = {
    "q20_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q20_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q20_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q20_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}

QUESTION_21_SCORES = {
    "q21_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q21_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q21_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q21_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}

QUESTION_22_SCORES = {
    "q22_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q22_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q22_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q22_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}

QUESTION_23_SCORES = {
    "q23_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q23_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q23_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q23_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}

QUESTION_24_SCORES = {
    "q24_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q24_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q24_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q24_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}

QUESTION_25_SCORES = {
    "q25_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q25_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q25_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q25_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}

# ============================================================
# QUESTION 26 SCORES
# ============================================================

QUESTION_26_SCORES = {
    "q26_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q26_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q26_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q26_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 27 SCORES
# ============================================================

QUESTION_27_SCORES = {
    "q27_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q27_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q27_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q27_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 28 SCORES
# ============================================================

QUESTION_28_SCORES = {
    "q28_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q28_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q28_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q28_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 29 SCORES
# ============================================================

QUESTION_29_SCORES = {
    "q29_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q29_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q29_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q29_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 30 SCORES
# ============================================================

QUESTION_30_SCORES = {
    "q30_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q30_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q30_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q30_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 31 SCORES
# ============================================================

QUESTION_31_SCORES = {
    "q31_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q31_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q31_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q31_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 32 SCORES
# ============================================================

QUESTION_32_SCORES = {
    "q32_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q32_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q32_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q32_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 33 SCORES
# ============================================================

QUESTION_33_SCORES = {
    "q33_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q33_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q33_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q33_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 34 SCORES
# ============================================================

QUESTION_34_SCORES = {
    "q34_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q34_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q34_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q34_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 35 SCORES
# ============================================================

QUESTION_35_SCORES = {
    "q35_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q35_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q35_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q35_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 36 SCORES
# ============================================================

QUESTION_36_SCORES = {
    "q36_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q36_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q36_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q36_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 37 SCORES
# ============================================================

QUESTION_37_SCORES = {
    "q37_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q37_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q37_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q37_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 38 SCORES
# ============================================================

QUESTION_38_SCORES = {
    "q38_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q38_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q38_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q38_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 39 SCORES
# ============================================================

QUESTION_39_SCORES = {
    "q39_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q39_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q39_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q39_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 40 SCORES
# ============================================================

QUESTION_40_SCORES = {
    "q40_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q40_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q40_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q40_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 41 SCORES
# ============================================================

QUESTION_41_SCORES = {
    "q41_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q41_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q41_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q41_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 42 SCORES
# ============================================================

QUESTION_42_SCORES = {
    "q42_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q42_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q42_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q42_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 43 SCORES
# ============================================================

QUESTION_43_SCORES = {
    "q43_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q43_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q43_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q43_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 44 SCORES
# ============================================================

QUESTION_44_SCORES = {
    "q44_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q44_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q44_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q44_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 45 SCORES
# ============================================================

QUESTION_45_SCORES = {
    "q45_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q45_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q45_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q45_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 46 SCORES
# ============================================================

QUESTION_46_SCORES = {
    "q46_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q46_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q46_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q46_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 47 SCORES
# ============================================================

QUESTION_47_SCORES = {
    "q47_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q47_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q47_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q47_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 48 SCORES
# ============================================================

QUESTION_48_SCORES = {
    "q48_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q48_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q48_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q48_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 49 SCORES
# ============================================================

QUESTION_49_SCORES = {
    "q49_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q49_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q49_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q49_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 50 SCORES
# ============================================================

QUESTION_50_SCORES = {
    "q50_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q50_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q50_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q50_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 51 SCORES
# ============================================================

QUESTION_51_SCORES = {
    "q51_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q51_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q51_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q51_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 52 SCORES
# ============================================================

QUESTION_52_SCORES = {
    "q52_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q52_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q52_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q52_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 53 SCORES
# ============================================================

QUESTION_53_SCORES = {
    "q53_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q53_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q53_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q53_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 54 SCORES
# ============================================================

QUESTION_54_SCORES = {
    "q54_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q54_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q54_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q54_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 55 SCORES
# ============================================================

QUESTION_55_SCORES = {
    "q55_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q55_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q55_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q55_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 56 SCORES
# ============================================================

QUESTION_56_SCORES = {
    "q56_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q56_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q56_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q56_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 57 SCORES
# ============================================================

QUESTION_57_SCORES = {
    "q57_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q57_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q57_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q57_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 58 SCORES
# ============================================================

QUESTION_58_SCORES = {
    "q58_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q58_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q58_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q58_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 59 SCORES
# ============================================================

QUESTION_59_SCORES = {
    "q59_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q59_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q59_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q59_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 60 SCORES
# ============================================================

QUESTION_60_SCORES = {
    "q60_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q60_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q60_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q60_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 61 SCORES
# ============================================================

QUESTION_61_SCORES = {
    "q61_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q61_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q61_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q61_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 62 SCORES
# ============================================================

QUESTION_62_SCORES = {
    "q62_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q62_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q62_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q62_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 63 SCORES
# ============================================================

QUESTION_63_SCORES = {
    "q63_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q63_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q63_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q63_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 64 SCORES
# ============================================================

QUESTION_64_SCORES = {
    "q64_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q64_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q64_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q64_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 65 SCORES
# ============================================================

QUESTION_65_SCORES = {
    "q65_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q65_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q65_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q65_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 66 SCORES
# ============================================================

QUESTION_66_SCORES = {
    "q66_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q66_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q66_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q66_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 67 SCORES
# ============================================================

QUESTION_67_SCORES = {
    "q67_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q67_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q67_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q67_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 68 SCORES
# ============================================================

QUESTION_68_SCORES = {
    "q68_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q68_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q68_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q68_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 69 SCORES
# ============================================================

QUESTION_69_SCORES = {
    "q69_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q69_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q69_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q69_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 70 SCORES
# ============================================================

QUESTION_70_SCORES = {
    "q70_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q70_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q70_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q70_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
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




#سؤال 1

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
# IMAGE
# ============================================================

IMAGE_URL = "https://images.steamusercontent.com/ugc/965355694153811922/DF6B86B28B17363E7529D2980F1580D221B2B96D/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false"


# ============================================================
# QUESTION 1
# ============================================================

@bot.message_handler(commands=["start"])
def start(message):

    # Create/reset user's scores
    user_id = message.from_user.id
    user_scores[user_id] = create_new_score()

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 1
    # --------------------------------------------------------

    bot.send_message(
        message.chat.id,
        "Emily and Daniel are talking after school.\n\n"
        "Emily wants to know if Daniel would be interested "
        "in joining the student council."
    )

    # --------------------------------------------------------
    # QUESTION 1 BUTTONS
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # QUESTION 1 IMAGE
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # QUESTION 1 TEXT
    # --------------------------------------------------------

    bot.send_message(
        message.chat.id,
        "Emily asks whether Daniel wants to join "
        "the student council.\n\n"
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

    # --------------------------------------------------------
    # ADD POINTS
    # --------------------------------------------------------

    points = QUESTION_1_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n"
        f"{answer}"
		
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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 1
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully to Daniel's answer.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION WILL GO HERE
    # --------------------------------------------------------

    # Example:
    #
     send_question_2(call.message.chat.id)

#سؤال 2

# ============================================================
# QUESTION 2
# ============================================================

def send_question_2(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 2
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "A little later, Sophie joins the conversation.\n\n"
        "She asks Daniel what he thinks about helping "
        "with an upcoming school event."
    )

    # --------------------------------------------------------
    # QUESTION 2 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Sure, I can help.",
            callback_data="q2_1"
        ),
        types.InlineKeyboardButton(
            "2. I think someone else should do it.",
            callback_data="q2_2"
        ),
        types.InlineKeyboardButton(
            "3. I'll help if you need me.",
            callback_data="q2_3"
        ),
        types.InlineKeyboardButton(
            "4. What exactly would I have to do?",
            callback_data="q2_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 2 IMAGE
    # --------------------------------------------------------

    QUESTION_2_IMAGE_URL = IMAGE_URL

    try:
        response = requests.get(
            QUESTION_2_IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        photo = BytesIO(response.content)
        photo.name = "question2.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 2 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 2 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Sophie asks Daniel whether he would help "
        "with the school event.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 2 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q2_")
)
def question_2_answer(call):

    answers = {
        "q2_1": "Sure, I can help.",
        "q2_2": "I think someone else should do it.",
        "q2_3": "I'll help if you need me.",
        "q2_4": "What exactly would I have to do?"
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 2 POINTS
    # --------------------------------------------------------

    points = QUESTION_2_SCORES.get(call.data)

    if points:
        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n"
        f"{answer}"
    )

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 2
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Sophie considers Daniel's response.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_3(call.message.chat.id)


# ============================================================
# QUESTION 3
# ============================================================

def send_question_3(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 3
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "The conversation continues after the school event.\n\n"
        "Grace asks Daniel how he feels about working with "
        "other students on a difficult project."
    )

    # --------------------------------------------------------
    # QUESTION 3 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I enjoy working with other people.",
            callback_data="q3_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd rather work on my own.",
            callback_data="q3_2"
        ),
        types.InlineKeyboardButton(
            "3. I can work with a team if necessary.",
            callback_data="q3_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd like to know more about the project first.",
            callback_data="q3_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 3 IMAGE
    # --------------------------------------------------------

    QUESTION_3_IMAGE_URL = IMAGE_URL

    try:
        response = requests.get(
            QUESTION_3_IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        photo = BytesIO(response.content)
        photo.name = "question3.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 3 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 3 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Grace asks Daniel how he feels about working "
        "with other students on a difficult project.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 3 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q3_")
)
def question_3_answer(call):

    answers = {
        "q3_1": "I enjoy working with other people.",
        "q3_2": "I'd rather work on my own.",
        "q3_3": "I can work with a team if necessary.",
        "q3_4": "I'd like to know more about the project first."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 3 POINTS
    # --------------------------------------------------------

    points = QUESTION_3_SCORES.get(call.data)

    if points:
        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n"
        f"{answer}"
    )

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 3
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Grace thinks about Daniel's response.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_4(call.message.chat.id)


# ============================================================
# QUESTION 4
# ============================================================

def send_question_4(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 4
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "The conversation continues after Daniel talks "
        "with Grace.\n\n"
        "Charlotte asks Daniel what he would do when "
        "faced with an important decision."
    )

    # --------------------------------------------------------
    # QUESTION 4 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd ask someone I trust for advice.",
            callback_data="q4_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd make the decision myself.",
            callback_data="q4_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd think carefully before deciding.",
            callback_data="q4_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd consider what everyone else thinks.",
            callback_data="q4_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 4 IMAGE
    # --------------------------------------------------------

    QUESTION_4_IMAGE_URL = IMAGE_URL

    try:
        response = requests.get(
            QUESTION_4_IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        photo = BytesIO(response.content)
        photo.name = "question4.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 4 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 4 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Charlotte asks Daniel what he would do when "
        "faced with an important decision.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 4 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q4_")
)
def question_4_answer(call):

    answers = {
        "q4_1": "I'd ask someone I trust for advice.",
        "q4_2": "I'd make the decision myself.",
        "q4_3": "I'd think carefully before deciding.",
        "q4_4": "I'd consider what everyone else thinks."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 4 POINTS
    # --------------------------------------------------------

    points = QUESTION_4_SCORES.get(call.data)

    if points:
        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n"
        f"{answer}"
    )

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 4
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Charlotte thinks about Daniel's response.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_5(call.message.chat.id)


# ============================================================
# QUESTION 5
# ============================================================

def send_question_5(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 5
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "After speaking with Charlotte, Daniel continues "
        "the conversation with Emily.\n\n"
        "Emily asks Daniel how he would react if a friend "
        "needed his help with a difficult problem."
    )

    # --------------------------------------------------------
    # QUESTION 5 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd help them right away.",
            callback_data="q5_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd help if I had enough time.",
            callback_data="q5_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd encourage them to solve it themselves.",
            callback_data="q5_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd ask what kind of help they need first.",
            callback_data="q5_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 5 IMAGE
    # --------------------------------------------------------

    QUESTION_5_IMAGE_URL = IMAGE_URL

    try:
        response = requests.get(
            QUESTION_5_IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        photo = BytesIO(response.content)
        photo.name = "question5.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 5 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 5 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel how he would react if a friend "
        "needed his help with a difficult problem.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 5 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q5_")
)
def question_5_answer(call):

    answers = {
        "q5_1": "I'd help them right away.",
        "q5_2": "I'd help if I had enough time.",
        "q5_3": "I'd encourage them to solve it themselves.",
        "q5_4": "I'd ask what kind of help they need first."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 5 POINTS
    # --------------------------------------------------------

    points = QUESTION_5_SCORES.get(call.data)

    if points:
        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n"
        f"{answer}"
    )

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 5
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily appreciates Daniel's answer.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_6(call.message.chat.id)


# ============================================================
# QUESTION 6
# ============================================================

def send_question_6(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 6
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "The conversation continues as Daniel talks "
        "with Sophie.\n\n"
        "Sophie asks Daniel what he would do if he "
        "disagreed with a close friend."
    )

    # --------------------------------------------------------
    # QUESTION 6 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd tell them honestly what I think.",
            callback_data="q6_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd avoid arguing about it.",
            callback_data="q6_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd try to find a compromise.",
            callback_data="q6_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd ask them why they feel that way.",
            callback_data="q6_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 6 IMAGE
    # --------------------------------------------------------

    QUESTION_6_IMAGE_URL = IMAGE_URL

    try:
        response = requests.get(
            QUESTION_6_IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        photo = BytesIO(response.content)
        photo.name = "question6.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 6 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 6 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Sophie asks Daniel what he would do if he "
        "disagreed with a close friend.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 6 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q6_")
)
def question_6_answer(call):

    answers = {
        "q6_1": "I'd tell them honestly what I think.",
        "q6_2": "I'd avoid arguing about it.",
        "q6_3": "I'd try to find a compromise.",
        "q6_4": "I'd ask them why they feel that way."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 6 POINTS
    # --------------------------------------------------------

    points = QUESTION_6_SCORES.get(call.data)

    if points:
        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        f"You selected:\n\n"
        f"{answer}"
    )

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 6
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Sophie thinks about Daniel's response.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    # Question 7 will go here later:
    #
    # send_question_7(call.message.chat.id)


# ============================================================
# START BOT
# ============================================================

print("Bot is running...")

bot.delete_webhook(drop_pending_updates=True)
bot.infinity_polling()
