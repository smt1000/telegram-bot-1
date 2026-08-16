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
        "Grace": 0,
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
        "Emily": 1,
        "Sophie": 3,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 1,
        "Independence": 1,
        "ECompatibility": 0,
        "SCompatibility": 10,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q2_2": {
        "Emily": 0,
        "Sophie": 1,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 2,
        "Independence": 1,
        "ECompatibility": 0,
        "SCompatibility": 5,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q2_3": {
        "Emily": 1,
        "Sophie": 2,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 1,
        "Independence": 1,
        "ECompatibility": 0,
        "SCompatibility": 5,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q2_4": {
        "Emily": 0,
        "Sophie": -1,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 2,
        "Independence": 2,
        "ECompatibility": 0,
        "SCompatibility": 5,
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
        "Grace": 2,
        "Charlotte": 0,
        "Honest": 1,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 10,
        "CCompatibility": 0,
    },

    "q3_2": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 3,
        "Charlotte": 0,
        "Honest": 2,
        "Independence": 1,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 15,
        "CCompatibility": 0,
    },

    "q3_3": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": 1,
        "Charlotte": 0,
        "Honest": 2,
        "Independence": 2,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 10,
        "CCompatibility": 0,
    },

    "q3_4": {
        "Emily": 0,
        "Sophie": 0,
        "Grace": -1,
        "Charlotte": 0,
        "Honest": -1,
        "Independence": 1,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": -5,
        "CCompatibility": 0,
    }
}


# ============================================================
# QUESTION 4 SCORES
# ============================================================

QUESTION_4_SCORES = {

    "q4_1": {
        "Emily": 1,
        "Sophie": 2,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 1,
        "Independence": 0,
        "ECompatibility": 0,
        "SCompatibility": 5,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q4_2": {
        "Emily": 1,
        "Sophie": 0,
        "Grace": 0,
        "Charlotte": 0,
        "Honest": 1,
        "Independence": 2,
        "ECompatibility": 5,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q4_3": {
        "Emily": 1,
        "Sophie": 1,
        "Grace": 1,
        "Charlotte": 0,
        "Honest": 2,
        "Independence": 1,
        "ECompatibility": 5,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 0,
    },

    "q4_4": {
        "Emily": 0,
        "Sophie": 1,
        "Grace": 0,
        "Charlotte": 2,
        "Honest": 2,
        "Independence": 2,
        "ECompatibility": 0,
        "SCompatibility": 0,
        "GCompatibility": 0,
        "CCompatibility": 10,
    }
}

# ============================================================
# QUESTION 5 SCORES
# ============================================================

QUESTION_5_SCORES = {
    "q5_1": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 1, "ECompatibility": 10, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q5_2": {"Emily": -1, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 2, "ECompatibility": 5, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q5_3": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 2, "ECompatibility": 10, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q5_4": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 3, "ECompatibility": 15, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 6 SCORES
# ============================================================

QUESTION_6_SCORES = {
    "q6_1": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 10, "GCompatibility": 0, "CCompatibility": 0},
    "q6_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 1, "ECompatibility": 0, "SCompatibility": 5, "GCompatibility": 0, "CCompatibility": 0},
    "q6_3": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 1, "ECompatibility": 0, "SCompatibility": 10, "GCompatibility": 0, "CCompatibility": 0},
    "q6_4": {"Emily": 0, "Sophie": 1, "Grace": 1, "Charlotte": 0, "Honest": 2, "Independence": 2, "ECompatibility": 0, "SCompatibility": 5, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 7 SCORES
# ============================================================

QUESTION_7_SCORES = {
    "q7_1": {"Emily": 0, "Sophie": 0, "Grace": -2, "Charlotte": 0, "Honest": -2, "Independence": -1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": -10, "CCompatibility": 0},
    "q7_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
    "q7_3": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 3, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 20, "CCompatibility": 0},
    "q7_4": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 2, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 10, "CCompatibility": 0},
}


# ============================================================
# QUESTION 8 SCORES
# ============================================================

QUESTION_8_SCORES = {
    "q8_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 1, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 10},
    "q8_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 2, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 5},
    "q8_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 2, "Honest": 2, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 10},
    "q8_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 3, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 15},
}


# ============================================================
# QUESTION 9 SCORES
# ============================================================

QUESTION_9_SCORES = {
    "q9_1": {"Emily": 2, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 5, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q9_2": {"Emily": 0, "Sophie": 2, "Grace": 1, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 5, "GCompatibility": 0, "CCompatibility": 0},
    "q9_3": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 5, "CCompatibility": 0},
    "q9_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 2, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 5},
}


# ============================================================
# QUESTION 10 SCORES
# ============================================================

QUESTION_10_SCORES = {
    "q10_1": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 1, "ECompatibility": 10, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q10_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 2, "ECompatibility": 0, "SCompatibility": 5, "GCompatibility": 0, "CCompatibility": 0},
    "q10_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 2, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 10, "CCompatibility": 0},
    "q10_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 10},
}


# ============================================================
# QUESTION 11 SCORES
# ============================================================

QUESTION_11_SCORES = {
    "q11_1": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 10, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q11_2": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q11_3": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q11_4": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 10, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 12 SCORES
# ============================================================

QUESTION_12_SCORES = {
    "q12_1": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q12_2": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q12_3": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q12_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 15, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 13 SCORES
# ============================================================

QUESTION_13_SCORES = {
    "q13_1": {"Emily": 0, "Sophie": 0, "Grace": 1, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q13_2": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q13_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 10, "CCompatibility": 0},
    "q13_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
}


# ============================================================
# QUESTION 14 SCORES
# ============================================================

QUESTION_14_SCORES = {
    "q14_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 2, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q14_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q14_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q14_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 15},
}


# ============================================================
# QUESTION 15 SCORES
# ============================================================

QUESTION_15_SCORES = {
    "q15_1": {"Emily": 1, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": -1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q15_2": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q15_3": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q15_4": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 15, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 16 SCORES
# ============================================================

QUESTION_16_SCORES = {
    "q16_1": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q16_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q16_3": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q16_4": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 10, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 17 SCORES
# ============================================================

QUESTION_17_SCORES = {
    "q17_1": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q17_2": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q17_3": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
    "q17_4": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 2, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 18 SCORES
# ============================================================

QUESTION_18_SCORES = {
    "q18_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q18_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q18_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q18_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 15},
}


# ============================================================
# QUESTION 19 SCORES
# ============================================================

QUESTION_19_SCORES = {
    "q19_1": {"Emily": 1, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": -1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q19_2": {"Emily": 1, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": -1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q19_3": {"Emily": 2, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q19_4": {"Emily": 2, "Sophie": 2, "Grace": 1, "Charlotte": 1, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 20 SCORES
# ============================================================

QUESTION_20_SCORES = {
    "q20_1": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 10, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q20_2": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 10, "GCompatibility": 0, "CCompatibility": 0},
    "q20_3": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 10, "CCompatibility": 0},
    "q20_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 10},
}

QUESTION_21_SCORES = {
    "q21_1": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q21_2": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q21_3": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q21_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 15, "GCompatibility": 0, "CCompatibility": 0},
}

QUESTION_22_SCORES = {
    "q22_1": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q22_2": {"Emily": 1, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q22_3": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q22_4": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 15, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}

QUESTION_23_SCORES = {
    "q23_1": {"Emily": 0, "Sophie": 0, "Grace": 1, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q23_2": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q23_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q23_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
}

QUESTION_24_SCORES = {
    "q24_1": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q24_2": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q24_3": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q24_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 15, "GCompatibility": 0, "CCompatibility": 0},
}

QUESTION_25_SCORES = {
    "q25_1": {"Emily": 1, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q25_2": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q25_3": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q25_4": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 10},
}

# ============================================================
# QUESTION 26 SCORES
# ============================================================

QUESTION_26_SCORES = {
    "q26_1": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q26_2": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q26_3": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q26_4": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 15, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 27 SCORES
# ============================================================

QUESTION_27_SCORES = {
    "q27_1": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q27_2": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q27_3": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q27_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 15, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 28 SCORES
# ============================================================

QUESTION_28_SCORES = {
    "q28_1": {"Emily": 0, "Sophie": 0, "Grace": 1, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q28_2": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q28_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q28_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
}


# ============================================================
# QUESTION 29 SCORES
# ============================================================

QUESTION_29_SCORES = {
    "q29_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q29_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 2, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q29_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q29_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 15},
}


# ============================================================
# QUESTION 30 SCORES
# ============================================================

QUESTION_30_SCORES = {
    "q30_1": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 10, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q30_2": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 10, "GCompatibility": 0, "CCompatibility": 0},
    "q30_3": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 10, "CCompatibility": 0},
    "q30_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 10},
}


# ============================================================
# QUESTION 31 SCORES
# ============================================================

QUESTION_31_SCORES = {
    "q31_1": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 10, "GCompatibility": 0, "CCompatibility": 0},
    "q31_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q31_3": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q31_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 20, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 32 SCORES
# ============================================================

QUESTION_32_SCORES = {
    "q32_1": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q32_2": {"Emily": 0, "Sophie": 0, "Grace": 1, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q32_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q32_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 20, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 33 SCORES
# ============================================================

QUESTION_33_SCORES = {
    "q33_1": {"Emily": 1, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q33_2": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q33_3": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q33_4": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 20, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 34 SCORES
# ============================================================

QUESTION_34_SCORES = {
    "q34_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q34_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q34_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q34_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 20},
}


# ============================================================
# QUESTION 35 SCORES
# ============================================================

QUESTION_35_SCORES = {
    "q35_1": {"Emily": 1, "Sophie": 1, "Grace": 1, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q35_2": {"Emily": 1, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q35_3": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q35_4": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 36 SCORES
# ============================================================

QUESTION_36_SCORES = {
    "q36_1": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": -1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q36_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": -2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q36_3": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q36_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 4, "ECompatibility": 0, "SCompatibility": 20, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 37 SCORES
# ============================================================

QUESTION_37_SCORES = {
    "q37_1": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q37_2": {"Emily": 0, "Sophie": 0, "Grace": 1, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q37_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q37_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 20, "CCompatibility": 0},
}


# ============================================================
# QUESTION 38 SCORES
# ============================================================

QUESTION_38_SCORES = {
    "q38_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q38_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q38_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q38_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 20},
}


# ============================================================
# QUESTION 39 SCORES
# ============================================================

QUESTION_39_SCORES = {
    "q39_1": {"Emily": 1, "Sophie": 1, "Grace": 1, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q39_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": -2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q39_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q39_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 40 SCORES
# ============================================================

QUESTION_40_SCORES = {
    "q40_1": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 15, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q40_2": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 15, "GCompatibility": 0, "CCompatibility": 0},
    "q40_3": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
    "q40_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 15},
}


# ============================================================
# QUESTION 41 SCORES
# ============================================================

QUESTION_41_SCORES = {
    "q41_1": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q41_2": {"Emily": 1, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q41_3": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q41_4": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 15, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 42 SCORES
# ============================================================

QUESTION_42_SCORES = {
    "q42_1": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q42_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": -1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q42_3": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q42_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 15, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 43 SCORES
# ============================================================

QUESTION_43_SCORES = {
    "q43_1": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q43_2": {"Emily": 0, "Sophie": 0, "Grace": 1, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q43_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q43_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
}


# ============================================================
# QUESTION 44 SCORES
# ============================================================

QUESTION_44_SCORES = {
    "q44_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 2, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q44_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q44_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q44_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 15},
}


# ============================================================
# QUESTION 45 SCORES
# ============================================================

QUESTION_45_SCORES = {
    "q45_1": {"Emily": 2, "Sophie": 1, "Grace": 1, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q45_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q45_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q45_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 4, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 46 SCORES
# ============================================================

QUESTION_46_SCORES = {
    "q46_1": {"Emily": 3, "Sophie": 3, "Grace": 3, "Charlotte": 3, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q46_2": {"Emily": -1, "Sophie": -1, "Grace": -1, "Charlotte": -1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q46_3": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q46_4": {"Emily": 3, "Sophie": 3, "Grace": 3, "Charlotte": 3, "Honest": 4, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 47 SCORES
# ============================================================

QUESTION_47_SCORES = {
    "q47_1": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q47_2": {"Emily": -1, "Sophie": -1, "Grace": -1, "Charlotte": -1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q47_3": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q47_4": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 48 SCORES
# ============================================================

QUESTION_48_SCORES = {
    "q48_1": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 0, "Independence": -2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q48_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q48_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q48_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 4, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 49 SCORES
# ============================================================

QUESTION_49_SCORES = {
    "q49_1": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q49_2": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q49_3": {"Emily": 3, "Sophie": 3, "Grace": 3, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q49_4": {"Emily": 3, "Sophie": 3, "Grace": 3, "Charlotte": 3, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 50 SCORES
# ============================================================

QUESTION_50_SCORES = {
    "q50_1": {"Emily": 1, "Sophie": 1, "Grace": 1, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q50_2": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q50_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q50_4": {"Emily": 1, "Sophie": 1, "Grace": 1, "Charlotte": 1, "Honest": 3, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 51 SCORES
# ============================================================

QUESTION_51_SCORES = {
    "q51_1": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q51_2": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q51_3": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q51_4": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 3, "ECompatibility": 15, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 52 SCORES
# ============================================================

QUESTION_52_SCORES = {
    "q52_1": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q52_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q52_3": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q52_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 4, "ECompatibility": 0, "SCompatibility": 20, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 53 SCORES
# ============================================================

QUESTION_53_SCORES = {
    "q53_1": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q53_2": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q53_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q53_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 20, "CCompatibility": 0},
}


# ============================================================
# QUESTION 54 SCORES
# ============================================================

QUESTION_54_SCORES = {
    "q54_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 2, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q54_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q54_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q54_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 4, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 20},
}


# ============================================================
# QUESTION 55 SCORES
# ============================================================

QUESTION_55_SCORES = {
    "q55_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q55_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q55_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q55_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 4, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 56 SCORES
# ============================================================

QUESTION_56_SCORES = {
    "q56_1": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q56_2": {"Emily": 1, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q56_3": {"Emily": 2, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q56_4": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 15, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 57 SCORES
# ============================================================

QUESTION_57_SCORES = {
    "q57_1": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q57_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q57_3": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q57_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 15, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 58 SCORES
# ============================================================

QUESTION_58_SCORES = {
    "q58_1": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q58_2": {"Emily": 0, "Sophie": 0, "Grace": 1, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q58_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q58_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
}


# ============================================================
# QUESTION 59 SCORES
# ============================================================

QUESTION_59_SCORES = {
    "q59_1": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 0, "Independence": -1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q59_2": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q59_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 0, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q59_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 2, "Independence": 4, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 20},
}


# ============================================================
# QUESTION 60 SCORES
# ============================================================

QUESTION_60_SCORES = {
    "q60_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q60_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q60_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q60_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 4, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 61 SCORES
# ============================================================

QUESTION_61_SCORES = {
    "q61_1": {"Emily": 4, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q61_2": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q61_3": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q61_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 62 SCORES
# ============================================================

QUESTION_62_SCORES = {
    "q62_1": {"Emily": 3, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q62_2": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q62_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q62_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 63 SCORES
# ============================================================

QUESTION_63_SCORES = {
    "q63_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q63_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q63_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q63_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 4, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 64 SCORES
# ============================================================

QUESTION_64_SCORES = {
    "q64_1": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q64_2": {"Emily": 1, "Sophie": 1, "Grace": 1, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q64_3": {"Emily": 3, "Sophie": 3, "Grace": 3, "Charlotte": 3, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q64_4": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 1, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 65 SCORES
# ============================================================

QUESTION_65_SCORES = {
    "q65_1": {"Emily": 0, "Sophie": 3, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q65_2": {"Emily": 0, "Sophie": 1, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q65_3": {"Emily": 0, "Sophie": 2, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q65_4": {"Emily": 0, "Sophie": 4, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 10, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 66 SCORES
# ============================================================

QUESTION_66_SCORES = {
    "q66_1": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q66_2": {"Emily": 0, "Sophie": 0, "Grace": 2, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q66_3": {"Emily": 0, "Sophie": 0, "Grace": 3, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q66_4": {"Emily": 0, "Sophie": 0, "Grace": 4, "Charlotte": 0, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 15, "CCompatibility": 0},
}


# ============================================================
# QUESTION 67 SCORES
# ============================================================

QUESTION_67_SCORES = {
    "q67_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q67_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q67_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 3, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q67_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 4, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 15},
}


# ============================================================
# QUESTION 68 SCORES
# ============================================================

QUESTION_68_SCORES = {
    "q68_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 1, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q68_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 1, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q68_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q68_4": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 4, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 69 SCORES
# ============================================================

QUESTION_69_SCORES = {
    "q69_1": {"Emily": 4, "Sophie": 4, "Grace": 4, "Charlotte": 4, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q69_2": {"Emily": 1, "Sophie": 1, "Grace": 1, "Charlotte": 1, "Honest": 0, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q69_3": {"Emily": 3, "Sophie": 3, "Grace": 3, "Charlotte": 3, "Honest": 2, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q69_4": {"Emily": 3, "Sophie": 3, "Grace": 3, "Charlotte": 3, "Honest": 3, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
}


# ============================================================
# QUESTION 70 SCORES
# ============================================================

QUESTION_70_SCORES = {
    "q70_1": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q70_2": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 3, "Independence": 0, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q70_3": {"Emily": 0, "Sophie": 0, "Grace": 0, "Charlotte": 0, "Honest": 0, "Independence": 3, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
    "q70_4": {"Emily": 2, "Sophie": 2, "Grace": 2, "Charlotte": 2, "Honest": 2, "Independence": 2, "ECompatibility": 0, "SCompatibility": 0, "GCompatibility": 0, "CCompatibility": 0},
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
    "Daniel Carter is seventeen and has just transferred to Westbridge High "
    "after his family moved to the area.\n\n"
    "He isn’t particularly popular, athletic, or academically brilliant. "
    "What makes him unusual is that he listens carefully to people.\n\n"
    "Unfortunately, Daniel also has a habit of avoiding difficult decisions. "
    "His greatest fear isn’t failure. It’s choosing something—and discovering "
    "later that he chose wrong.\n\n"
    "You play as Daniel."
)

bot.send_message(
    message.chat.id,
    "Daniel arrived at Westbridge High on a rainy Monday morning.\n"
    "He stood outside the main entrance holding a piece of paper with his classroom\n"
    "number.\n"
    "The paper was already wet.\n"
    "“Brilliant.”\n"
    "Someone behind him laughed.\n"
    "Daniel turned.\n"
    "A girl with blonde hair was standing beneath an umbrella.\n"
    "“First day?”\n"
    "“Is it that obvious?”\n"
    "“You’re holding the map upside down.”\n"
    "Daniel looked down.\n"
    "She was right.\n"
    "“Oh.”\n"
    "She smiled.\n"
    "“Sophie Williams.”\n"
    "“Daniel Carter.”\n"
    "“Come on, Daniel Carter. I’ll show you where you’re going.”\n"
    "Before Daniel could respond, another girl approached.\n"
    "“You’re Daniel, aren’t you?”\n"
    "She was carrying several folders.\n"
    "“Emily Parker. Student council.”\n"
    "Daniel nodded.\n"
    "“Yes.”\n"
    "“Good. I was told to make sure you know where everything is.”\n"
    "Sophie raised an eyebrow.\n"
    "“I already found him.”\n"
    "Emily smiled politely.\n"
    "“Then you’ve saved me a job.”\n"
    "A third girl walked past them carrying several books.\n"
    "One slipped from her hands.\n"
    "Daniel picked it up.\n"
    "“Thanks.”\n"
    "She looked at the cover.\n"
    "“That’s mine.”\n"
    "“Sorry.”\n"
    "“It’s okay.”\n"
    "She took it.\n"
    "“Grace Bennett.”\n"
    "Then she disappeared into the building.\n"
    "Daniel watched her leave.\n"
    "Sophie waved a hand in front of his face.\n"
    "“Earth to Daniel.”\n"
    "“What?”\n"
    "“You’re going to be fine here.”\n"
    "A fourth girl walked through the entrance.\n"
    "Charlotte Reed.\n"
    "She glanced at the group.\n"
    "“You’re blocking the doorway.”\n"
    "Sophie laughed.\n"
    "“Good morning to you too, Charlotte.”\n"
    "Charlotte sighed.\n"
    "“Good morning.”\n"
    "Then she walked inside.\n"
    "Daniel looked at the four girls.\n"
    "He had been at Westbridge High for less than ten minutes.\n"
    "Already, he suspected the year would be complicated."
)

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 1
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully to Daniel's answer.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

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

    try:
        response = requests.get(
            IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        print("Question 2 image status:", response.status_code)
        print(
            "Question 2 image type:",
            response.headers.get("Content-Type")
        )

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

#سؤال 3
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
        "Grace joins Daniel and Sophie and asks Daniel "
        "how he feels about working with other students "
        "on a difficult project."
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

    try:
        response = requests.get(
            IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        print("Question 3 image status:", response.status_code)
        print(
            "Question 3 image type:",
            response.headers.get("Content-Type")
        )

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

#سؤال 4

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
        "Charlotte joins the conversation and asks Daniel "
        "what he would do when faced with an important decision."
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

    try:
        response = requests.get(
            IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        print("Question 4 image status:", response.status_code)
        print(
            "Question 4 image type:",
            response.headers.get("Content-Type")
        )

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
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

#سؤال 5
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

    try:
        response = requests.get(
            IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        print("Question 5 image status:", response.status_code)
        print(
            "Question 5 image type:",
            response.headers.get("Content-Type")
        )

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
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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


#سؤال 6

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

    try:
        response = requests.get(
            IMAGE_URL,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        print("Question 6 image status:", response.status_code)
        print(
            "Question 6 image type:",
            response.headers.get("Content-Type")
        )

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
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    send_question_7(call.message.chat.id)

#سؤال 7

# ============================================================
# QUESTION 7
# ============================================================

def send_question_7(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 7
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "After talking with Sophie, Daniel continues "
        "the conversation with Grace.\n\n"
        "Grace asks Daniel how he would react if he "
        "had to take responsibility for an important task."
    )

    # --------------------------------------------------------
    # QUESTION 7 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd take responsibility and get started.",
            callback_data="q7_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd ask someone else to handle it.",
            callback_data="q7_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd do it, but I'd want some guidance.",
            callback_data="q7_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd first make sure I understood everything.",
            callback_data="q7_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 7 IMAGE
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

        print("Question 7 image status:", response.status_code)
        print(
            "Question 7 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question7.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 7 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 7 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Grace asks Daniel how he would react if he "
        "had to take responsibility for an important task.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 7 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q7_")
)
def question_7_answer(call):

    answers = {
        "q7_1": "I'd take responsibility and get started.",
        "q7_2": "I'd ask someone else to handle it.",
        "q7_3": "I'd do it, but I'd want some guidance.",
        "q7_4": "I'd first make sure I understood everything."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 7 POINTS
    # --------------------------------------------------------

    points = QUESTION_7_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 7
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Grace thinks about Daniel's response.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_8(call.message.chat.id)


#سؤال 8 

# ============================================================
# QUESTION 8
# ============================================================

def send_question_8(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 8
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "After talking with Grace, Daniel continues "
        "the conversation with Charlotte.\n\n"
        "Charlotte asks Daniel what he would do if "
        "a friend came to him with a difficult problem."
    )

    # --------------------------------------------------------
    # QUESTION 8 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd help them right away.",
            callback_data="q8_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd encourage them to solve it themselves.",
            callback_data="q8_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd help them if I had enough time.",
            callback_data="q8_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd ask what kind of help they need first.",
            callback_data="q8_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 8 IMAGE
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

        print("Question 8 image status:", response.status_code)
        print(
            "Question 8 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question8.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 8 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 8 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Charlotte asks Daniel what he would do if "
        "a friend came to him with a difficult problem.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 8 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q8_")
)
def question_8_answer(call):

    answers = {
        "q8_1": "I'd help them right away.",
        "q8_2": "I'd encourage them to solve it themselves.",
        "q8_3": "I'd help them if I had enough time.",
        "q8_4": "I'd ask what kind of help they need first."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 8 POINTS
    # --------------------------------------------------------

    points = QUESTION_8_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 8
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Charlotte thinks about Daniel's response.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_9(call.message.chat.id)

#سؤال 9

# ============================================================
# QUESTION 9
# ============================================================

def send_question_9(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 9
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "After talking with Charlotte, Daniel continues "
        "the conversation with Emily.\n\n"
        "Emily asks Daniel what he would do if he noticed "
        "that someone was being treated unfairly."
    )

    # --------------------------------------------------------
    # QUESTION 9 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd speak up and say something.",
            callback_data="q9_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd stay out of it.",
            callback_data="q9_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd try to help the person privately.",
            callback_data="q9_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd first find out what happened.",
            callback_data="q9_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 9 IMAGE
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

        print("Question 9 image status:", response.status_code)
        print(
            "Question 9 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question9.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 9 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 9 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would do if he noticed "
        "that someone was being treated unfairly.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 9 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q9_")
)
def question_9_answer(call):

    answers = {
        "q9_1": "I'd speak up and say something.",
        "q9_2": "I'd stay out of it.",
        "q9_3": "I'd try to help the person privately.",
        "q9_4": "I'd first find out what happened."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 9 POINTS
    # --------------------------------------------------------

    points = QUESTION_9_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 9
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily thinks about Daniel's response.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_10(call.message.chat.id)


#سؤال 10

# ============================================================
# QUESTION 10
# ============================================================

def send_question_10(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 10
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "After talking with Charlotte, Daniel continues "
        "the conversation with Emily.\n\n"
        "Emily asks Daniel how he would react if he made "
        "a mistake while working on something important."
    )

    # --------------------------------------------------------
    # QUESTION 10 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd admit the mistake and try to fix it.",
            callback_data="q10_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd try to fix it on my own first.",
            callback_data="q10_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd ask someone I trust for advice.",
            callback_data="q10_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd think carefully about what went wrong.",
            callback_data="q10_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 10 IMAGE
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

        print("Question 10 image status:", response.status_code)
        print(
            "Question 10 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question10.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 10 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 10 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel how he would react if he made "
        "a mistake while working on something important.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 10 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q10_")
)
def question_10_answer(call):

    answers = {
        "q10_1": "I'd admit the mistake and try to fix it.",
        "q10_2": "I'd try to fix it on my own first.",
        "q10_3": "I'd ask someone I trust for advice.",
        "q10_4": "I'd think carefully about what went wrong."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 10 POINTS
    # --------------------------------------------------------

    points = QUESTION_10_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 10
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily thinks about Daniel's response.\n\n"
        "The conversation continues..."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_11(call.message.chat.id)

#سؤال 11 

# ============================================================
# QUESTION 11
# ============================================================

def send_question_11(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 11
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "The conversation continues with Emily.\n\n"
        "Emily asks Daniel what he usually does when "
        "he has to make an important decision."
    )

    # --------------------------------------------------------
    # QUESTION 11 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I listen to my feelings and trust my instincts.",
            callback_data="q11_1"
        ),
        types.InlineKeyboardButton(
            "2. I prefer to make the decision by myself.",
            callback_data="q11_2"
        ),
        types.InlineKeyboardButton(
            "3. I talk to someone I trust before deciding.",
            callback_data="q11_3"
        ),
        types.InlineKeyboardButton(
            "4. I take my time and carefully consider everything.",
            callback_data="q11_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 11 IMAGE
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

        print("Question 11 image status:", response.status_code)
        print(
            "Question 11 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question11.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 11 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 11 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he usually does when "
        "he has to make an important decision.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 11 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q11_")
)
def question_11_answer(call):

    answers = {
        "q11_1": "I listen to my feelings and trust my instincts.",
        "q11_2": "I prefer to make the decision by myself.",
        "q11_3": "I talk to someone I trust before deciding.",
        "q11_4": "I take my time and carefully consider everything."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 11 POINTS
    # --------------------------------------------------------

    points = QUESTION_11_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 11
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully to Daniel's answer.\n\n"
        "She feels that she is beginning to understand "
        "him a little better."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_12(call.message.chat.id)

#سؤال 12

# ============================================================
# QUESTION 12
# ============================================================

def send_question_12(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 12
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles and continues talking with Daniel.\n\n"
        "She asks him what he values most when building "
        "a close relationship with someone."
    )

    # --------------------------------------------------------
    # QUESTION 12 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Honesty, even when the truth is difficult.",
            callback_data="q12_1"
        ),
        types.InlineKeyboardButton(
            "2. Having enough freedom to be myself.",
            callback_data="q12_2"
        ),
        types.InlineKeyboardButton(
            "3. Trust and being able to rely on each other.",
            callback_data="q12_3"
        ),
        types.InlineKeyboardButton(
            "4. Taking time to understand each other deeply.",
            callback_data="q12_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 12 IMAGE
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

        print("Question 12 image status:", response.status_code)
        print(
            "Question 12 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question12.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 12 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 12 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he values most when "
        "building a close relationship with someone.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 12 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q12_")
)
def question_12_answer(call):

    answers = {
        "q12_1": "Honesty, even when the truth is difficult.",
        "q12_2": "Having enough freedom to be myself.",
        "q12_3": "Trust and being able to rely on each other.",
        "q12_4": "Taking time to understand each other deeply."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 12 POINTS
    # --------------------------------------------------------

    points = QUESTION_12_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 12
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully at Daniel's answer.\n\n"
        "She feels that the conversation is becoming "
        "more personal."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_13(call.message.chat.id)

#سؤال 13

# ============================================================
# QUESTION 13
# ============================================================

def send_question_13(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 13
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily becomes curious about Daniel's personality.\n\n"
        "She asks him what he would do if someone close to him "
        "was having a difficult day."
    )

    # --------------------------------------------------------
    # QUESTION 13 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd listen honestly and let them know they can trust me.",
            callback_data="q13_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd give them some space and let them handle it.",
            callback_data="q13_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd stay with them and try to support them.",
            callback_data="q13_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd ask questions and try to understand what they're feeling.",
            callback_data="q13_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 13 IMAGE
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

        print("Question 13 image status:", response.status_code)
        print(
            "Question 13 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question13.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 13 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 13 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would do if someone "
        "close to him was having a difficult day.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 13 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q13_")
)
def question_13_answer(call):

    answers = {
        "q13_1": "I'd listen honestly and let them know they can trust me.",
        "q13_2": "I'd give them some space and let them handle it.",
        "q13_3": "I'd stay with them and try to support them.",
        "q13_4": "I'd ask questions and try to understand what they're feeling."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 13 POINTS
    # --------------------------------------------------------

    points = QUESTION_13_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 13
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily appreciates Daniel's answer.\n\n"
        "She feels that his response reveals something "
        "important about the way he treats people close to him."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_14(call.message.chat.id)


#سؤال 14

# ============================================================
# QUESTION 14
# ============================================================

def send_question_14(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 14
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily thinks about Daniel's answer and smiles.\n\n"
        "She asks him what he would most enjoy doing "
        "with someone he really likes spending time with."
    )

    # --------------------------------------------------------
    # QUESTION 14 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Having an honest conversation somewhere quiet.",
            callback_data="q14_1"
        ),
        types.InlineKeyboardButton(
            "2. Doing something independently, but enjoying the time together.",
            callback_data="q14_2"
        ),
        types.InlineKeyboardButton(
            "3. Going somewhere fun and making good memories together.",
            callback_data="q14_3"
        ),
        types.InlineKeyboardButton(
            "4. Taking a walk and talking about life and our goals.",
            callback_data="q14_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 14 IMAGE
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

        print("Question 14 image status:", response.status_code)
        print(
            "Question 14 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question14.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 14 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 14 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would most enjoy doing "
        "with someone he really likes spending time with.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 14 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q14_")
)
def question_14_answer(call):

    answers = {
        "q14_1": "Having an honest conversation somewhere quiet.",
        "q14_2": "Doing something independently, but enjoying the time together.",
        "q14_3": "Going somewhere fun and making good memories together.",
        "q14_4": "Taking a walk and talking about life and our goals."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 14 POINTS
    # --------------------------------------------------------

    points = QUESTION_14_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 14
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily laughs softly at Daniel's answer.\n\n"
        "The conversation feels easier now, and she is "
        "curious to learn even more about him."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_15(call.message.chat.id)

#سؤال 15

# ============================================================
# QUESTION 15
# ============================================================

def send_question_15(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 15
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily feels comfortable talking with Daniel now.\n\n"
        "She asks him what he thinks makes a relationship "
        "strong over time."
    )

    # --------------------------------------------------------
    # QUESTION 15 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being completely honest with each other.",
            callback_data="q15_1"
        ),
        types.InlineKeyboardButton(
            "2. Respecting each other's independence and choices.",
            callback_data="q15_2"
        ),
        types.InlineKeyboardButton(
            "3. Supporting each other through good and difficult times.",
            callback_data="q15_3"
        ),
        types.InlineKeyboardButton(
            "4. Communicating patiently and understanding each other.",
            callback_data="q15_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 15 IMAGE
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

        print("Question 15 image status:", response.status_code)
        print(
            "Question 15 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question15.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 15 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 15 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks makes a relationship "
        "strong over time.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 15 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q15_")
)
def question_15_answer(call):

    answers = {
        "q15_1": "Being completely honest with each other.",
        "q15_2": "Respecting each other's independence and choices.",
        "q15_3": "Supporting each other through good and difficult times.",
        "q15_4": "Communicating patiently and understanding each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 15 POINTS
    # --------------------------------------------------------

    points = QUESTION_15_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 15
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles after hearing Daniel's answer.\n\n"
        "She feels that their conversation is becoming "
        "more meaningful."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_16(call.message.chat.id)

#سؤال 16 

# ============================================================
# QUESTION 16
# ============================================================

def send_question_16(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 16
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily pauses for a moment before asking another question.\n\n"
        "She asks Daniel what he would do if someone he cared "
        "about disagreed strongly with him."
    )

    # --------------------------------------------------------
    # QUESTION 16 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd be honest about my opinion, but stay respectful.",
            callback_data="q16_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd give them space and let them have their own opinion.",
            callback_data="q16_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd try to find a compromise that works for both of us.",
            callback_data="q16_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd listen carefully and try to understand their point of view.",
            callback_data="q16_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 16 IMAGE
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

        print("Question 16 image status:", response.status_code)
        print(
            "Question 16 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question16.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 16 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 16 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would do if someone he cared "
        "about disagreed strongly with him.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 16 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q16_")
)
def question_16_answer(call):

    answers = {
        "q16_1": "I'd be honest about my opinion, but stay respectful.",
        "q16_2": "I'd give them space and let them have their own opinion.",
        "q16_3": "I'd try to find a compromise that works for both of us.",
        "q16_4": "I'd listen carefully and try to understand their point of view."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 16 POINTS
    # --------------------------------------------------------

    points = QUESTION_16_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 16
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully to Daniel's answer.\n\n"
        "She appreciates the way he thinks about disagreements "
        "and what they can reveal about two people."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_17(call.message.chat.id)

#سؤال 17 

# ============================================================
# QUESTION 17
# ============================================================

def send_question_17(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 17
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles and continues the conversation.\n\n"
        "She asks Daniel what kind of moment makes him feel "
        "most connected to someone."
    )

    # --------------------------------------------------------
    # QUESTION 17 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. When we can speak honestly about anything.",
            callback_data="q17_1"
        ),
        types.InlineKeyboardButton(
            "2. When we can enjoy being together without feeling restricted.",
            callback_data="q17_2"
        ),
        types.InlineKeyboardButton(
            "3. When we help and support each other.",
            callback_data="q17_3"
        ),
        types.InlineKeyboardButton(
            "4. When we have a deep conversation and really understand each other.",
            callback_data="q17_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 17 IMAGE
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

        print("Question 17 image status:", response.status_code)
        print(
            "Question 17 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question17.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 17 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 17 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what kind of moment makes him feel "
        "most connected to someone.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 17 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q17_")
)
def question_17_answer(call):

    answers = {
        "q17_1": "When we can speak honestly about anything.",
        "q17_2": "When we can enjoy being together without feeling restricted.",
        "q17_3": "When we help and support each other.",
        "q17_4": "When we have a deep conversation and really understand each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 17 POINTS
    # --------------------------------------------------------

    points = QUESTION_17_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 17
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily looks thoughtful after hearing Daniel's answer.\n\n"
        "She feels that she is getting closer to understanding "
        "what kind of connection Daniel is looking for."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_18(call.message.chat.id)

#سؤال 18
# ============================================================
# QUESTION 18
# ============================================================

def send_question_18(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 18
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily has enjoyed getting to know Daniel through their "
        "conversation.\n\n"
        "She asks him what he would do if someone he cared about "
        "needed help with an important problem."
    )

    # --------------------------------------------------------
    # QUESTION 18 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd be honest with them and tell them what I really think.",
            callback_data="q18_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd encourage them to handle it themselves if they can.",
            callback_data="q18_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd offer my help and stay by their side.",
            callback_data="q18_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd listen carefully and help them think through the problem.",
            callback_data="q18_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 18 IMAGE
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

        print("Question 18 image status:", response.status_code)
        print(
            "Question 18 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question18.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 18 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 18 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would do if someone he cared "
        "about needed help with an important problem.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 18 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q18_")
)
def question_18_answer(call):

    answers = {
        "q18_1": "I'd be honest with them and tell them what I really think.",
        "q18_2": "I'd encourage them to handle it themselves if they can.",
        "q18_3": "I'd offer my help and stay by their side.",
        "q18_4": "I'd listen carefully and help them think through the problem."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 18 POINTS
    # --------------------------------------------------------

    points = QUESTION_18_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 18
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods after hearing Daniel's answer.\n\n"
        "She appreciates learning how he responds when "
        "someone important to him needs support."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_19(call.message.chat.id)

#سؤال19
# ============================================================
# QUESTION 19
# ============================================================

def send_question_19(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 19
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a curious smile.\n\n"
        "She asks him what he thinks is the best way to "
        "keep a relationship interesting over time."
    )

    # --------------------------------------------------------
    # QUESTION 19 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Always being honest and sharing what is on your mind.",
            callback_data="q19_1"
        ),
        types.InlineKeyboardButton(
            "2. Giving each other freedom to have separate interests.",
            callback_data="q19_2"
        ),
        types.InlineKeyboardButton(
            "3. Trying new things and creating fun memories together.",
            callback_data="q19_3"
        ),
        types.InlineKeyboardButton(
            "4. Having meaningful conversations and learning more about each other.",
            callback_data="q19_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 19 IMAGE
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

        print("Question 19 image status:", response.status_code)
        print(
            "Question 19 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question19.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 19 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 19 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "keep a relationship interesting over time.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 19 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q19_")
)
def question_19_answer(call):

    answers = {
        "q19_1": "Always being honest and sharing what is on your mind.",
        "q19_2": "Giving each other freedom to have separate interests.",
        "q19_3": "Trying new things and creating fun memories together.",
        "q19_4": "Having meaningful conversations and learning more about each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 19 POINTS
    # --------------------------------------------------------

    points = QUESTION_19_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 19
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles at Daniel's answer.\n\n"
        "She feels that every question is revealing "
        "another side of his personality."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_20(call.message.chat.id)

#سؤال 20
# ============================================================
# QUESTION 20
# ============================================================

def send_question_20(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 20
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily has enjoyed their conversation so far.\n\n"
        "She asks Daniel what he would most want someone "
        "close to him to understand about his personality."
    )

    # --------------------------------------------------------
    # QUESTION 20 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. That I always try to be honest about who I am.",
            callback_data="q20_1"
        ),
        types.InlineKeyboardButton(
            "2. That I need my own space and independence.",
            callback_data="q20_2"
        ),
        types.InlineKeyboardButton(
            "3. That I care deeply about the people close to me.",
            callback_data="q20_3"
        ),
        types.InlineKeyboardButton(
            "4. That I may take time to open up, but I value deep connections.",
            callback_data="q20_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 20 IMAGE
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

        print("Question 20 image status:", response.status_code)
        print(
            "Question 20 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question20.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 20 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 20 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would most want someone "
        "close to him to understand about his personality.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 20 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q20_")
)
def question_20_answer(call):

    answers = {
        "q20_1": "That I always try to be honest about who I am.",
        "q20_2": "That I need my own space and independence.",
        "q20_3": "That I care deeply about the people close to me.",
        "q20_4": "That I may take time to open up, but I value deep connections."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 20 POINTS
    # --------------------------------------------------------

    points = QUESTION_20_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 20
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily is quiet for a moment after hearing Daniel's answer.\n\n"
        "She feels that she now understands him much better "
        "than when their conversation first began."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_21(call.message.chat.id)

#سؤال21
# ============================================================
# QUESTION 21
# ============================================================

def send_question_21(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 21
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles as the conversation continues.\n\n"
        "She asks Daniel what he thinks is most important "
        "when two people are trying to build trust."
    )

    # --------------------------------------------------------
    # QUESTION 21 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Always telling the truth, even when it is uncomfortable.",
            callback_data="q21_1"
        ),
        types.InlineKeyboardButton(
            "2. Respecting each other's boundaries and personal space.",
            callback_data="q21_2"
        ),
        types.InlineKeyboardButton(
            "3. Showing through actions that you can be relied on.",
            callback_data="q21_3"
        ),
        types.InlineKeyboardButton(
            "4. Communicating openly and giving each other time to feel comfortable.",
            callback_data="q21_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 21 IMAGE
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

        print("Question 21 image status:", response.status_code)
        print(
            "Question 21 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question21.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 21 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 21 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is most important "
        "when two people are trying to build trust.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 21 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q21_")
)
def question_21_answer(call):

    answers = {
        "q21_1": "Always telling the truth, even when it is uncomfortable.",
        "q21_2": "Respecting each other's boundaries and personal space.",
        "q21_3": "Showing through actions that you can be relied on.",
        "q21_4": "Communicating openly and giving each other time to feel comfortable."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 21 POINTS
    # --------------------------------------------------------

    points = QUESTION_21_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 21
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She realizes that Daniel has a clear idea of what "
        "trust means to him."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_22(call.message.chat.id)

#سؤال 22
# ============================================================
# QUESTION 22
# ============================================================

def send_question_22(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 22
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel and smiles.\n\n"
        "She asks him what he would enjoy most on a relaxed "
        "day with someone he feels close to."
    )

    # --------------------------------------------------------
    # QUESTION 22 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Sitting somewhere quiet and having a long conversation.",
            callback_data="q22_1"
        ),
        types.InlineKeyboardButton(
            "2. Spending some time together while still doing our own things.",
            callback_data="q22_2"
        ),
        types.InlineKeyboardButton(
            "3. Going somewhere fun and enjoying the day together.",
            callback_data="q22_3"
        ),
        types.InlineKeyboardButton(
            "4. Taking a peaceful walk and talking about our future.",
            callback_data="q22_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 22 IMAGE
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

        print("Question 22 image status:", response.status_code)
        print(
            "Question 22 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question22.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 22 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 22 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would enjoy most on a relaxed "
        "day with someone he feels close to.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 22 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q22_")
)
def question_22_answer(call):

    answers = {
        "q22_1": "Sitting somewhere quiet and having a long conversation.",
        "q22_2": "Spending some time together while still doing our own things.",
        "q22_3": "Going somewhere fun and enjoying the day together.",
        "q22_4": "Taking a peaceful walk and talking about our future."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 22 POINTS
    # --------------------------------------------------------

    points = QUESTION_22_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 22
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily laughs softly and says that sounds like "
        "a good way to spend a day.\n\n"
        "The conversation continues, and she has one more "
        "thing she wants to ask Daniel."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_23(call.message.chat.id)

#سؤال 23
# ============================================================
# QUESTION 23
# ============================================================

def send_question_23(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 23
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks thoughtful for a moment.\n\n"
        "She asks Daniel what he thinks people should do "
        "when a relationship starts becoming difficult."
    )

    # --------------------------------------------------------
    # QUESTION 23 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be completely honest about what is going wrong.",
            callback_data="q23_1"
        ),
        types.InlineKeyboardButton(
            "2. Give each other some space before talking again.",
            callback_data="q23_2"
        ),
        types.InlineKeyboardButton(
            "3. Work together and support each other through it.",
            callback_data="q23_3"
        ),
        types.InlineKeyboardButton(
            "4. Talk calmly and try to understand both sides.",
            callback_data="q23_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 23 IMAGE
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

        print("Question 23 image status:", response.status_code)
        print(
            "Question 23 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question23.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 23 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 23 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks people should do "
        "when a relationship starts becoming difficult.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 23 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q23_")
)
def question_23_answer(call):

    answers = {
        "q23_1": "Be completely honest about what is going wrong.",
        "q23_2": "Give each other some space before talking again.",
        "q23_3": "Work together and support each other through it.",
        "q23_4": "Talk calmly and try to understand both sides."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 23 POINTS
    # --------------------------------------------------------

    points = QUESTION_23_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 23
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods slowly at Daniel's answer.\n\n"
        "She likes that the conversation has become honest "
        "and thoughtful."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_24(call.message.chat.id)

#سؤال 24
# ============================================================
# QUESTION 24
# ============================================================

def send_question_24(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 24
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles and looks at Daniel thoughtfully.\n\n"
        "She asks him what quality he notices first when "
        "he meet someone new."
    )

    # --------------------------------------------------------
    # QUESTION 24 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. How honest and genuine they seem.",
            callback_data="q24_1"
        ),
        types.InlineKeyboardButton(
            "2. How confident and independent they are.",
            callback_data="q24_2"
        ),
        types.InlineKeyboardButton(
            "3. How kind and caring they are toward others.",
            callback_data="q24_3"
        ),
        types.InlineKeyboardButton(
            "4. How thoughtful and easy they are to talk to.",
            callback_data="q24_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 24 IMAGE
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

        print("Question 24 image status:", response.status_code)
        print(
            "Question 24 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question24.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 24 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 24 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what quality he notices first when "
        "he meets someone new.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 24 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q24_")
)
def question_24_answer(call):

    answers = {
        "q24_1": "How honest and genuine they seem.",
        "q24_2": "How confident and independent they are.",
        "q24_3": "How kind and caring they are toward others.",
        "q24_4": "How thoughtful and easy they are to talk to."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 24 POINTS
    # --------------------------------------------------------

    points = QUESTION_24_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 24
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles at Daniel's answer.\n\n"
        "She realizes that first impressions can reveal "
        "a lot about what someone values."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_25(call.message.chat.id)

#سؤال 25

# ============================================================
# QUESTION 25
# ============================================================

def send_question_25(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 25
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily has one more question on her mind.\n\n"
        "She asks Daniel what would make him feel truly "
        "comfortable with someone over time."
    )

    # --------------------------------------------------------
    # QUESTION 25 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Knowing that we can always be honest with each other.",
            callback_data="q25_1"
        ),
        types.InlineKeyboardButton(
            "2. Knowing that we respect each other's independence.",
            callback_data="q25_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing that we can always count on each other.",
            callback_data="q25_3"
        ),
        types.InlineKeyboardButton(
            "4. Knowing that we can talk openly without being judged.",
            callback_data="q25_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 25 IMAGE
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

        print("Question 25 image status:", response.status_code)
        print(
            "Question 25 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question25.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 25 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 25 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what would make him feel truly "
        "comfortable with someone over time.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 25 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q25_")
)
def question_25_answer(call):

    answers = {
        "q25_1": "Knowing that we can always be honest with each other.",
        "q25_2": "Knowing that we respect each other's independence.",
        "q25_3": "Knowing that we can always count on each other.",
        "q25_4": "Knowing that we can talk openly without being judged."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 25 POINTS
    # --------------------------------------------------------

    points = QUESTION_25_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 25
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly after Daniel's answer.\n\n"
        "She feels that their conversation has revealed "
        "a lot about what matters to him."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_26(call.message.chat.id)

#سؤال 26

# ============================================================
# QUESTION 26
# ============================================================

def send_question_26(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 26
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a thoughtful smile.\n\n"
        "She asks him what he thinks is the best way to "
        "show someone that they are important to you."
    )

    # --------------------------------------------------------
    # QUESTION 26 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Tell them honestly how much they mean to you.",
            callback_data="q26_1"
        ),
        types.InlineKeyboardButton(
            "2. Respect their needs and give them room to be themselves.",
            callback_data="q26_2"
        ),
        types.InlineKeyboardButton(
            "3. Be there for them whenever they need support.",
            callback_data="q26_3"
        ),
        types.InlineKeyboardButton(
            "4. Make time to listen and understand what matters to them.",
            callback_data="q26_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 26 IMAGE
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

        print("Question 26 image status:", response.status_code)
        print(
            "Question 26 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question26.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 26 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 26 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "show someone that they are important to you.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 26 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q26_")
)
def question_26_answer(call):

    answers = {
        "q26_1": "Tell them honestly how much they mean to you.",
        "q26_2": "Respect their needs and give them room to be themselves.",
        "q26_3": "Be there for them whenever they need support.",
        "q26_4": "Make time to listen and understand what matters to them."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 26 POINTS
    # --------------------------------------------------------

    points = QUESTION_26_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 26
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully and smiles.\n\n"
        "She feels that Daniel's answer says a lot about "
        "how he expresses care and affection."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_27(call.message.chat.id)

#سؤال 27
# ============================================================
# QUESTION 27
# ============================================================

def send_question_27(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 27
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily thinks about everything Daniel has shared so far.\n\n"
        "She asks him what he would value most in a person "
        "he could build a long-term relationship with."
    )

    # --------------------------------------------------------
    # QUESTION 27 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Someone who is honest and never hides their true feelings.",
            callback_data="q27_1"
        ),
        types.InlineKeyboardButton(
            "2. Someone who has their own goals and respects my independence.",
            callback_data="q27_2"
        ),
        types.InlineKeyboardButton(
            "3. Someone loyal who will stand by me through difficult times.",
            callback_data="q27_3"
        ),
        types.InlineKeyboardButton(
            "4. Someone patient who wants to understand me deeply.",
            callback_data="q27_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 27 IMAGE
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

        print("Question 27 image status:", response.status_code)
        print(
            "Question 27 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question27.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 27 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 27 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would value most in a person "
        "he could build a long-term relationship with.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 27 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q27_")
)
def question_27_answer(call):

    answers = {
        "q27_1": "Someone who is honest and never hides their true feelings.",
        "q27_2": "Someone who has their own goals and respects my independence.",
        "q27_3": "Someone loyal who will stand by me through difficult times.",
        "q27_4": "Someone patient who wants to understand me deeply."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 27 POINTS
    # --------------------------------------------------------

    points = QUESTION_27_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 27
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles after hearing Daniel's answer.\n\n"
        "She is beginning to see which qualities Daniel "
        "would value most in a serious relationship."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_28(call.message.chat.id)

#سؤال 28

# ============================================================
# QUESTION 28
# ============================================================

def send_question_28(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 28
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel and asks one more personal question.\n\n"
        "She wants to know what makes him feel most appreciated "
        "by someone he cares about."
    )

    # --------------------------------------------------------
    # QUESTION 28 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. When they tell me honestly that they appreciate me.",
            callback_data="q28_1"
        ),
        types.InlineKeyboardButton(
            "2. When they respect my choices and give me room to be myself.",
            callback_data="q28_2"
        ),
        types.InlineKeyboardButton(
            "3. When they notice my efforts and support me.",
            callback_data="q28_3"
        ),
        types.InlineKeyboardButton(
            "4. When they take the time to understand me and remember the little things.",
            callback_data="q28_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 28 IMAGE
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

        print("Question 28 image status:", response.status_code)
        print(
            "Question 28 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question28.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 28 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 28 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what makes him feel most appreciated "
        "by someone he cares about.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 28 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q28_")
)
def question_28_answer(call):

    answers = {
        "q28_1": "When they tell me honestly that they appreciate me.",
        "q28_2": "When they respect my choices and give me room to be myself.",
        "q28_3": "When they notice my efforts and support me.",
        "q28_4": "When they take the time to understand me and remember the little things."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 28 POINTS
    # --------------------------------------------------------

    points = QUESTION_28_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 28
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly at Daniel's answer.\n\n"
        "She feels that she is getting a clearer picture "
        "of what makes him feel valued and understood."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_29(call.message.chat.id)

#سؤال 29

# ============================================================
# QUESTION 29
# ============================================================

def send_question_29(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 29
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily pauses and thinks about their conversation.\n\n"
        "She asks Daniel what he would do to make someone "
        "he cares about feel secure in their relationship."
    )

    # --------------------------------------------------------
    # QUESTION 29 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd always be honest and never hide important things.",
            callback_data="q29_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd respect their independence and never try to control them.",
            callback_data="q29_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd be dependable and show them they can count on me.",
            callback_data="q29_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd communicate openly and make sure they feel heard.",
            callback_data="q29_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 29 IMAGE
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

        print("Question 29 image status:", response.status_code)
        print(
            "Question 29 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question29.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 29 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 29 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would do to make someone "
        "he cares about feel secure in their relationship.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 29 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q29_")
)
def question_29_answer(call):

    answers = {
        "q29_1": "I'd always be honest and never hide important things.",
        "q29_2": "I'd respect their independence and never try to control them.",
        "q29_3": "I'd be dependable and show them they can count on me.",
        "q29_4": "I'd communicate openly and make sure they feel heard."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 29 POINTS
    # --------------------------------------------------------

    points = QUESTION_29_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 29
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully after Daniel's answer.\n\n"
        "She feels that his answer shows what he believes "
        "makes a relationship feel safe and comfortable."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_30(call.message.chat.id)

#سؤال 30

# ============================================================
# QUESTION 30
# ============================================================

def send_question_30(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 30
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles as she realizes how much they have talked about.\n\n"
        "She asks Daniel what he thinks is most important "
        "for two people who want to build a future together."
    )

    # --------------------------------------------------------
    # QUESTION 30 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about your hopes, feelings, and plans.",
            callback_data="q30_1"
        ),
        types.InlineKeyboardButton(
            "2. Supporting each other's individual goals and dreams.",
            callback_data="q30_2"
        ),
        types.InlineKeyboardButton(
            "3. Staying loyal and being there for each other.",
            callback_data="q30_3"
        ),
        types.InlineKeyboardButton(
            "4. Communicating openly and making important decisions together.",
            callback_data="q30_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 30 IMAGE
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

        print("Question 30 image status:", response.status_code)
        print(
            "Question 30 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question30.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 30 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 30 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is most important "
        "for two people who want to build a future together.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 30 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q30_")
)
def question_30_answer(call):

    answers = {
        "q30_1": "Being honest about your hopes, feelings, and plans.",
        "q30_2": "Supporting each other's individual goals and dreams.",
        "q30_3": "Staying loyal and being there for each other.",
        "q30_4": "Communicating openly and making important decisions together."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 30 POINTS
    # --------------------------------------------------------

    points = QUESTION_30_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 30
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily becomes quiet for a moment and smiles.\n\n"
        "She feels that Daniel has shared a lot about "
        "what he wants from a meaningful relationship."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_31(call.message.chat.id)

#سؤال 31

# ============================================================
# QUESTION 31
# ============================================================

def send_question_31(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 31
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a warm smile.\n\n"
        "She asks him what kind of moment would make him "
        "feel especially happy in a relationship."
    )

    # --------------------------------------------------------
    # QUESTION 31 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Sharing a private moment where we can be completely honest.",
            callback_data="q31_1"
        ),
        types.InlineKeyboardButton(
            "2. Seeing each other succeed while still following our own dreams.",
            callback_data="q31_2"
        ),
        types.InlineKeyboardButton(
            "3. Celebrating something special that we achieved together.",
            callback_data="q31_3"
        ),
        types.InlineKeyboardButton(
            "4. Having a deep conversation that makes us understand each other better.",
            callback_data="q31_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 31 IMAGE
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

        print("Question 31 image status:", response.status_code)
        print(
            "Question 31 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question31.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 31 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 31 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what kind of moment would make him "
        "feel especially happy in a relationship.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 31 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q31_")
)
def question_31_answer(call):

    answers = {
        "q31_1": "Sharing a private moment where we can be completely honest.",
        "q31_2": "Seeing each other succeed while still following our own dreams.",
        "q31_3": "Celebrating something special that we achieved together.",
        "q31_4": "Having a deep conversation that makes us understand each other better."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 31 POINTS
    # --------------------------------------------------------

    points = QUESTION_31_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 31
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles after hearing Daniel's answer.\n\n"
        "She feels that the conversation has become something "
        "more meaningful than she expected."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_32(call.message.chat.id)

#سؤال 32
# ============================================================
# QUESTION 32
# ============================================================

def send_question_32(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 32
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel and smiles.\n\n"
        "She asks him what he thinks helps two people stay "
        "close when life becomes busy."
    )

    # --------------------------------------------------------
    # QUESTION 32 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about how you feel, even when you are busy.",
            callback_data="q32_1"
        ),
        types.InlineKeyboardButton(
            "2. Giving each other enough space to focus on personal goals.",
            callback_data="q32_2"
        ),
        types.InlineKeyboardButton(
            "3. Making time for each other and showing continued support.",
            callback_data="q32_3"
        ),
        types.InlineKeyboardButton(
            "4. Keeping communication open and making time for meaningful conversations.",
            callback_data="q32_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 32 IMAGE
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

        print("Question 32 image status:", response.status_code)
        print(
            "Question 32 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question32.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 32 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 32 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps two people stay "
        "close when life becomes busy.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 32 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q32_")
)
def question_32_answer(call):

    answers = {
        "q32_1": "Being honest about how you feel, even when you are busy.",
        "q32_2": "Giving each other enough space to focus on personal goals.",
        "q32_3": "Making time for each other and showing continued support.",
        "q32_4": "Keeping communication open and making time for meaningful conversations."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 32 POINTS
    # --------------------------------------------------------

    points = QUESTION_32_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 32
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She likes hearing how Daniel thinks about balancing "
        "everyday responsibilities with a meaningful connection."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_33(call.message.chat.id)
	
	
#سؤال 33
# ============================================================
# QUESTION 33
# ============================================================

def send_question_33(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 33
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a curious smile.\n\n"
        "She asks him what he thinks makes someone feel "
        "truly understood in a relationship."
    )

    # --------------------------------------------------------
    # QUESTION 33 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being able to speak honestly without hiding your feelings.",
            callback_data="q33_1"
        ),
        types.InlineKeyboardButton(
            "2. Having your personal choices and boundaries respected.",
            callback_data="q33_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing that the other person listens and supports you.",
            callback_data="q33_3"
        ),
        types.InlineKeyboardButton(
            "4. Having someone who takes the time to understand your thoughts and feelings.",
            callback_data="q33_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 33 IMAGE
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

        print("Question 33 image status:", response.status_code)
        print(
            "Question 33 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question33.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 33 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 33 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks makes someone feel "
        "truly understood in a relationship.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 33 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q33_")
)
def question_33_answer(call):

    answers = {
        "q33_1": "Being able to speak honestly without hiding your feelings.",
        "q33_2": "Having your personal choices and boundaries respected.",
        "q33_3": "Knowing that the other person listens and supports you.",
        "q33_4": "Having someone who takes the time to understand your thoughts and feelings."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 33 POINTS
    # --------------------------------------------------------

    points = QUESTION_33_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 33
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully and smiles.\n\n"
        "She feels that Daniel has a thoughtful way of "
        "looking at emotional connection."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_34(call.message.chat.id)

#سؤال 34
# ============================================================
# QUESTION 34
# ============================================================

def send_question_34(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 34
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles as she thinks about Daniel's answers.\n\n"
        "She asks him what he thinks helps a relationship "
        "remain strong when two people disagree."
    )

    # --------------------------------------------------------
    # QUESTION 34 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about your feelings instead of hiding them.",
            callback_data="q34_1"
        ),
        types.InlineKeyboardButton(
            "2. Respecting each other's opinions and giving each other space.",
            callback_data="q34_2"
        ),
        types.InlineKeyboardButton(
            "3. Remembering that you are on the same team and supporting each other.",
            callback_data="q34_3"
        ),
        types.InlineKeyboardButton(
            "4. Listening carefully and trying to understand each other's point of view.",
            callback_data="q34_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 34 IMAGE
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

        print("Question 34 image status:", response.status_code)
        print(
            "Question 34 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question34.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 34 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 34 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps a relationship "
        "remain strong when two people disagree.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 34 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q34_")
)
def question_34_answer(call):

    answers = {
        "q34_1": "Being honest about your feelings instead of hiding them.",
        "q34_2": "Respecting each other's opinions and giving each other space.",
        "q34_3": "Remembering that you are on the same team and supporting each other.",
        "q34_4": "Listening carefully and trying to understand each other's point of view."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 34 POINTS
    # --------------------------------------------------------

    points = QUESTION_34_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 34
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully at Daniel's answer.\n\n"
        "She feels that disagreements do not have to create "
        "distance when both people are willing to understand "
        "each other."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_35(call.message.chat.id)

#سؤال 35

# ============================================================
# QUESTION 35
# ============================================================

def send_question_35(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 35
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a warm smile.\n\n"
        "She asks him what he thinks is the best way to "
        "keep a relationship feeling special after a long time."
    )

    # --------------------------------------------------------
    # QUESTION 35 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Keep being honest and never take each other for granted.",
            callback_data="q35_1"
        ),
        types.InlineKeyboardButton(
            "2. Give each other freedom to grow and follow individual interests.",
            callback_data="q35_2"
        ),
        types.InlineKeyboardButton(
            "3. Keep making memories together and supporting each other's dreams.",
            callback_data="q35_3"
        ),
        types.InlineKeyboardButton(
            "4. Continue having meaningful conversations and learning about each other.",
            callback_data="q35_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 35 IMAGE
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

        print("Question 35 image status:", response.status_code)
        print(
            "Question 35 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question35.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 35 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 35 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "keep a relationship feeling special after a long time.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 35 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q35_")
)
def question_35_answer(call):

    answers = {
        "q35_1": "Keep being honest and never take each other for granted.",
        "q35_2": "Give each other freedom to grow and follow individual interests.",
        "q35_3": "Keep making memories together and supporting each other's dreams.",
        "q35_4": "Continue having meaningful conversations and learning about each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 35 POINTS
    # --------------------------------------------------------

    points = QUESTION_35_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 35
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles and nods.\n\n"
        "She feels that Daniel understands that a strong "
        "relationship needs care even after the excitement "
        "of the beginning has passed."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_36(call.message.chat.id)

#سؤال 36
# ============================================================
# QUESTION 36
# ============================================================

def send_question_36(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 36
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel and smiles.\n\n"
        "She asks him what he thinks makes a person "
        "feel confident about the future of a relationship."
    )

    # --------------------------------------------------------
    # QUESTION 36 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Knowing that both people are honest about their feelings and intentions.",
            callback_data="q36_1"
        ),
        types.InlineKeyboardButton(
            "2. Knowing that both people can grow while keeping their independence.",
            callback_data="q36_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing that both people will support each other through challenges.",
            callback_data="q36_3"
        ),
        types.InlineKeyboardButton(
            "4. Knowing that both people communicate openly and understand each other.",
            callback_data="q36_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 36 IMAGE
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

        print("Question 36 image status:", response.status_code)
        print(
            "Question 36 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question36.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 36 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 36 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks makes a person "
        "feel confident about the future of a relationship.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 36 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q36_")
)
def question_36_answer(call):

    answers = {
        "q36_1": "Knowing that both people are honest about their feelings and intentions.",
        "q36_2": "Knowing that both people can grow while keeping their independence.",
        "q36_3": "Knowing that both people will support each other through challenges.",
        "q36_4": "Knowing that both people communicate openly and understand each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 36 POINTS
    # --------------------------------------------------------

    points = QUESTION_36_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 36
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully and smiles.\n\n"
        "She feels that Daniel has a clear idea of what "
        "would make a relationship feel secure and lasting."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_37(call.message.chat.id)

#سؤال 37

# ============================================================
# QUESTION 37
# ============================================================

def send_question_37(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 37
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as their conversation continues.\n\n"
        "She asks him what he thinks is the best way to "
        "make someone feel special on an ordinary day."
    )

    # --------------------------------------------------------
    # QUESTION 37 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Tell them honestly how much they mean to you.",
            callback_data="q37_1"
        ),
        types.InlineKeyboardButton(
            "2. Give them time and space to enjoy their own interests.",
            callback_data="q37_2"
        ),
        types.InlineKeyboardButton(
            "3. Do something thoughtful to show that you care.",
            callback_data="q37_3"
        ),
        types.InlineKeyboardButton(
            "4. Spend quality time together and have a meaningful conversation.",
            callback_data="q37_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 37 IMAGE
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

        print("Question 37 image status:", response.status_code)
        print(
            "Question 37 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question37.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 37 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 37 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "make someone feel special on an ordinary day.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 37 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q37_")
)
def question_37_answer(call):

    answers = {
        "q37_1": "Tell them honestly how much they mean to you.",
        "q37_2": "Give them time and space to enjoy their own interests.",
        "q37_3": "Do something thoughtful to show that you care.",
        "q37_4": "Spend quality time together and have a meaningful conversation."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 37 POINTS
    # --------------------------------------------------------

    points = QUESTION_37_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 37
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly at Daniel's answer.\n\n"
        "She realizes that sometimes the smallest gestures "
        "can say the most."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_38(call.message.chat.id)

#سؤال 38

# ============================================================
# QUESTION 38
# ============================================================

def send_question_38(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 38
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel thoughtfully.\n\n"
        "She asks him what he thinks helps two people "
        "feel emotionally connected even when they are apart."
    )

    # --------------------------------------------------------
    # QUESTION 38 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about how you feel and keeping each other updated.",
            callback_data="q38_1"
        ),
        types.InlineKeyboardButton(
            "2. Trusting each other and giving each person enough personal space.",
            callback_data="q38_2"
        ),
        types.InlineKeyboardButton(
            "3. Making an effort to stay in touch and remind each other you care.",
            callback_data="q38_3"
        ),
        types.InlineKeyboardButton(
            "4. Having meaningful conversations and sharing your thoughts and experiences.",
            callback_data="q38_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 38 IMAGE
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

        print("Question 38 image status:", response.status_code)
        print(
            "Question 38 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question38.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 38 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 38 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps two people "
        "feel emotionally connected even when they are apart.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 38 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q38_")
)
def question_38_answer(call):

    answers = {
        "q38_1": "Being honest about how you feel and keeping each other updated.",
        "q38_2": "Trusting each other and giving each person enough personal space.",
        "q38_3": "Making an effort to stay in touch and remind each other you care.",
        "q38_4": "Having meaningful conversations and sharing your thoughts and experiences."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 38 POINTS
    # --------------------------------------------------------

    points = QUESTION_38_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 38
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods with a smile.\n\n"
        "She thinks about how important it is to stay "
        "connected even when life keeps people busy or apart."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_39(call.message.chat.id)

#سؤال 39

# ============================================================
# QUESTION 39
# ============================================================

def send_question_39(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 39
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a gentle smile.\n\n"
        "She asks him what he thinks makes a relationship "
        "feel truly special over the long term."
    )

    # --------------------------------------------------------
    # QUESTION 39 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Knowing that you can always be honest with each other.",
            callback_data="q39_1"
        ),
        types.InlineKeyboardButton(
            "2. Being able to grow together while still being yourselves.",
            callback_data="q39_2"
        ),
        types.InlineKeyboardButton(
            "3. Having someone who stays loyal and supports you through life.",
            callback_data="q39_3"
        ),
        types.InlineKeyboardButton(
            "4. Feeling deeply understood and comfortable sharing everything.",
            callback_data="q39_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 39 IMAGE
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

        print("Question 39 image status:", response.status_code)
        print(
            "Question 39 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question39.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 39 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 39 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks makes a relationship "
        "feel truly special over the long term.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 39 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q39_")
)
def question_39_answer(call):

    answers = {
        "q39_1": "Knowing that you can always be honest with each other.",
        "q39_2": "Being able to grow together while still being yourselves.",
        "q39_3": "Having someone who stays loyal and supports you through life.",
        "q39_4": "Feeling deeply understood and comfortable sharing everything."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 39 POINTS
    # --------------------------------------------------------

    points = QUESTION_39_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 39
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles thoughtfully at Daniel's answer.\n\n"
        "She feels that they are getting closer to understanding "
        "what really matters to him in a lasting connection."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_40(call.message.chat.id)

#سؤال 40
# ============================================================
# QUESTION 40
# ============================================================

def send_question_40(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 40
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as their conversation continues.\n\n"
        "She asks him what he would want his partner to know "
        "when he is going through a difficult time."
    )

    # --------------------------------------------------------
    # QUESTION 40 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I'd want them to know that I will always be honest about how I feel.",
            callback_data="q40_1"
        ),
        types.InlineKeyboardButton(
            "2. I'd want them to give me some space while still respecting my choices.",
            callback_data="q40_2"
        ),
        types.InlineKeyboardButton(
            "3. I'd want them to stay by my side and remind me that I am not alone.",
            callback_data="q40_3"
        ),
        types.InlineKeyboardButton(
            "4. I'd want them to listen patiently and let me talk when I am ready.",
            callback_data="q40_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 40 IMAGE
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

        print("Question 40 image status:", response.status_code)
        print(
            "Question 40 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question40.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 40 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 40 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would want his partner to know "
        "when he is going through a difficult time.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 40 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q40_")
)
def question_40_answer(call):

    answers = {
        "q40_1": "I'd want them to know that I will always be honest about how I feel.",
        "q40_2": "I'd want them to give me some space while still respecting my choices.",
        "q40_3": "I'd want them to stay by my side and remind me that I am not alone.",
        "q40_4": "I'd want them to listen patiently and let me talk when I am ready."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 40 POINTS
    # --------------------------------------------------------

    points = QUESTION_40_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 40
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens quietly and smiles.\n\n"
        "She feels that Daniel has shared something more personal "
        "about how he handles difficult moments and what he needs "
        "from someone close to him."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_41(call.message.chat.id)


#سؤال 41
# ============================================================
# QUESTION 41
# ============================================================

def send_question_41(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 41
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a thoughtful smile.\n\n"
        "She asks him what he thinks is most important when "
        "two people are planning their future together."
    )

    # --------------------------------------------------------
    # QUESTION 41 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about what each person really wants.",
            callback_data="q41_1"
        ),
        types.InlineKeyboardButton(
            "2. Making sure both people can follow their own dreams.",
            callback_data="q41_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing that you can rely on each other through every challenge.",
            callback_data="q41_3"
        ),
        types.InlineKeyboardButton(
            "4. Talking openly about plans and making important decisions together.",
            callback_data="q41_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 41 IMAGE
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

        print("Question 41 image status:", response.status_code)
        print(
            "Question 41 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question41.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 41 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 41 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is most important "
        "when two people are planning their future together.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 41 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q41_")
)
def question_41_answer(call):

    answers = {
        "q41_1": "Being honest about what each person really wants.",
        "q41_2": "Making sure both people can follow their own dreams.",
        "q41_3": "Knowing that you can rely on each other through every challenge.",
        "q41_4": "Talking openly about plans and making important decisions together."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 41 POINTS
    # --------------------------------------------------------

    points = QUESTION_41_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 41
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She likes hearing how Daniel imagines building a "
        "future while still keeping both people's needs in mind."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_42(call.message.chat.id)

#سؤال 42 

# ============================================================
# QUESTION 42
# ============================================================

def send_question_42(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 42
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel and thinks about everything "
        "they have discussed.\n\n"
        "She asks him what he thinks is the best way to show "
        "someone that they are genuinely important to you."
    )

    # --------------------------------------------------------
    # QUESTION 42 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Tell them honestly and openly how much they mean to you.",
            callback_data="q42_1"
        ),
        types.InlineKeyboardButton(
            "2. Respect their independence and support the life they want.",
            callback_data="q42_2"
        ),
        types.InlineKeyboardButton(
            "3. Be there for them when they need support, no matter what.",
            callback_data="q42_3"
        ),
        types.InlineKeyboardButton(
            "4. Listen to them carefully and remember the things that matter to them.",
            callback_data="q42_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 42 IMAGE
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

        print("Question 42 image status:", response.status_code)
        print(
            "Question 42 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question42.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 42 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 42 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "show someone that they are genuinely important to you.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 42 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q42_")
)
def question_42_answer(call):

    answers = {
        "q42_1": "Tell them honestly and openly how much they mean to you.",
        "q42_2": "Respect their independence and support the life they want.",
        "q42_3": "Be there for them when they need support, no matter what.",
        "q42_4": "Listen to them carefully and remember the things that matter to them."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 42 POINTS
    # --------------------------------------------------------

    points = QUESTION_42_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 42
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly at Daniel's answer.\n\n"
        "She feels that he has a thoughtful understanding "
        "of the different ways people can show that they care."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_43(call.message.chat.id)

#سؤال 43

# ============================================================
# QUESTION 43
# ============================================================

def send_question_43(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 43
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a curious smile.\n\n"
        "She asks him what he thinks two people should do "
        "when they realize they have different priorities."
    )

    # --------------------------------------------------------
    # QUESTION 43 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Talk honestly about what each person wants.",
            callback_data="q43_1"
        ),
        types.InlineKeyboardButton(
            "2. Give each other freedom to follow different priorities.",
            callback_data="q43_2"
        ),
        types.InlineKeyboardButton(
            "3. Find a compromise and make sure neither person feels alone.",
            callback_data="q43_3"
        ),
        types.InlineKeyboardButton(
            "4. Take time to understand each other's reasons before deciding.",
            callback_data="q43_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 43 IMAGE
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

        print("Question 43 image status:", response.status_code)
        print(
            "Question 43 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question43.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 43 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 43 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks two people should do "
        "when they realize they have different priorities.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 43 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q43_")
)
def question_43_answer(call):

    answers = {
        "q43_1": "Talk honestly about what each person wants.",
        "q43_2": "Give each other freedom to follow different priorities.",
        "q43_3": "Find a compromise and make sure neither person feels alone.",
        "q43_4": "Take time to understand each other's reasons before deciding."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 43 POINTS
    # --------------------------------------------------------

    points = QUESTION_43_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 43
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She appreciates Daniel's answer and wonders how "
        "he would handle other important moments in a future relationship."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_44(call.message.chat.id)


#سؤال 44

# ============================================================
# QUESTION 44
# ============================================================

def send_question_44(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 44
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel and continues the conversation.\n\n"
        "She asks him what he thinks is the best way to rebuild "
        "trust after someone has been hurt."
    )

    # --------------------------------------------------------
    # QUESTION 44 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be completely honest and admit what happened.",
            callback_data="q44_1"
        ),
        types.InlineKeyboardButton(
            "2. Give the other person time and respect their boundaries.",
            callback_data="q44_2"
        ),
        types.InlineKeyboardButton(
            "3. Show through actions that they can depend on you again.",
            callback_data="q44_3"
        ),
        types.InlineKeyboardButton(
            "4. Talk openly about what happened and try to understand each other's feelings.",
            callback_data="q44_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 44 IMAGE
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

        print("Question 44 image status:", response.status_code)
        print(
            "Question 44 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question44.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 44 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 44 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "rebuild trust after someone has been hurt.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 44 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q44_")
)
def question_44_answer(call):

    answers = {
        "q44_1": "Be completely honest and admit what happened.",
        "q44_2": "Give the other person time and respect their boundaries.",
        "q44_3": "Show through actions that they can depend on you again.",
        "q44_4": "Talk openly about what happened and try to understand each other's feelings."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 44 POINTS
    # --------------------------------------------------------

    points = QUESTION_44_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 44
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully and nods.\n\n"
        "She feels that Daniel understands that trust is built "
        "again through honesty, patience, and consistent actions."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_45(call.message.chat.id)


#سؤال 45

# ============================================================
# QUESTION 45
# ============================================================

def send_question_45(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 45
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as the conversation continues.\n\n"
        "She asks him what he thinks makes a relationship "
        "feel peaceful and comfortable."
    )

    # --------------------------------------------------------
    # QUESTION 45 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Knowing that you can always speak honestly with each other.",
            callback_data="q45_1"
        ),
        types.InlineKeyboardButton(
            "2. Feeling free to be yourself without losing your independence.",
            callback_data="q45_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing that you can rely on each other when life gets difficult.",
            callback_data="q45_3"
        ),
        types.InlineKeyboardButton(
            "4. Feeling understood, listened to, and comfortable sharing your thoughts.",
            callback_data="q45_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 45 IMAGE
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

        print("Question 45 image status:", response.status_code)
        print(
            "Question 45 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question45.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 45 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 45 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks makes a relationship "
        "feel peaceful and comfortable.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 45 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q45_")
)
def question_45_answer(call):

    answers = {
        "q45_1": "Knowing that you can always speak honestly with each other.",
        "q45_2": "Feeling free to be yourself without losing your independence.",
        "q45_3": "Knowing that you can rely on each other when life gets difficult.",
        "q45_4": "Feeling understood, listened to, and comfortable sharing your thoughts."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 45 POINTS
    # --------------------------------------------------------

    points = QUESTION_45_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 45
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly after hearing Daniel's answer.\n\n"
        "She feels that he understands how important it is "
        "to feel safe, respected, and comfortable with someone."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_46(call.message.chat.id)

#سؤال 46

# ============================================================
# QUESTION 46
# ============================================================

def send_question_46(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 46
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a thoughtful smile.\n\n"
        "She asks him what he thinks is most important when "
        "a relationship starts becoming more serious."
    )

    # --------------------------------------------------------
    # QUESTION 46 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about your feelings and what you want.",
            callback_data="q46_1"
        ),
        types.InlineKeyboardButton(
            "2. Making sure both people can still have their own lives and goals.",
            callback_data="q46_2"
        ),
        types.InlineKeyboardButton(
            "3. Showing that you are loyal and willing to support each other.",
            callback_data="q46_3"
        ),
        types.InlineKeyboardButton(
            "4. Talking openly about expectations and understanding each other.",
            callback_data="q46_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 46 IMAGE
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

        print("Question 46 image status:", response.status_code)
        print(
            "Question 46 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question46.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 46 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 46 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is most important "
        "when a relationship starts becoming more serious.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 46 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q46_")
)
def question_46_answer(call):

    answers = {
        "q46_1": "Being honest about your feelings and what you want.",
        "q46_2": "Making sure both people can still have their own lives and goals.",
        "q46_3": "Showing that you are loyal and willing to support each other.",
        "q46_4": "Talking openly about expectations and understanding each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 46 POINTS
    # --------------------------------------------------------

    points = QUESTION_46_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 46
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods slowly.\n\n"
        "She feels that Daniel understands that a serious "
        "relationship needs both trust and a clear understanding "
        "of what each person wants."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_47(call.message.chat.id)

#سؤال 47

# ============================================================
# QUESTION 47
# ============================================================

def send_question_47(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 47
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as they continue talking.\n\n"
        "She asks him what he thinks is the best way to "
        "keep a relationship strong during stressful times."
    )

    # --------------------------------------------------------
    # QUESTION 47 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest about your stress instead of hiding it.",
            callback_data="q47_1"
        ),
        types.InlineKeyboardButton(
            "2. Give each other space to deal with personal responsibilities.",
            callback_data="q47_2"
        ),
        types.InlineKeyboardButton(
            "3. Support each other and make sure neither person feels alone.",
            callback_data="q47_3"
        ),
        types.InlineKeyboardButton(
            "4. Talk calmly about what is happening and listen to each other.",
            callback_data="q47_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 47 IMAGE
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

        print("Question 47 image status:", response.status_code)
        print(
            "Question 47 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question47.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 47 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 47 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "keep a relationship strong during stressful times.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 47 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q47_")
)
def question_47_answer(call):

    answers = {
        "q47_1": "Be honest about your stress instead of hiding it.",
        "q47_2": "Give each other space to deal with personal responsibilities.",
        "q47_3": "Support each other and make sure neither person feels alone.",
        "q47_4": "Talk calmly about what is happening and listen to each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 47 POINTS
    # --------------------------------------------------------

    points = QUESTION_47_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 47
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She appreciates Daniel's answer and feels that "
        "he understands how important support and communication "
        "can be when life becomes difficult."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_48(call.message.chat.id)

#سؤال 48

# ============================================================
# QUESTION 48
# ============================================================

def send_question_48(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 48
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a warm smile.\n\n"
        "She asks him what he thinks helps two people "
        "stay close when their lives become very busy."
    )

    # --------------------------------------------------------
    # QUESTION 48 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest when you are busy and make sure the other person knows how you feel.",
            callback_data="q48_1"
        ),
        types.InlineKeyboardButton(
            "2. Respect each other's schedules and make time for your own interests too.",
            callback_data="q48_2"
        ),
        types.InlineKeyboardButton(
            "3. Make a real effort to stay connected and be there for each other.",
            callback_data="q48_3"
        ),
        types.InlineKeyboardButton(
            "4. Keep communicating and share what is happening in your lives.",
            callback_data="q48_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 48 IMAGE
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

        print("Question 48 image status:", response.status_code)
        print(
            "Question 48 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question48.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 48 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 48 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps two people "
        "stay close when their lives become very busy.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 48 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q48_")
)
def question_48_answer(call):

    answers = {
        "q48_1": "Be honest when you are busy and make sure the other person knows how you feel.",
        "q48_2": "Respect each other's schedules and make time for your own interests too.",
        "q48_3": "Make a real effort to stay connected and be there for each other.",
        "q48_4": "Keep communicating and share what is happening in your lives."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 48 POINTS
    # --------------------------------------------------------

    points = QUESTION_48_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 48
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles and nods.\n\n"
        "She feels that Daniel understands that being busy "
        "doesn't have to mean becoming emotionally distant."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_49(call.message.chat.id)

#سؤال 49

# ============================================================
# QUESTION 49
# ============================================================

def send_question_49(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 49
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a thoughtful smile.\n\n"
        "She asks him what he thinks is the best way to handle "
        "an important disagreement with someone you care about."
    )

    # --------------------------------------------------------
    # QUESTION 49 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest about how you feel without hiding the truth.",
            callback_data="q49_1"
        ),
        types.InlineKeyboardButton(
            "2. Give each other some space and think independently before responding.",
            callback_data="q49_2"
        ),
        types.InlineKeyboardButton(
            "3. Try to find a solution that supports both people.",
            callback_data="q49_3"
        ),
        types.InlineKeyboardButton(
            "4. Listen carefully and try to understand the other person's point of view.",
            callback_data="q49_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 49 IMAGE
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

        print("Question 49 image status:", response.status_code)
        print(
            "Question 49 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question49.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 49 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 49 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "handle an important disagreement with someone you care about.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 49 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q49_")
)
def question_49_answer(call):

    answers = {
        "q49_1": "Be honest about how you feel without hiding the truth.",
        "q49_2": "Give each other some space and think independently before responding.",
        "q49_3": "Try to find a solution that supports both people.",
        "q49_4": "Listen carefully and try to understand the other person's point of view."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 49 POINTS
    # --------------------------------------------------------

    points = QUESTION_49_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 49
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully and nods.\n\n"
        "She appreciates Daniel's thoughtful approach and feels "
        "that he understands that disagreements do not have to "
        "damage a strong relationship."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_50(call.message.chat.id)


#سؤال 50

# ============================================================
# QUESTION 50
# ============================================================

def send_question_50(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 50
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as their conversation reaches "
        "another important moment.\n\n"
        "She asks him what he thinks is the most important "
        "quality to have in a long-term relationship."
    )

    # --------------------------------------------------------
    # QUESTION 50 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Honesty, so both people can always trust each other.",
            callback_data="q50_1"
        ),
        types.InlineKeyboardButton(
            "2. Independence, so both people can continue to grow.",
            callback_data="q50_2"
        ),
        types.InlineKeyboardButton(
            "3. Loyalty, so both people know they can depend on each other.",
            callback_data="q50_3"
        ),
        types.InlineKeyboardButton(
            "4. Understanding, so both people feel heard and appreciated.",
            callback_data="q50_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 50 IMAGE
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

        print("Question 50 image status:", response.status_code)
        print(
            "Question 50 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question50.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 50 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 50 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the most important "
        "quality to have in a long-term relationship.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 50 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q50_")
)
def question_50_answer(call):

    answers = {
        "q50_1": "Honesty, so both people can always trust each other.",
        "q50_2": "Independence, so both people can continue to grow.",
        "q50_3": "Loyalty, so both people know they can depend on each other.",
        "q50_4": "Understanding, so both people feel heard and appreciated."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 50 POINTS
    # --------------------------------------------------------

    points = QUESTION_50_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 50
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles after hearing Daniel's answer.\n\n"
        "She feels that their conversation has revealed more "
        "about what he truly values in a lasting relationship."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_51(call.message.chat.id)

#سؤال 51

# ============================================================
# QUESTION 51
# ============================================================

def send_question_51(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 51
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a warm smile.\n\n"
        "She asks him what he would do if someone he cared about "
        "was feeling uncertain about their relationship."
    )

    # --------------------------------------------------------
    # QUESTION 51 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest about my feelings and reassure them without pretending.",
            callback_data="q51_1"
        ),
        types.InlineKeyboardButton(
            "2. Give them time to think and let them make their own decision.",
            callback_data="q51_2"
        ),
        types.InlineKeyboardButton(
            "3. Remind them that I care and that they can count on me.",
            callback_data="q51_3"
        ),
        types.InlineKeyboardButton(
            "4. Listen to their concerns and talk through them together.",
            callback_data="q51_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 51 IMAGE
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

        print("Question 51 image status:", response.status_code)
        print(
            "Question 51 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question51.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 51 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 51 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he would do if someone he cared "
        "about was feeling uncertain about their relationship.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 51 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q51_")
)
def question_51_answer(call):

    answers = {
        "q51_1": "Be honest about my feelings and reassure them without pretending.",
        "q51_2": "Give them time to think and let them make their own decision.",
        "q51_3": "Remind them that I care and that they can count on me.",
        "q51_4": "Listen to their concerns and talk through them together."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 51 POINTS
    # --------------------------------------------------------

    points = QUESTION_51_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 51
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily listens carefully and smiles.\n\n"
        "She appreciates Daniel's answer and feels that he "
        "understands the importance of patience, reassurance, "
        "and honest communication."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_52(call.message.chat.id)

#سؤال 52

# ============================================================
# QUESTION 52
# ============================================================

def send_question_52(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 52
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as the conversation continues.\n\n"
        "She asks him what he thinks helps a couple keep their "
        "connection strong as they get to know each other better."
    )

    # --------------------------------------------------------
    # QUESTION 52 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being truthful and comfortable sharing your real feelings.",
            callback_data="q52_1"
        ),
        types.InlineKeyboardButton(
            "2. Respecting each other's personal space and individual goals.",
            callback_data="q52_2"
        ),
        types.InlineKeyboardButton(
            "3. Making time for each other and showing consistent support.",
            callback_data="q52_3"
        ),
        types.InlineKeyboardButton(
            "4. Continuing to ask questions, listen, and understand each other's thoughts.",
            callback_data="q52_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 52 IMAGE
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

        print("Question 52 image status:", response.status_code)
        print(
            "Question 52 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question52.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 52 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 52 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps a couple keep "
        "their connection strong as they get to know each other better.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 52 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q52_")
)
def question_52_answer(call):

    answers = {
        "q52_1": "Being truthful and comfortable sharing your real feelings.",
        "q52_2": "Respecting each other's personal space and individual goals.",
        "q52_3": "Making time for each other and showing consistent support.",
        "q52_4": "Continuing to ask questions, listen, and understand each other's thoughts."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 52 POINTS
    # --------------------------------------------------------

    points = QUESTION_52_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 52
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods with a smile.\n\n"
        "She feels that Daniel understands that getting closer "
        "to someone takes patience, effort, and genuine interest."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_53(call.message.chat.id)

#سؤال 53

# ============================================================
# QUESTION 53
# ============================================================

def send_question_53(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 53
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel thoughtfully.\n\n"
        "She asks him what he thinks a couple should do when "
        "one person needs extra support but does not know how to ask for it."
    )

    # --------------------------------------------------------
    # QUESTION 53 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest and gently ask them what they are feeling.",
            callback_data="q53_1"
        ),
        types.InlineKeyboardButton(
            "2. Give them space while letting them know you are available.",
            callback_data="q53_2"
        ),
        types.InlineKeyboardButton(
            "3. Stay close and show through your actions that you are there for them.",
            callback_data="q53_3"
        ),
        types.InlineKeyboardButton(
            "4. Listen carefully and give them time to explain what they need.",
            callback_data="q53_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 53 IMAGE
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

        print("Question 53 image status:", response.status_code)
        print(
            "Question 53 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question53.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 53 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 53 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks a couple should do "
        "when one person needs extra support but does not know "
        "how to ask for it.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 53 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q53_")
)
def question_53_answer(call):

    answers = {
        "q53_1": "Be honest and gently ask them what they are feeling.",
        "q53_2": "Give them space while letting them know you are available.",
        "q53_3": "Stay close and show through your actions that you are there for them.",
        "q53_4": "Listen carefully and give them time to explain what they need."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 53 POINTS
    # --------------------------------------------------------

    points = QUESTION_53_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 53
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles softly.\n\n"
        "She appreciates Daniel's thoughtful answer and feels "
        "that he understands how important it is to notice when "
        "someone needs care without putting pressure on them."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_54(call.message.chat.id)


#سؤال 54

# ============================================================
# QUESTION 54
# ============================================================

def send_question_54(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 54
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as the conversation continues.\n\n"
        "She asks him what he thinks helps two people feel "
        "secure enough to be completely themselves in a relationship."
    )

    # --------------------------------------------------------
    # QUESTION 54 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Knowing that you can be honest without being judged.",
            callback_data="q54_1"
        ),
        types.InlineKeyboardButton(
            "2. Knowing that you can have your own interests and still be accepted.",
            callback_data="q54_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing that your partner will stay loyal and support you.",
            callback_data="q54_3"
        ),
        types.InlineKeyboardButton(
            "4. Knowing that your partner will listen and try to understand you.",
            callback_data="q54_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 54 IMAGE
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

        print("Question 54 image status:", response.status_code)
        print(
            "Question 54 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question54.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 54 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 54 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps two people feel "
        "secure enough to be completely themselves in a relationship.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 54 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q54_")
)
def question_54_answer(call):

    answers = {
        "q54_1": "Knowing that you can be honest without being judged.",
        "q54_2": "Knowing that you can have your own interests and still be accepted.",
        "q54_3": "Knowing that your partner will stay loyal and support you.",
        "q54_4": "Knowing that your partner will listen and try to understand you."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 54 POINTS
    # --------------------------------------------------------

    points = QUESTION_54_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 54
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods with a warm smile.\n\n"
        "She feels that Daniel understands that a strong "
        "relationship should allow both people to feel accepted "
        "without pretending to be someone they are not."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_55(call.message.chat.id)

#سؤال 55

# ============================================================
# QUESTION 55
# ============================================================

def send_question_55(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 55
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel and smiles.\n\n"
        "She asks him what he thinks makes someone feel truly "
        "appreciated in a relationship."
    )

    # --------------------------------------------------------
    # QUESTION 55 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Hearing sincere words that show how much they are valued.",
            callback_data="q55_1"
        ),
        types.InlineKeyboardButton(
            "2. Having their choices, interests, and personal goals respected.",
            callback_data="q55_2"
        ),
        types.InlineKeyboardButton(
            "3. Seeing that their partner makes an effort to support them.",
            callback_data="q55_3"
        ),
        types.InlineKeyboardButton(
            "4. Feeling listened to and knowing their thoughts genuinely matter.",
            callback_data="q55_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 55 IMAGE
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

        print("Question 55 image status:", response.status_code)
        print(
            "Question 55 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question55.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 55 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 55 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks makes someone feel "
        "truly appreciated in a relationship.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 55 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q55_")
)
def question_55_answer(call):

    answers = {
        "q55_1": "Hearing sincere words that show how much they are valued.",
        "q55_2": "Having their choices, interests, and personal goals respected.",
        "q55_3": "Seeing that their partner makes an effort to support them.",
        "q55_4": "Feeling listened to and knowing their thoughts genuinely matter."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 55 POINTS
    # --------------------------------------------------------

    points = QUESTION_55_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 55
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly.\n\n"
        "She feels that Daniel understands that appreciation "
        "is not just about words, but also about respect, support, "
        "and genuine attention."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_56(call.message.chat.id)

#سؤال 56

# ============================================================
# QUESTION 56
# ============================================================

def send_question_56(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 56
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel thoughtfully.\n\n"
        "She asks him what he thinks two people should do "
        "when they want different things from their future."
    )

    # --------------------------------------------------------
    # QUESTION 56 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest about what each person wants and why.",
            callback_data="q56_1"
        ),
        types.InlineKeyboardButton(
            "2. Respect each person's individual plans and find a way to grow separately.",
            callback_data="q56_2"
        ),
        types.InlineKeyboardButton(
            "3. Look for a compromise that allows both people to feel supported.",
            callback_data="q56_3"
        ),
        types.InlineKeyboardButton(
            "4. Have a calm conversation and try to understand both perspectives.",
            callback_data="q56_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 56 IMAGE
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

        print("Question 56 image status:", response.status_code)
        print(
            "Question 56 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question56.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 56 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 56 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks two people should do "
        "when they want different things from their future.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 56 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q56_")
)
def question_56_answer(call):

    answers = {
        "q56_1": "Be honest about what each person wants and why.",
        "q56_2": "Respect each person's individual plans and find a way to grow separately.",
        "q56_3": "Look for a compromise that allows both people to feel supported.",
        "q56_4": "Have a calm conversation and try to understand both perspectives."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 56 POINTS
    # --------------------------------------------------------

    points = QUESTION_56_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 56
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She appreciates Daniel's answer and feels that he "
        "understands how important it is to respect both people's "
        "dreams while finding common ground."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_57(call.message.chat.id)

#سؤال 57

# ============================================================
# QUESTION 57
# ============================================================

def send_question_57(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 57
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as they continue their conversation.\n\n"
        "She asks him what he thinks is the best way to show "
        "someone that they can trust you."
    )

    # --------------------------------------------------------
    # QUESTION 57 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Always tell the truth, even when it is difficult.",
            callback_data="q57_1"
        ),
        types.InlineKeyboardButton(
            "2. Keep your promises while respecting their independence.",
            callback_data="q57_2"
        ),
        types.InlineKeyboardButton(
            "3. Be consistent and prove through your actions that you care.",
            callback_data="q57_3"
        ),
        types.InlineKeyboardButton(
            "4. Listen to their concerns and make sure they feel understood.",
            callback_data="q57_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 57 IMAGE
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

        print("Question 57 image status:", response.status_code)
        print(
            "Question 57 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question57.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 57 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 57 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "show someone that they can trust you.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 57 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q57_")
)
def question_57_answer(call):

    answers = {
        "q57_1": "Always tell the truth, even when it is difficult.",
        "q57_2": "Keep your promises while respecting their independence.",
        "q57_3": "Be consistent and prove through your actions that you care.",
        "q57_4": "Listen to their concerns and make sure they feel understood."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 57 POINTS
    # --------------------------------------------------------

    points = QUESTION_57_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 57
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods with a small smile.\n\n"
        "She feels that Daniel understands that trust is built "
        "through honesty, consistency, respect, and genuine care."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_58(call.message.chat.id)

#سؤال 58

# ============================================================
# QUESTION 58
# ============================================================

def send_question_58(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 58
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a curious smile.\n\n"
        "She asks him what he thinks helps a relationship "
        "continue to grow after the first excitement begins to fade."
    )

    # --------------------------------------------------------
    # QUESTION 58 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Continue being honest and open about your feelings.",
            callback_data="q58_1"
        ),
        types.InlineKeyboardButton(
            "2. Give each other room to grow and keep your own interests.",
            callback_data="q58_2"
        ),
        types.InlineKeyboardButton(
            "3. Keep making an effort and showing that you care.",
            callback_data="q58_3"
        ),
        types.InlineKeyboardButton(
            "4. Keep learning about each other and talking about what matters.",
            callback_data="q58_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 58 IMAGE
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

        print("Question 58 image status:", response.status_code)
        print(
            "Question 58 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question58.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 58 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 58 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps a relationship "
        "continue to grow after the first excitement begins to fade.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 58 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q58_")
)
def question_58_answer(call):

    answers = {
        "q58_1": "Continue being honest and open about your feelings.",
        "q58_2": "Give each other room to grow and keep your own interests.",
        "q58_3": "Keep making an effort and showing that you care.",
        "q58_4": "Keep learning about each other and talking about what matters."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 58 POINTS
    # --------------------------------------------------------

    points = QUESTION_58_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 58
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles and nods.\n\n"
        "She feels that Daniel understands that a lasting "
        "relationship needs continued effort, curiosity, honesty, "
        "and respect for each person's growth."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_59(call.message.chat.id)


#سؤال 59

# ============================================================
# QUESTION 59
# ============================================================

def send_question_59(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 59
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as they continue their conversation.\n\n"
        "She asks him what he thinks is most important when "
        "building a future together with someone."
    )

    # --------------------------------------------------------
    # QUESTION 59 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about your hopes, plans, and expectations.",
            callback_data="q59_1"
        ),
        types.InlineKeyboardButton(
            "2. Supporting each other's dreams while keeping your own identity.",
            callback_data="q59_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing that you can rely on each other through good and difficult times.",
            callback_data="q59_3"
        ),
        types.InlineKeyboardButton(
            "4. Communicating openly and making important decisions together.",
            callback_data="q59_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 59 IMAGE
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

        print("Question 59 image status:", response.status_code)
        print(
            "Question 59 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question59.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 59 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 59 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is most important when "
        "building a future together with someone.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 59 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q59_")
)
def question_59_answer(call):

    answers = {
        "q59_1": "Being honest about your hopes, plans, and expectations.",
        "q59_2": "Supporting each other's dreams while keeping your own identity.",
        "q59_3": "Knowing that you can rely on each other through good and difficult times.",
        "q59_4": "Communicating openly and making important decisions together."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 59 POINTS
    # --------------------------------------------------------

    points = QUESTION_59_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 59
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She feels that Daniel understands that building a future "
        "together requires trust, support, communication, and a "
        "shared willingness to grow."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_60(call.message.chat.id)

#سؤال 60

# ============================================================
# QUESTION 60
# ============================================================

def send_question_60(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 60
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as their conversation continues.\n\n"
        "She asks him what he thinks is the best way to make "
        "someone feel valued when they are going through a difficult time."
    )

    # --------------------------------------------------------
    # QUESTION 60 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest with them and let them know they can talk to you.",
            callback_data="q60_1"
        ),
        types.InlineKeyboardButton(
            "2. Give them space while respecting whatever they need to feel comfortable.",
            callback_data="q60_2"
        ),
        types.InlineKeyboardButton(
            "3. Stay by their side and show through your actions that you care.",
            callback_data="q60_3"
        ),
        types.InlineKeyboardButton(
            "4. Listen patiently and try to understand what they are going through.",
            callback_data="q60_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 60 IMAGE
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

        print("Question 60 image status:", response.status_code)
        print(
            "Question 60 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question60.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 60 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 60 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "make someone feel valued when they are going through "
        "a difficult time.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 60 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q60_")
)
def question_60_answer(call):

    answers = {
        "q60_1": "Be honest with them and let them know they can talk to you.",
        "q60_2": "Give them space while respecting whatever they need to feel comfortable.",
        "q60_3": "Stay by their side and show through your actions that you care.",
        "q60_4": "Listen patiently and try to understand what they are going through."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 60 POINTS
    # --------------------------------------------------------

    points = QUESTION_60_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 60
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly after hearing Daniel's answer.\n\n"
        "She feels that Daniel understands that being there for "
        "someone means respecting their needs while making sure "
        "they know they are not alone."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_61(call.message.chat.id)

#سؤال 61

# ============================================================
# QUESTION 61
# ============================================================

def send_question_61(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 61
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a thoughtful smile.\n\n"
        "She asks him what he thinks helps a relationship "
        "remain strong when both people are changing and growing."
    )

    # --------------------------------------------------------
    # QUESTION 61 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about how your feelings and priorities change.",
            callback_data="q61_1"
        ),
        types.InlineKeyboardButton(
            "2. Encouraging each other to grow while respecting your differences.",
            callback_data="q61_2"
        ),
        types.InlineKeyboardButton(
            "3. Staying loyal and continuing to support each other through changes.",
            callback_data="q61_3"
        ),
        types.InlineKeyboardButton(
            "4. Talking regularly and making sure you still understand each other.",
            callback_data="q61_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 61 IMAGE
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

        print("Question 61 image status:", response.status_code)
        print(
            "Question 61 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question61.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 61 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 61 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps a relationship "
        "remain strong when both people are changing and growing.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 61 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q61_")
)
def question_61_answer(call):

    answers = {
        "q61_1": "Being honest about how your feelings and priorities change.",
        "q61_2": "Encouraging each other to grow while respecting your differences.",
        "q61_3": "Staying loyal and continuing to support each other through changes.",
        "q61_4": "Talking regularly and making sure you still understand each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 61 POINTS
    # --------------------------------------------------------

    points = QUESTION_61_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 61
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She feels that Daniel understands that people can grow "
        "and change without losing the connection they have built."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_62(call.message.chat.id)

#سؤال 62

# ============================================================
# QUESTION 62
# ============================================================

def send_question_62(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 62
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as the conversation continues.\n\n"
        "She asks him what he thinks is the best way to keep "
        "a relationship meaningful over time."
    )

    # --------------------------------------------------------
    # QUESTION 62 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Keep being honest about your feelings and never take each other for granted.",
            callback_data="q62_1"
        ),
        types.InlineKeyboardButton(
            "2. Give each other freedom to grow while maintaining your own interests.",
            callback_data="q62_2"
        ),
        types.InlineKeyboardButton(
            "3. Continue making an effort and showing that you care through your actions.",
            callback_data="q62_3"
        ),
        types.InlineKeyboardButton(
            "4. Keep communicating, listening, and discovering new things about each other.",
            callback_data="q62_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 62 IMAGE
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

        print("Question 62 image status:", response.status_code)
        print(
            "Question 62 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question62.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 62 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 62 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "keep a relationship meaningful over time.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 62 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q62_")
)
def question_62_answer(call):

    answers = {
        "q62_1": "Keep being honest about your feelings and never take each other for granted.",
        "q62_2": "Give each other freedom to grow while maintaining your own interests.",
        "q62_3": "Continue making an effort and showing that you care through your actions.",
        "q62_4": "Keep communicating, listening, and discovering new things about each other."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 62 POINTS
    # --------------------------------------------------------

    points = QUESTION_62_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 62
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly.\n\n"
        "She feels that Daniel understands that keeping a "
        "relationship meaningful takes honesty, effort, freedom, "
        "and genuine interest in each other."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_63(call.message.chat.id)

#سؤال 63

# ============================================================
# QUESTION 63
# ============================================================

def send_question_63(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 63
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a gentle smile.\n\n"
        "She asks him what he thinks is most important when "
        "two people are trying to build a relationship based on trust."
    )

    # --------------------------------------------------------
    # QUESTION 63 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest, even when the truth is uncomfortable.",
            callback_data="q63_1"
        ),
        types.InlineKeyboardButton(
            "2. Respecting each other's choices and personal boundaries.",
            callback_data="q63_2"
        ),
        types.InlineKeyboardButton(
            "3. Keeping promises and being dependable when it matters.",
            callback_data="q63_3"
        ),
        types.InlineKeyboardButton(
            "4. Listening carefully and making sure both people feel understood.",
            callback_data="q63_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 63 IMAGE
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

        print("Question 63 image status:", response.status_code)
        print(
            "Question 63 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question63.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 63 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 63 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is most important "
        "when two people are trying to build a relationship "
        "based on trust.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 63 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q63_")
)
def question_63_answer(call):

    answers = {
        "q63_1": "Being honest, even when the truth is uncomfortable.",
        "q63_2": "Respecting each other's choices and personal boundaries.",
        "q63_3": "Keeping promises and being dependable when it matters.",
        "q63_4": "Listening carefully and making sure both people feel understood."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 63 POINTS
    # --------------------------------------------------------

    points = QUESTION_63_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 63
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She feels that Daniel understands that trust is built "
        "through honesty, respect, reliability, and genuine understanding."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_64(call.message.chat.id)


#سؤال 64

# ============================================================
# QUESTION 64
# ============================================================

def send_question_64(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 64
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as they continue talking.\n\n"
        "She asks him what he thinks is the best way to keep "
        "a relationship healthy when life becomes unpredictable."
    )

    # --------------------------------------------------------
    # QUESTION 64 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest about what is happening and how you feel.",
            callback_data="q64_1"
        ),
        types.InlineKeyboardButton(
            "2. Stay flexible and give each other room to adapt.",
            callback_data="q64_2"
        ),
        types.InlineKeyboardButton(
            "3. Stay loyal and support each other when things get difficult.",
            callback_data="q64_3"
        ),
        types.InlineKeyboardButton(
            "4. Talk things through and try to understand how the changes affect both people.",
            callback_data="q64_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 64 IMAGE
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

        print("Question 64 image status:", response.status_code)
        print(
            "Question 64 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question64.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 64 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 64 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to keep "
        "a relationship healthy when life becomes unpredictable.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 64 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q64_")
)
def question_64_answer(call):

    answers = {
        "q64_1": "Be honest about what is happening and how you feel.",
        "q64_2": "Stay flexible and give each other room to adapt.",
        "q64_3": "Stay loyal and support each other when things get difficult.",
        "q64_4": "Talk things through and try to understand how the changes affect both people."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 64 POINTS
    # --------------------------------------------------------

    points = QUESTION_64_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 64
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods with a thoughtful smile.\n\n"
        "She feels that Daniel understands that unexpected "
        "changes are easier to handle when two people remain "
        "honest, flexible, supportive, and willing to communicate."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_65(call.message.chat.id)

#سؤال 65

# ============================================================
# QUESTION 65
# ============================================================

def send_question_65(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 65
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel and pauses for a moment.\n\n"
        "She asks him what he thinks makes someone feel "
        "comfortable enough to open up about their worries."
    )

    # --------------------------------------------------------
    # QUESTION 65 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Knowing they can speak honestly without being judged.",
            callback_data="q65_1"
        ),
        types.InlineKeyboardButton(
            "2. Knowing they can talk when they are ready without pressure.",
            callback_data="q65_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing someone will stay beside them and offer support.",
            callback_data="q65_3"
        ),
        types.InlineKeyboardButton(
            "4. Knowing someone will listen carefully and try to understand.",
            callback_data="q65_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 65 IMAGE
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

        print("Question 65 image status:", response.status_code)
        print(
            "Question 65 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question65.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 65 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 65 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks makes someone feel "
        "comfortable enough to open up about their worries.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 65 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q65_")
)
def question_65_answer(call):

    answers = {
        "q65_1": "Knowing they can speak honestly without being judged.",
        "q65_2": "Knowing they can talk when they are ready without pressure.",
        "q65_3": "Knowing someone will stay beside them and offer support.",
        "q65_4": "Knowing someone will listen carefully and try to understand."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 65 POINTS
    # --------------------------------------------------------

    points = QUESTION_65_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 65
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly.\n\n"
        "She appreciates Daniel's answer and feels that he "
        "understands how important trust, patience, support, "
        "and understanding are when someone is opening up."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_66(call.message.chat.id)


#سؤال 66

# ============================================================
# QUESTION 66
# ============================================================

def send_question_66(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 66
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a warm smile.\n\n"
        "She asks him what he thinks is most important when "
        "two people disagree about something that really matters."
    )

    # --------------------------------------------------------
    # QUESTION 66 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Be honest about your opinion while remaining respectful.",
            callback_data="q66_1"
        ),
        types.InlineKeyboardButton(
            "2. Give each person time and space to think independently.",
            callback_data="q66_2"
        ),
        types.InlineKeyboardButton(
            "3. Focus on finding a solution that supports both people.",
            callback_data="q66_3"
        ),
        types.InlineKeyboardButton(
            "4. Listen carefully and try to understand why the other person feels that way.",
            callback_data="q66_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 66 IMAGE
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

        print("Question 66 image status:", response.status_code)
        print(
            "Question 66 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question66.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 66 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 66 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is most important "
        "when two people disagree about something that really matters.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 66 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q66_")
)
def question_66_answer(call):

    answers = {
        "q66_1": "Be honest about your opinion while remaining respectful.",
        "q66_2": "Give each person time and space to think independently.",
        "q66_3": "Focus on finding a solution that supports both people.",
        "q66_4": "Listen carefully and try to understand why the other person feels that way."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 66 POINTS
    # --------------------------------------------------------

    points = QUESTION_66_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 66
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily nods thoughtfully.\n\n"
        "She feels that Daniel understands that disagreements "
        "do not have to create distance when both people are "
        "willing to communicate with honesty and respect."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_67(call.message.chat.id)

#سؤال 67

# ============================================================
# QUESTION 67
# ============================================================

def send_question_67(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 67
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as the conversation continues.\n\n"
        "She asks him what he thinks makes a relationship feel "
        "safe and comfortable over the long term."
    )

    # --------------------------------------------------------
    # QUESTION 67 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Knowing that both people can always be honest with each other.",
            callback_data="q67_1"
        ),
        types.InlineKeyboardButton(
            "2. Knowing that both people can maintain their independence and boundaries.",
            callback_data="q67_2"
        ),
        types.InlineKeyboardButton(
            "3. Knowing that both people will be dependable and supportive.",
            callback_data="q67_3"
        ),
        types.InlineKeyboardButton(
            "4. Knowing that both people can talk openly and feel understood.",
            callback_data="q67_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 67 IMAGE
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

        print("Question 67 image status:", response.status_code)
        print(
            "Question 67 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question67.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 67 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 67 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks makes a relationship "
        "feel safe and comfortable over the long term.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 67 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q67_")
)
def question_67_answer(call):

    answers = {
        "q67_1": "Knowing that both people can always be honest with each other.",
        "q67_2": "Knowing that both people can maintain their independence and boundaries.",
        "q67_3": "Knowing that both people will be dependable and supportive.",
        "q67_4": "Knowing that both people can talk openly and feel understood."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 67 POINTS
    # --------------------------------------------------------

    points = QUESTION_67_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 67
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly.\n\n"
        "She feels that Daniel understands that a lasting "
        "relationship needs honesty, independence, reliability, "
        "and open communication."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_68(call.message.chat.id)

#سؤال 68

# ============================================================
# QUESTION 68
# ============================================================

def send_question_68(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 68
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel with a curious smile.\n\n"
        "She asks him what he thinks is the best way to show "
        "someone that their feelings are important to you."
    )

    # --------------------------------------------------------
    # QUESTION 68 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Tell them honestly that their feelings matter to you.",
            callback_data="q68_1"
        ),
        types.InlineKeyboardButton(
            "2. Respect their feelings even when you see things differently.",
            callback_data="q68_2"
        ),
        types.InlineKeyboardButton(
            "3. Show through your actions that you are there for them.",
            callback_data="q68_3"
        ),
        types.InlineKeyboardButton(
            "4. Listen carefully and give them your full attention.",
            callback_data="q68_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 68 IMAGE
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

        print("Question 68 image status:", response.status_code)
        print(
            "Question 68 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question68.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 68 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 68 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is the best way to "
        "show someone that their feelings are important to you.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 68 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q68_")
)
def question_68_answer(call):

    answers = {
        "q68_1": "Tell them honestly that their feelings matter to you.",
        "q68_2": "Respect their feelings even when you see things differently.",
        "q68_3": "Show through your actions that you are there for them.",
        "q68_4": "Listen carefully and give them your full attention."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 68 POINTS
    # --------------------------------------------------------

    points = QUESTION_68_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 68
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles and nods.\n\n"
        "She appreciates Daniel's answer and feels that he "
        "understands how important it is to make another person "
        "feel heard, respected, and cared for."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_69(call.message.chat.id)


#سؤال 69

# ============================================================
# QUESTION 69
# ============================================================

def send_question_69(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 69
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily looks at Daniel thoughtfully.\n\n"
        "She asks him what he thinks helps two people stay "
        "close when they have very different personalities."
    )

    # --------------------------------------------------------
    # QUESTION 69 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being honest about your differences and accepting each other.",
            callback_data="q69_1"
        ),
        types.InlineKeyboardButton(
            "2. Giving each other enough freedom to be yourselves.",
            callback_data="q69_2"
        ),
        types.InlineKeyboardButton(
            "3. Focusing on the things you enjoy doing together.",
            callback_data="q69_3"
        ),
        types.InlineKeyboardButton(
            "4. Talking openly and trying to understand each other's perspective.",
            callback_data="q69_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 69 IMAGE
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

        print("Question 69 image status:", response.status_code)
        print(
            "Question 69 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question69.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:
        print("QUESTION 69 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 69 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks helps two people stay "
        "close when they have very different personalities.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 69 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q69_")
)
def question_69_answer(call):

    answers = {
        "q69_1": "Being honest about your differences and accepting each other.",
        "q69_2": "Giving each other enough freedom to be yourselves.",
        "q69_3": "Focusing on the things you enjoy doing together.",
        "q69_4": "Talking openly and trying to understand each other's perspective."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 69 POINTS
    # --------------------------------------------------------

    points = QUESTION_69_SCORES.get(call.data)

    if points:

        for category, value in points.items():
            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # TEXT AFTER QUESTION 69
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,
        "Emily smiles warmly.\n\n"
        "She feels that Daniel understands that differences "
        "do not have to create distance when two people respect "
        "each other and make an effort to understand one another."
    )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    send_question_70(call.message.chat.id)

#----------------------------- الحسبة النهائية
# ============================================================
# FINAL CHARACTER SELECTION
# ============================================================

def choose_final_character(user_id):

    scores = user_scores[user_id]

    # ============================================================
    # CHARACTER SCORES
    # ============================================================

    character_scores = {
        "Emily": scores["Emily"],
        "Sophie": scores["Sophie"],
        "Grace": scores["Grace"],
        "Charlotte": scores["Charlotte"]
    }

    # ============================================================
    # FIND HIGHEST CHARACTER
    # ============================================================

    highest_character = max(
        character_scores,
        key=character_scores.get
    )

    highest_score = character_scores[highest_character]

    # ============================================================
    # FIND SECOND HIGHEST SCORE
    # ============================================================

    other_scores = [
        score
        for character, score in character_scores.items()
        if character != highest_character
    ]

    second_highest_score = max(other_scores)

    difference = highest_score - second_highest_score

    # ============================================================
    # MAIN RULES
    # ============================================================

    if highest_score > 60 and difference > 4:

        # --------------------------------------------------------
        # EMILY
        # --------------------------------------------------------

        if (
            highest_character == "Emily"
            and scores["ECompatibility"] > 75
            and scores["Honest"] >= 60
            and scores["Independence"] > 50
        ):
            return "Emily"

        # --------------------------------------------------------
        # SOPHIE
        # --------------------------------------------------------

        if (
            highest_character == "Sophie"
            and scores["SCompatibility"] > 75
            and scores["Honest"] >= 55
            and scores["Independence"] > 60
        ):
            return "Sophie"

        # --------------------------------------------------------
        # GRACE
        # --------------------------------------------------------

        if (
            highest_character == "Grace"
            and scores["GCompatibility"] > 75
            and scores["Honest"] >= 65
            and scores["Independence"] > 50
        ):
            return "Grace"

        # --------------------------------------------------------
        # CHARLOTTE
        # --------------------------------------------------------

        if (
            highest_character == "Charlotte"
            and scores["CCompatibility"] > 75
            and scores["Honest"] >= 60
            and scores["Independence"] > 65
        ):
            return "Charlotte"

    # ============================================================
    # BACKUP RULES
    # ============================================================

    emily = scores["Emily"]
    sophie = scores["Sophie"]
    grace = scores["Grace"]
    charlotte = scores["Charlotte"]

    independence = scores["Independence"]
    honest = scores["Honest"]

    # ============================================================
    # BACKUP RULE 1
    #
    # ALL FOUR CHARACTERS BETWEEN 30 AND 50
    #
    # Winner = "Four Friends"
    # ============================================================

    if (
        30 <= emily <= 50
        and 30 <= sophie <= 50
        and 30 <= grace <= 50
        and 30 <= charlotte <= 50
    ):
        return "Four Friends"

    # ============================================================
    # BACKUP RULE 2
    #
    # ALL FOUR CHARACTERS LESS THAN 40
    #
    # Winner = "No Friends or New Beginning"
    # ============================================================

    if (
        emily < 40
        and sophie < 40
        and grace < 40
        and charlotte < 40
    ):
        return "No Friends or New Beginning"

    # ============================================================
    # BACKUP RULE 3
    #
    # ANY CHARACTER ABOVE 45
    #
    # Choose ALL characters above 45.
    #
    # Example:
    #
    # Emily = 50
    # Sophie = 60
    # Grace = 40
    # Charlotte = 55
    #
    # Result:
    # Emily + Sophie + Charlotte Close Friends
    # ============================================================

    characters_above_45 = [
        character
        for character, score in character_scores.items()
        if score > 45
    ]

    if characters_above_45:
        return " + ".join(characters_above_45) + " Close Friends"

    # ============================================================
    # BACKUP RULE 4
    #
    # INDEPENDENCE LESS THAN 40
    #
    # Winner = "Missed Opportunities"
    # ============================================================

    if independence < 40:
        return "Missed Opportunities"

    # ============================================================
    # BACKUP RULE 5
    #
    # ALL FOUR CHARACTERS LESS THAN 50
    # AND INDEPENDENCE MORE THAN 75
    #
    # Winner = "Independent- Positive"
    # ============================================================

    if (
        emily < 50
        and sophie < 50
        and grace < 50
        and charlotte < 50
        and independence > 75
    ):
        return "Independent- Positive"

    # ============================================================
    # BACKUP RULE 6
    #
    # INDEPENDENCE LESS THAN 55
    # AND HONEST LESS THAN 50
    #
    # Winner = "Independent- Positive"
    # ============================================================

    if (
        independence < 55
        and honest < 50
    ):
        return "Independent- Positive"

    # ============================================================
    # FINAL BACKUP
    #
    # Anything else
    #
    # Winner = "Solo End"
    # ============================================================

    return "Solo End"



#سؤال 70

# ============================================================
# QUESTION 70 POINTS
# ============================================================

QUESTION_70_SCORES = {

    # --------------------------------------------------------
    # ANSWER 1 - HONESTY
    # --------------------------------------------------------

    "q70_1": {
        "Emily": 3,
        "Honest": 5,
        "ECompatibility": 3
    },

    # --------------------------------------------------------
    # ANSWER 2 - INDEPENDENCE
    # --------------------------------------------------------

    "q70_2": {
        "Sophie": 3,
        "Independence": 5,
        "SCompatibility": 3
    },

    # --------------------------------------------------------
    # ANSWER 3 - SUPPORT / DEPENDABILITY
    # --------------------------------------------------------

    "q70_3": {
        "Grace": 3,
        "GCompatibility": 3,
        "Honest": 2
    },

    # --------------------------------------------------------
    # ANSWER 4 - COMMUNICATION / UNDERSTANDING
    # --------------------------------------------------------

    "q70_4": {
        "Charlotte": 3,
        "CCompatibility": 3,
        "Honest": 2
    }
}


# ============================================================
# QUESTION 70
# ============================================================

def send_question_70(chat_id):

    # --------------------------------------------------------
    # TEXT BEFORE QUESTION 70
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily smiles at Daniel as they continue their conversation.\n\n"
        "She asks him what he thinks is most important when "
        "two people want to build a lasting relationship together."
    )

    # --------------------------------------------------------
    # QUESTION 70 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Being completely honest about your feelings and intentions.",
            callback_data="q70_1"
        ),
        types.InlineKeyboardButton(
            "2. Respecting each other's independence and personal goals.",
            callback_data="q70_2"
        ),
        types.InlineKeyboardButton(
            "3. Being dependable and supporting each other through difficult times.",
            callback_data="q70_3"
        ),
        types.InlineKeyboardButton(
            "4. Communicating openly and making sure both people feel understood.",
            callback_data="q70_4"
        )
    )

    # --------------------------------------------------------
    # QUESTION 70 IMAGE
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

        print("Question 70 image status:", response.status_code)
        print(
            "Question 70 image type:",
            response.headers.get("Content-Type")
        )

        photo = BytesIO(response.content)
        photo.name = "question70.jpg"

        bot.send_photo(
            chat_id,
            photo
        )

    except Exception as e:

        print("QUESTION 70 IMAGE ERROR:", e)

        bot.send_message(
            chat_id,
            "The question image could not be loaded, "
            "but you can still continue."
        )

    # --------------------------------------------------------
    # QUESTION 70 TEXT
    # --------------------------------------------------------

    bot.send_message(
        chat_id,
        "Emily asks Daniel what he thinks is most important "
        "when two people want to build a lasting relationship together.\n\n"
        "Choose Daniel's response:",
        reply_markup=keyboard
    )


# ============================================================
# QUESTION 70 ANSWER
# ============================================================

@bot.callback_query_handler(
    func=lambda call: call.data.startswith("q70_")
)
def question_70_answer(call):

    answers = {

        "q70_1":
            "Being completely honest about your feelings and intentions.",

        "q70_2":
            "Respecting each other's independence and personal goals.",

        "q70_3":
            "Being dependable and supporting each other through difficult times.",

        "q70_4":
            "Communicating openly and making sure both people feel understood."
    }

    answer = answers.get(call.data)

    user_id = call.from_user.id

    # --------------------------------------------------------
    # ADD QUESTION 70 POINTS
    # --------------------------------------------------------

    points = QUESTION_70_SCORES.get(call.data)

    if points:

        for category, value in points.items():

            user_scores[user_id][category] += value

    bot.answer_callback_query(call.id)

    # --------------------------------------------------------
    # SHOW SELECTED ANSWER + CURRENT SCORES
    # --------------------------------------------------------

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

        # --------------------------------------------------------
    # TEXT AFTER QUESTION 70
    # --------------------------------------------------------

    bot.send_message(
        call.message.chat.id,

        "Emily smiles warmly.\n\n"
        "She feels that Daniel understands that a lasting "
        "relationship requires honesty, independence, support, "
        "and meaningful communication."
    )

    # ============================================================
    # FIND FINAL WINNER
    # ============================================================

    winner = choose_final_character(user_id)

    # ============================================================
    # SHOW FINAL WINNER
    # ============================================================

    if winner:

        bot.send_message(
            call.message.chat.id,
            f"🎉 Your final match is {winner}!\n\n"
            f"Your strongest connection is with {winner}."
        )

    else:

        bot.send_message(
            call.message.chat.id,
            "No character qualified based on the final "
            "score requirements."
        )


# ============================================================
# START BOT
# ============================================================

print("Bot is running...")

bot.delete_webhook(drop_pending_updates=True)
bot.infinity_polling()
