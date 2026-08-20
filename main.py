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

IMAGE_URL = "https://i.ibb.co/Jjp6nm43/Emily-2.jpg"


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
        "A girl was standing beneath an umbrella.\n"
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
        "Emily is the student council president.\n"
        "She’s intelligent, organized, polite, and seemingly impossible to upset.\n"
        "Teachers trust her.\n"
        "Students depend on her.\n"
        "But Emily has spent years trying to become the person everyone expects her to be.\n"
        "She secretly wonders what would happen if she stopped being “the responsible one\n"
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
    IMAGE_URL2 = "https://i.ibb.co/qM7vXkX3/Sophie-2.jpg"

    # --------------------------------------------------------
    # QUESTION 2 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL2,
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
    IMAGE_URL3 = "https://i.ibb.co/9Hs8vKZL/Grace.jpg"
    # --------------------------------------------------------
    # QUESTION 3 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL3,
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
        "Next Morning..\n\n"
        "Charlotte, who spoke with Daniel two or three times, left her table and asked Daniel"
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

    IMAGE_URL4 = "https://i.ibb.co/BH22kYWK/Charlotte-2.jpg"
    # --------------------------------------------------------
    # QUESTION 4 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL4,
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
        "Later..."
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
        "Daniel discovers that Emily stayed at school late. "
    )

    # --------------------------------------------------------
    # QUESTION 5 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Ask whether she’s okay.",
            callback_data="q5_1"
        ),
        types.InlineKeyboardButton(
            "2. Leave her alone.",
            callback_data="q5_2"
        ),
        types.InlineKeyboardButton(
            "3. Offer to help.",
            callback_data="q5_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask why she feels responsible for everything.",
            callback_data="q5_4"
        )
    )

    IMAGE_URL5 = "https://i.ibb.co/BKPbsjXF/Emily.jpg"
    # --------------------------------------------------------
    # QUESTION 5 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL5,
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
        "Daniel discovers that Emily stayed at school late.  "
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
        "q5_1": "Ask whether she’s okay.",
        "q5_2": "Leave her alone.",
        "q5_3": "Offer to help.",
        "q5_4": "Ask why she feels responsible for everything."
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
        "Sophie Williams\n"
		"Sophie is cheerful, athletic, and extremely competitive.\n"
        "She plays football for the school and seems to know everyone.\n"
        "She becomes one of Daniel’s first friends.\n"
        "She dislikes complicated conversations and tends to turn uncomfortable situations\n"
        "into jokes.\n"
        "But beneath her confidence is a fear of being left behind as everyone grows older."
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
        "Sophie lost an important football match and disagreed with a close friend. "
    )

    # --------------------------------------------------------
    # QUESTION 6 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Comfort her.",
            callback_data="q6_1"
        ),
        types.InlineKeyboardButton(
            "2. Tell her she’ll win next time.",
            callback_data="q6_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask whether she wants to talk.",
            callback_data="q6_3"
        ),
        types.InlineKeyboardButton(
            "4. Give her some space.",
            callback_data="q6_4"
        )
    )
    IMAGE_URL6 = "https://i.ibb.co/KcNzCBqs/Sophie-3.jpg"
    # --------------------------------------------------------
    # QUESTION 6 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL6,
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
        "Sophie lost an important football match and disagreed with a close friend."
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
        "q6_1": "Comfort her.",
        "q6_2": "Tell her she’ll win next time.",
        "q6_3": "Ask whether she wants to talk.",
        "q6_4": "Give her some space."
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
        "Later..."
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
        "Grace invited Daniel to see the library."
        "She goes to search for a book\n\n"
        "Grace accidentally leaves her notebook open. "
        "Daniel sees a story about someone who sounds suspiciously like him."
    )

    # --------------------------------------------------------
    # QUESTION 7 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Read it.",
            callback_data="q7_1"
        ),
        types.InlineKeyboardButton(
            "2. Close the notebook.",
            callback_data="q7_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask Grace about it.",
            callback_data="q7_3"
        ),
        types.InlineKeyboardButton(
            "4. Pretend not to notice.",
            callback_data="q7_4"
        )
    )
    IMAGE_URL7 = "https://i.ibb.co/SXfZhq47/Grace-2.jpg"
    # --------------------------------------------------------
    # QUESTION 7 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL7,
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
        "q7_1": "Read it.",
        "q7_2": "Close the notebook.",
        "q7_3": "Ask Grace about it.",
        "q7_4": "Pretend not to notice."
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
        "Grace is watching Daniel.\n\n"
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
        "After talking with Grace, Daniel meets Charlotte. "
        "They had a conversation .\n\n"
        "Charlotte asks Daniel what he would do if he was in her place. "
        "she receives criticism from her parents about her grades."
    )

    # --------------------------------------------------------
    # QUESTION 8 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Tell her to ignore them.",
            callback_data="q8_1"
        ),
        types.InlineKeyboardButton(
            "2. Ask what she wants.",
            callback_data="q8_2"
        ),
        types.InlineKeyboardButton(
            "3. Tell her to work harder.",
            callback_data="q8_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her she doesn’t need to meet everyone’s expectations",
            callback_data="q8_4"
        )
    )
    IMAGE_URL8 = "https://i.ibb.co/60MsTMqD/Charlotte.jpg"
    # --------------------------------------------------------
    # QUESTION 8 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL8,
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
        "q8_1": "Tell her to ignore them.",
        "q8_2": "Ask what she wants.",
        "q8_3": "Tell her to work harder.",
        "q8_4": "Tell her she doesn’t need to meet everyone’s expectations."
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
		"Charlotte Reed is the daughter of a successful local businessman.\n\n"
        "She is confident, sophisticated, and determined to attend a prestigious university.\n\n"
        "Unlike the others, she seems to have her entire future planned.\n\n"
        "But her plans aren't entirely hers.\n\n"
        "Her parents have already decided what career she should pursue.\n\n"
        "Charlotte begins wondering whether the life she is building actually belongs to her."
        
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
		"a few days later..."
        "Daniel has some free time after school.\n\n"
    )

    # --------------------------------------------------------
    # QUESTION 9 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Visit Emily.",
            callback_data="q9_1"
        ),
        types.InlineKeyboardButton(
            "2. Watch Sophie train.",
            callback_data="q9_2"
        ),
        types.InlineKeyboardButton(
            "3. Visit Grace in the library.",
            callback_data="q9_3"
        ),
        types.InlineKeyboardButton(
            "4. Work with Charlotte.",
            callback_data="q9_4"
        )
    )
    IMAGE_URL9 = "https://i.ibb.co/JWmjm2Yy/Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 9 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL9,
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
        "What are you going to do?",
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
        "q9_1": "Visit Emily.",
        "q9_2": "Watch Sophie train.",
        "q9_3": "Visit Grace in the library.",
        "q9_4": "Work with Charlotte."
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
        "You spent a good time that day. \n\n"
        "Next week, Daniel go to school"
        "Someone asks Daniel which girl he finds most interesting."
    )

    # --------------------------------------------------------
    # QUESTION 10 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Emily.",
            callback_data="q10_1"
        ),
        types.InlineKeyboardButton(
            "2. Sophie",
            callback_data="q10_2"
        ),
        types.InlineKeyboardButton(
            "3. Grace.",
            callback_data="q10_3"
        ),
        types.InlineKeyboardButton(
            "4. Charlotte.",
            callback_data="q10_4"
        )
    )
    IMAGE_URL10 = "https://i.ibb.co/JWmjm2Yy/Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 10 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL10,
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
        "q10_1": "Emily.",
        "q10_2": "Sophie.",
        "q10_3": "Grace.",
        "q10_4": "Charlotte."
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
        "The autumn term becomes busier.\n\n"
        "The school announces its annual Winter Gala.\n\n"
        "Each girl becomes involved.\n\n"
        "Emily organizes it.\n"
        "Sophie volunteers for the entertainment.\n"
        "Grace is asked to write the event program.\n"
        "Charlotte becomes responsible for fundraising.\n\n"
        "Daniel is asked to help all four.\n\n"
        "But tensions begin appearing.\n\n"
        "Emily and Charlotte disagree about how money should be spent.\n"
        "Sophie feels ignored.\n"
        "Grace worries that nobody will read her writing.\n"
        "Daniel realizes that helping everyone isn't always possible."
		
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
        "Emily asks Daniel to take responsibility for an important task.\n\n"
    )

    # --------------------------------------------------------
    # QUESTION 11 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Accept.",
            callback_data="q11_1"
        ),
        types.InlineKeyboardButton(
            "2. Ask for instructions.",
            callback_data="q11_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask someone else to help.",
            callback_data="q11_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell Emily she is taking on too much.",
            callback_data="q11_4"
        )
    )
    IMAGE_URL11 = "https://i.ibb.co/Jjp6nm43/Emily-2.jpg"
    # --------------------------------------------------------
    # QUESTION 11 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL11,
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
        "q11_1": "Accept.",
        "q11_2": "Ask for instructions.",
        "q11_3": "Ask someone else to help.",
        "q11_4": "Tell Emily she is taking on too much."
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
        "Sophie is sad. She said nobody appreciates her work.\n\n"
    )

    # --------------------------------------------------------
    # QUESTION 12 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Tell her they do.",
            callback_data="q12_1"
        ),
        types.InlineKeyboardButton(
            "2. Ask why she feels that way.",
            callback_data="q12_2"
        ),
        types.InlineKeyboardButton(
            "3. Tell her to stop worrying.",
            callback_data="q12_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her that recognition isn’t everything.",
            callback_data="q12_4"
        )
    )
    IMAGE_URL12 = "https://i.ibb.co/KcNzCBqs/Sophie-3.jpg"
    # --------------------------------------------------------
    # QUESTION 12 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL12,
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
        "q12_1": "Tell her they do.",
        "q12_2": "Ask why she feels that way.",
        "q12_3": "Tell her to stop worrying.",
        "q12_4": "Tell her that recognition isn’t everything."
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
        "Grace Bennett spends most of her free time in the library.\n\n"
        "She's an excellent writer but refuses to show anyone her stories.\n\n"
        "Grace observes people constantly and remembers tiny details about them.\n\n"
        "She is comfortable communicating through writing but struggles with direct conversations."
    )

    # --------------------------------------------------------
    # QUESTION 13 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q13_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q13_2"
        ),
        types.InlineKeyboardButton(
            "3. Explain what you liked.",
            callback_data="q13_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask what the story means to her.",
            callback_data="q13_4"
        )
    )
    IMAGE_URL13 = "https://i.ibb.co/9Hs8vKZL/Grace.jpg"
    # --------------------------------------------------------
    # QUESTION 13 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL13,
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
        "Grace asks whether Daniel likes her writing."
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
        "q13_1": "Yes.",
        "q13_2": "No.",
        "q13_3": "Explain what you liked.",
        "q13_4": "Ask what the story means to her."
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
        "Daniel is resting after Sport class. "
        "Charlotte approaches him and asks..."
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
        "Charlotte asks Daniel whether ambition is a good thing."
    )

    # --------------------------------------------------------
    # QUESTION 14 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Definitely.",
            callback_data="q14_1"
        ),
        types.InlineKeyboardButton(
            "2. Not always.",
            callback_data="q14_2"
        ),
        types.InlineKeyboardButton(
            "3. It depends on what you’re willing to sacrifice.",
            callback_data="q14_3"
        ),
        types.InlineKeyboardButton(
            "4. Ambition is good if the goal is actually yours.",
            callback_data="q14_4"
        )
    )
    IMAGE_URL14 = "https://i.ibb.co/60MsTMqD/Charlotte.jpg"
    # --------------------------------------------------------
    # QUESTION 14 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL14,
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
        "q14_1": "Definitely.",
        "q14_2": "Not always.",
        "q14_3": "It depends on what you’re willing to sacrifice.",
        "q14_4": "Ambition is good if the goal is actually yours."
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
        "After a long day...\n\n"
        "Daniel discovers that Emily made a mistake. "
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


    # --------------------------------------------------------
    # QUESTION 15 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Hide it.",
            callback_data="q15_1"
        ),
        types.InlineKeyboardButton(
            "2. Tell her immediately.",
            callback_data="q15_2"
        ),
        types.InlineKeyboardButton(
            "3. Help fix it.",
            callback_data="q15_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask what she wants to do.",
            callback_data="q15_4"
        )
    )
    IMAGE_URL15 = "https://i.ibb.co/BKPbsjXF/Emily.jpg"
    # --------------------------------------------------------
    # QUESTION 15 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL15,
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
        "q15_1": "Hide it.",
        "q15_2": "Tell her immediately.",
        "q15_3": "Help fix it.",
        "q15_4": "Ask what she wants to do."
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
		"Emily feels comfortable talking with Daniel now.\n\n"
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
		"Daniel walks and meets Sophie.\n\n"
        "Sophie is actually very happy this time.\n\n"
        "Sophie challenges Daniel to a race."
    )

    # --------------------------------------------------------
    # QUESTION 16 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Accept.",
            callback_data="q16_1"
        ),
        types.InlineKeyboardButton(
            "2. Refuse.",
            callback_data="q16_2"
        ),
        types.InlineKeyboardButton(
            "3. Accept despite knowing she’ll win.",
            callback_data="q16_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask why she suddenly wants to compete.",
            callback_data="q16_4"
        )
    )
    IMAGE_URL16 = "https://i.ibb.co/wFkcxySg/Sophie.jpg"
    # --------------------------------------------------------
    # QUESTION 16 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL16,
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
        "q16_1": "Accept.",
        "q16_2": "Refuse.",
        "q16_3": "Accept despite knowing she’ll win.",
        "q16_4": "Ask why she suddenly wants to compete."
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
        "That girl was very fast\n\n"
        "That's what I remember from those days.."
    )

    # ----------------------------------------t----------------
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
        "Daniel : I went to the school too early today. \n\n"
        "I meet Grace in front of her class. "
        "Grace asks Daniel to read one of her stories."
    )

    # --------------------------------------------------------
    # QUESTION 17 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Read it immediately.",
            callback_data="q17_1"
        ),
        types.InlineKeyboardButton(
            "2. Ask whether she’s sure.",
            callback_data="q17_2"
        ),
        types.InlineKeyboardButton(
            "3. Read it and give honest feedback.",
            callback_data="q17_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her you’ll read it whenever she’s ready.",
            callback_data="q17_4"
        )
    )
    IMAGE_URL17 = "https://i.ibb.co/9Hs8vKZL/Grace.jpg"
    # --------------------------------------------------------
    # QUESTION 17 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL17,
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
        "q17_1": "Read it immediately.",
        "q17_2": "Ask whether she’s sure.",
        "q17_3": "Read it and give honest feedback.",
        "q17_4": "Tell her you’ll read it whenever she’s ready."
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
        "Grace looks thoughtful after hearing Daniel's answer.\n"

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
        "Charlotte is following Daniel after class. "
        "After a conversation about our teachers, she asks him what he thinks success means."
    )

    # --------------------------------------------------------
    # QUESTION 18 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Money.",
            callback_data="q18_1"
        ),
        types.InlineKeyboardButton(
            "2. Achievement.",
            callback_data="q18_2"
        ),
        types.InlineKeyboardButton(
            "3. Happiness.",
            callback_data="q18_3"
        ),
        types.InlineKeyboardButton(
            "4. Being able to choose your own life.",
            callback_data="q18_4"
        )
    )
    IMAGE_URL18 = "https://i.ibb.co/0pyy5z4V/Charlotte-2.jpg"
    # --------------------------------------------------------
    # QUESTION 18 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL18,
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
        "q18_1": "Money.",
        "q18_2": "Achievement.",
        "q18_3": "Happiness.",
        "q18_4": "Being able to choose your own life."
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
        "Two girls asked you for help."
		"Daniel has promised to help two girls at the same time."
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
        "Daniel: What to do now?\n\n"
    )

    # --------------------------------------------------------
    # QUESTION 19 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Choose one.",
            callback_data="q19_1"
        ),
        types.InlineKeyboardButton(
            "2. Try to do both.",
            callback_data="q19_2"
        ),
        types.InlineKeyboardButton(
            "3. Explain the situation honestly.",
            callback_data="q19_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask them to work together.",
            callback_data="q19_4"
        )
    )
    IMAGE_URL19 = "https://i.ibb.co/JWmjm2Yy/Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 19 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL19,
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
        "Choose what to do?",
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
        "q19_1": "Choose one.",
        "q19_2": "Try to do both.",
        "q19_3": "Explain the situation honestly.",
        "q19_4": "Ask them to work together."
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
        "The Winter Gala is approaching.\n\n"
        "Who does Daniel spend the evening helping? "
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


    # --------------------------------------------------------
    # QUESTION 20 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Emily.",
            callback_data="q20_1"
        ),
        types.InlineKeyboardButton(
            "2. Sophie.",
            callback_data="q20_2"
        ),
        types.InlineKeyboardButton(
            "3. Grace.",
            callback_data="q20_3"
        ),
        types.InlineKeyboardButton(
            "4. Charlotte.",
            callback_data="q20_4"
        )
    )
    IMAGE_URL20 = "https://i.ibb.co/JWmjm2Yy/Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 20 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL20,
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
        "Who does Daniel spend the evening helping?",
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
        "q20_1": "Emily.",
        "q20_2": "Sophie.",
        "q20_3": "Grace.",
        "q20_4": "Charlotte."
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
        "The Winter Gala becomes a turning point.\n\n"
        "Daniel discovers that Grace's writing has been selected for the school magazine. "
        "She is terrified.\n\n"
        "Charlotte's fundraising project becomes unexpectedly successful. "
        "Emily receives praise from the teachers. "
        "Sophie performs in front of the entire school.\n\n"
        "For one evening, everyone seems happy.\n\n"
        "But after the event, Sophie tells Daniel:\n\n"
        "\"Everyone keeps talking about where we're going after school.\"\n\n"
        "She looks toward the empty hall.\n\n"
        "\"I don't know if I want everything to change.\""
    )

    # --------------------------------------------------------
    # QUESTION 21 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Nothing has to change.",
            callback_data="q21_1"
        ),
        types.InlineKeyboardButton(
            "2. Change isn’t necessarily bad.",
            callback_data="q21_2"
        ),
        types.InlineKeyboardButton(
            "3. I’ll always be your friend.",
            callback_data="q21_3"
        ),
        types.InlineKeyboardButton(
            "4. What are you actually afraid of?",
            callback_data="q21_4"
        )
    )

    IMAGE_URL21 = "https://i.ibb.co/7m5h3f3/Early-Morning.jpg"

    # --------------------------------------------------------
    # QUESTION 21 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL21,
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
        "q21_1": "Nothing has to change.",
        "q21_2": "Change isn’t necessarily bad.",
        "q21_3": "I’ll always be your friend.",
        "q21_4": "What are you actually afraid of?"
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
        "The next day...\n\n"
        "Daniel meets Emily."
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
        "Emily asks Daniel whether she should run for student council president again."
    )

    # --------------------------------------------------------
    # QUESTION 22 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Encourage her.",
            callback_data="q22_1"
        ),
        types.InlineKeyboardButton(
            "2. Tell her to take a break.",
            callback_data="q22_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask whether she wants it.",
            callback_data="q22_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask whether she’s doing it for herself.",
            callback_data="q22_4"
        )
    )
    IMAGE_URL22 = "https://i.ibb.co/TMLX0df4/Emily-3.jpg"
    # --------------------------------------------------------
    # QUESTION 22 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL22,
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
        "q22_1": "Encourage her.",
        "q22_2": "Tell her to take a break.",
        "q22_3": "Ask whether she wants it.",
        "q22_4": "Ask whether she’s doing it for herself."
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
        "a good advice.\n\n"
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
        "“Daniel walks into the school and listens to Grace’s story, which receives criticism."
    )

    # --------------------------------------------------------
    # QUESTION 23 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Defend her.",
            callback_data="q23_1"
        ),
        types.InlineKeyboardButton(
            "2. Tell her to improve it.",
            callback_data="q23_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask whether she agrees with the criticism.",
            callback_data="q23_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her one opinion doesn’t define her writing.",
            callback_data="q23_4"
        )
    )
    IMAGE_URL23 = "https://i.ibb.co/JWmjm2Yy/Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 23 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL23,
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
        "q23_1": "Defend her.",
        "q23_2": "Tell her to improve it.",
        "q23_3": "Ask whether she agrees with the criticism.",
        "q23_4": "Tell her one opinion doesn’t define her writing."
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
		"Charlotte is sitting outside the classroom, reviewing her notes, "
        "when he walks over and places a coffee beside her.\n\n"
        "Daniel: “You looked like you needed this.” \n\n"
        "She looks at the cup, then at him.\n\n"
        "Charlotte: “You bought me coffee?” \n"
        "Daniel: “Don't make it a big deal.”"
		"Daniel sets in a nearby chair and they started talking"
        "Charlotte likes that the conversation has become honest "
        "and thoughtful."
		"Charlotte’s parents want her to pursue a career she doesn’t want."
		"She asks for Daniel’s opinion."
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


    # --------------------------------------------------------
    # QUESTION 24 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Tell her to rebel.",
            callback_data="q24_1"
        ),
        types.InlineKeyboardButton(
            "2. Tell her to obey.",
            callback_data="q24_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask what she wants.",
            callback_data="q24_3"
        ),
        types.InlineKeyboardButton(
            "4. Help her think through the consequences.",
            callback_data="q24_4"
        )
    )
    IMAGE_URL24 = "https://i.ibb.co/LXjSHvmZ/Charlotte-3.jpg"
    # --------------------------------------------------------
    # QUESTION 24 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL24,
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
        "q24_1": "Tell her to rebel.",
        "q24_2": "Tell her to obey.",
        "q24_3": "Ask what she wants.",
        "q24_4": "Help her think through the consequences."
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
        "NEXT morining, in the school \n\n"
        "Daniel :I remembered something important "
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

    # --------------------------------------------------------
    # QUESTION 25 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Have it immediately.",
            callback_data="q25_1"
        ),
        types.InlineKeyboardButton(
            "2. Wait for the right moment.",
            callback_data="q25_2"
        ),
        types.InlineKeyboardButton(
            "3. Write a letter.",
            callback_data="q25_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask the person to talk privately.",
            callback_data="q25_4"
        )
    )
    IMAGE_URL25 = "https://i.ibb.co/JWmjm2Yy/Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 25 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL25,
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
        "Daniel realizes he has been avoiding an important conversation. "
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
        "q25_1": "Have it immediately.",
        "q25_2": "Wait for the right moment.",
        "q25_3": "Write a letter.",
        "q25_4": "Ask the person to talk privately."
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
        "Daniel meets Emily. Emily looks at Daniel with a thoughtful smile.\n\n"
        "She asks him  what he thinks her biggest weakness is"
    )

    # --------------------------------------------------------
    # QUESTION 26 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. She worries too much.",
            callback_data="q26_1"
        ),
        types.InlineKeyboardButton(
            "2. She works too hard.",
            callback_data="q26_2"
        ),
        types.InlineKeyboardButton(
            "3. She cares too much about others’ opinions.",
            callback_data="q26_3"
        ),
        types.InlineKeyboardButton(
            "4. She doesn’t allow herself to make mistakes.",
            callback_data="q26_4"
        )
    )
    IMAGE_URL3 = "https://i.ibb.co/BKPbsjXF/Emily.jpg"
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
        "Emily asks Daniel what he thinks her biggest weakness is.\n\n"
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
        "q26_1": "She worries too much.",
        "q26_2": "She works too hard.",
        "q26_3": "She cares too much about others’ opinions.",
        "q26_4": "She doesn’t allow herself to make mistakes."
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
        "She feels that Daniel's answer says a lot about their relationship. "
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
        "“The next afternoon, after school, Sophie comes to meet Daniel. "
        "Sophie asks whether Daniel would miss her if she moved away."
    )

    # --------------------------------------------------------
    # QUESTION 27 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q27_1"
        ),
        types.InlineKeyboardButton(
            "2. Definitely.",
            callback_data="q27_2"
        ),
        types.InlineKeyboardButton(
            "3. Of course.",
            callback_data="q27_3"
        ),
        types.InlineKeyboardButton(
            "4. I don’t want to imagine that.",
            callback_data="q27_4"
        )
    )
    IMAGE_URL27 = "https://i.ibb.co/wFkcxySg/Sophie.jpg"
    # --------------------------------------------------------
    # QUESTION 27 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL27,
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
        #"Sophie asks whether Daniel would miss her if she moved away. "
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
        "q27_1": "Yes.",
        "q27_2": "Definitely.",
        "q27_3": "Of course.",
        "q27_4": "I don’t want to imagine that."
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
        "Daniel: Today, I decided to go to the library.  \n\n"

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

    # --------------------------------------------------------
    # QUESTION 28 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. I like books.",
            callback_data="q28_1"
        ),
        types.InlineKeyboardButton(
            "2. I like talking to you.",
            callback_data="q28_2"
        ),
        types.InlineKeyboardButton(
            "3. It’s quiet.",
            callback_data="q28_3"
        ),
        types.InlineKeyboardButton(
            "4. I feel comfortable here.",
            callback_data="q28_4"
        )
    )
    IMAGE_URL28 = "https://i.ibb.co/9Hs8vKZL/Grace.jpg"
    # --------------------------------------------------------
    # QUESTION 28 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL28,
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
        "Grace asks why Daniel keeps visiting the library. "
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
        "q28_1": "I like books.",
        "q28_2": "I like talking to you.",
        "q28_3": "It’s quiet.",
        "q28_4": "I feel comfortable here."
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

    # --------------------------------------------------------
    # QUESTION 29 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Safe.",
            callback_data="q29_1"
        ),
        types.InlineKeyboardButton(
            "2. Uncertain.",
            callback_data="q29_2"
        ),
        types.InlineKeyboardButton(
            "3. The one that makes me happier.",
            callback_data="q29_3"
        ),
        types.InlineKeyboardButton(
            "4. The one I chose for myself.",
            callback_data="q29_4"
        )
    )
    IMAGE_URL29 = "https://i.ibb.co/0pyy5z4V/Charlotte-2.jpg"
    # --------------------------------------------------------
    # QUESTION 29 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL29,
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
        "When I get back to my classroom."
        "Charlotte asks whether Daniel would choose a safe future or an uncertain one.\n\n"
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
        "q29_1": "Safe.",
        "q29_2": "Uncertain.",
        "q29_3": "The one that makes me happier.",
        "q29_4": "The one I chose for myself."
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
        "The school year reaches its midpoint.\n\n"
        "Daniel must decide whether to pursue one particular relationship more seriously."
        "Who should I build a future with?"
    )

    # --------------------------------------------------------
    # QUESTION 30 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Emily.",
            callback_data="q30_1"
        ),
        types.InlineKeyboardButton(
            "2. Sophie.",
            callback_data="q30_2"
        ),
        types.InlineKeyboardButton(
            "3. Grace.",
            callback_data="q30_3"
        ),
        types.InlineKeyboardButton(
            "4. Charlotte.",
            callback_data="q30_4"
        )
    )
    IMAGE_URL30 = "https://i.ibb.co/361jJv2/General-1.jpg"
    # --------------------------------------------------------
    # QUESTION 30 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL30,
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
        "Daniel must decide whether to pursue one particular relationship more seriously. \n\n"
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
        "q30_1": "Emily",
        "q30_2": "Sophie.",
        "q30_3": "Grace.",
        "q30_4": "Charlotte."
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
        "Spring arrives.\n\n"
        "The school begins discussing university applications and future careers. "
        "The girls start facing difficult decisions.\n\n"
        "Emily realizes she doesn't actually want the university her parents chose.\n"
        "Sophie receives an opportunity to join a regional football academy.\n"
        "Grace is offered a chance to publish her writing.\n"
        "Charlotte finally tells her parents that she wants a different career.\n\n"
        "Daniel finds himself wondering what his future holds "
        "and whether their future has a place for him."
    )

    # --------------------------------------------------------
    # QUESTION 31 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Tell her to accept.",
            callback_data="q31_1"
        ),
        types.InlineKeyboardButton(
            "2. Tell her to stay.",
            callback_data="q31_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask what she wants.",
            callback_data="q31_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her not to reject it because she’s afraid of change.",
            callback_data="q31_4"
        )
    )
    IMAGE_URL31 = "https://i.ibb.co/qM7vXkX3/Sophie-2.jpg"
    # --------------------------------------------------------
    # QUESTION 31 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL31,
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
        "Sophie is offered a football opportunity in another city. "
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
        "q31_1": "Tell her to accept.",
        "q31_2": "Tell her to stay.",
        "q31_3": "Ask what she wants.",
        "q31_4": "Tell her not to reject it because she’s afraid of change."
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
        "Sophie smiles after hearing Daniel's answer.\n\n"
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
        "Daniel meets Grace. \n\n"
        "Grace is offered publication but worries people will criticize her."
    )

    # --------------------------------------------------------
    # QUESTION 32 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Encourage her.",
            callback_data="q32_1"
        ),
        types.InlineKeyboardButton(
            "2. Tell her not to worry.",
            callback_data="q32_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask what she is afraid of.",
            callback_data="q32_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her that being understood matters more than being universally liked.",
            callback_data="q32_4"
        )
    )
    IMAGE_URL32 = "https://i.ibb.co/9Hs8vKZL/Grace.jpg"
    # --------------------------------------------------------
    # QUESTION 32 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL32,
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
        "q32_1": "Encourage her.",
        "q32_2": "Tell her not to worry.",
        "q32_3": "Ask what she is afraid of.",
        "q32_4": "Tell her that being understood matters more than being universally liked."
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
        "She asks whether Daniel thinks she is selfish for changing her plans."
    )

    # --------------------------------------------------------
    # QUESTION 33 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q33_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q33_2"
        ),
        types.InlineKeyboardButton(
            "3. Everyone deserves to choose their future.",
            callback_data="q33_3"
        ),
        types.InlineKeyboardButton(
            "4. It depends on how she handles the people affected.",
            callback_data="q33_4"
        )
    )
    IMAGE_URL33 = "https://i.ibb.co/TMLX0df4/Emily-3.jpg"
    # --------------------------------------------------------
    # QUESTION 33 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL33,
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
        "Emily asks whether Daniel thinks she is selfish for changing her plans. \n\n"
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
        "q33_1": "Yes.",
        "q33_2": "No.",
        "q33_3": "Everyone deserves to choose their future.",
        "q33_4": "It depends on how she handles the people affected."
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
        "looking at emotional stuff. "
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


    # --------------------------------------------------------
    # QUESTION 34 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Support her.",
            callback_data="q34_1"
        ),
        types.InlineKeyboardButton(
            "2. Stay out of it.",
            callback_data="q34_2"
        ),
        types.InlineKeyboardButton(
            "3. Help her prepare.",
            callback_data="q34_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her the decision has to be hers.",
            callback_data="q34_4"
        )
    )
    IMAGE_URL34 = "https://i.ibb.co/0pyy5z4V/Charlotte-2.jpg"
    # --------------------------------------------------------
    # QUESTION 34 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL34,
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
        "Charlotte finally confronts her parents. "
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
        "q34_1": "Support her.",
        "q34_2": "Stay out of it.",
        "q34_3": "Help her prepare.",
        "q34_4": "Tell her the decision has to be hers."
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
        "Charlotte went to her home and had a conversation with her parents.\n\n"
        "She feels that disagreements do not have to create "
        "distance when they are one family "
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
        "Daniel: The following week… surprisingly, I was offered a scholarship.\n\n"
    )

    # --------------------------------------------------------
    # QUESTION 35 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Accept immediately.",
            callback_data="q35_1"
        ),
        types.InlineKeyboardButton(
            "2. Reject it.",
            callback_data="q35_2"
        ),
        types.InlineKeyboardButton(
            "3. Research it carefully.",
            callback_data="q35_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask how it fits into his long-term plans.",
            callback_data="q35_4"
        )
    )
    IMAGE_URL35 = "https://i.ibb.co/7m5h3f3/Early-Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 35 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL35,
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
        "Daniel is offered a scholarship. "
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
        "q35_1": "Accept immediately.",
        "q35_2": "Reject it.",
        "q35_3": "Research it carefully.",
        "q35_4": "Ask how it fits into his long-term plans."
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
        "This probably will be a hard decision. \n\n"
        "That's what I thought at the time.."
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
        "After school, Sophie invites Daniel to go somewhere nearby with her. \n\n"
        "After buying some food.."
    )

    # --------------------------------------------------------
    # QUESTION 36 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q36_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q36_2"
        ),
        types.InlineKeyboardButton(
            "3. I want you to do what makes you happy.",
            callback_data="q36_3"
        ),
        types.InlineKeyboardButton(
            "4. I want you to stay, but I don’t want you to give up your dream.",
            callback_data="q36_4"
        )
    )
    IMAGE_URL36 = "https://i.ibb.co/xqHNy8xd/Sophie-4.jpg"
    # --------------------------------------------------------
    # QUESTION 36 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL36,
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
        "Sophie asks Daniel whether he wants her to stay. \n\n"
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
        "q36_1": "Yes.",
        "q36_2": "No.",
        "q36_3": "I want you to do what makes you happy.",
        "q36_4": "I want you to stay, but I don’t want you to give up your dream."
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
		"Daniel: I answered her like that. I couldn't tell if she was happy about the answer.  \n"
        "We spent a lovely afternoon walking around town. Eventually, everyone went home."
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
        "Daniel: I meet Grace in the library. I found a nice book that week.. \n\n"
        "After some reading.."
        "Grace asks me whether he thinks her stories are too personal."
    )

    # --------------------------------------------------------
    # QUESTION 37 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q37_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q37_2"
        ),
        types.InlineKeyboardButton(
            "3. Sometimes.",
            callback_data="q37_3"
        ),
        types.InlineKeyboardButton(
            "4. Personal stories can help other people feel understood.",
            callback_data="q37_4"
        )
    )
    IMAGE_URL37 = "https://i.ibb.co/9Hs8vKZL/Grace.jpg"
    # --------------------------------------------------------
    # QUESTION 37 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL37,
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
        "Grace asks Daniel whether he thinks her stories are too personal.\n\n"
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
        "q37_1": "Yes.",
        "q37_2": "No.",
        "q37_3": "Sometimes.",
        "q37_4": "Personal stories can help other people feel understood."
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
        "Later....   \n\n"
        "I meet Charlotte "
    )

    # --------------------------------------------------------
    # QUESTION 38 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Of course.",
            callback_data="q38_1"
        ),
        types.InlineKeyboardButton(
            "2. I’d be disappointed.",
            callback_data="q38_2"
        ),
        types.InlineKeyboardButton(
            "3. I’d respect your decision.",
            callback_data="q38_3"
        ),
        types.InlineKeyboardButton(
            "4. I’d respect you more for making your own decision.",
            callback_data="q38_4"
        )
    )
    IMAGE_URL38 = "https://i.ibb.co/60MsTMqD/Charlotte.jpg"
    # --------------------------------------------------------
    # QUESTION 38 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL38,
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
        "Charlotte asks whether Daniel would still respect her if she abandoned her original career plan.  \n\n"
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
        "q38_1": "Of course.",
        "q38_2": "I’d be disappointed.",
        "q38_3": "I’d respect your decision.",
        "q38_4": "I’d respect you more for making your own decision."
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
        "I answer her that answer. \n\n"
        "She looks a bit happy after hearing that."
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
        "After few days...\n\n"

    )

    # --------------------------------------------------------
    # QUESTION 39 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Correct them.",
            callback_data="q39_1"
        ),
        types.InlineKeyboardButton(
            "2. Ignore it.",
            callback_data="q39_2"
        ),
        types.InlineKeyboardButton(
            "3. Explain himself.",
            callback_data="q39_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask what they believe he feels.",
            callback_data="q39_4"
        )
    )
    IMAGE_URL39 = "https://i.ibb.co/JWmjm2Yy/Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 39 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL39,
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
        "Daniel realizes someone has misunderstood his feelings. "
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
        "q39_1": "Correct them.",
        "q39_2": "Ignore it.",
        "q39_3": "Explain himself.",
        "q39_4": "Ask what they believe he feels."
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



    # --------------------------------------------------------
    # QUESTION 40 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Emily.",
            callback_data="q40_1"
        ),
        types.InlineKeyboardButton(
            "2. Sophie.",
            callback_data="q40_2"
        ),
        types.InlineKeyboardButton(
            "3. Grace.",
            callback_data="q40_3"
        ),
        types.InlineKeyboardButton(
            "4. Charlotte.",
            callback_data="q40_4"
        )
    )
    IMAGE_URL40 = "https://i.ibb.co/361jJv2/General-1.jpg"
    # --------------------------------------------------------
    # QUESTION 40 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL40,
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
        "Daniel must choose someone to accompany him to a school event.\n\n"
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
        "q40_1": "Emily.",
        "q40_2": "Sophie.",
        "q40_3": "Grace.",
        "q40_4": "Charlotte."
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
        "Summer changes everything.\n\n"
        "The four girls begin preparing for their final year.\n\n"
        "Daniel's relationships have become complicated.\n\n"
        "There are friendships that might become romance.\n"
        "There are feelings that were never spoken.\n"
        "There are dreams that require people to leave.\n\n"
        "And Daniel realizes that love isn't simply about choosing the person he likes most.\n\n"
        "It is also about asking whether their lives can genuinely move forward together."
    )

    # --------------------------------------------------------
    # QUESTION 41 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q41_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q41_2"
        ),
        types.InlineKeyboardButton(
            "3. Sometimes.",
            callback_data="q41_3"
        ),
        types.InlineKeyboardButton(
            "4. Sacrifice shouldn’t mean losing yourself.",
            callback_data="q41_4"
        )
    )
    IMAGE_URL41 = "https://i.ibb.co/BKPbsjXF/Emily.jpg"
    # --------------------------------------------------------
    # QUESTION 41 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL41,
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
        "Emily asks Daniel whether he believes relationships require sacrifice. \n\n"
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
        "q41_1": "Yes.",
        "q41_2": "No.",
        "q41_3": "Sometimes.",
        "q41_4": "Sacrifice shouldn’t mean losing yourself."
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
        "She likes hearing how Daniel thinks about those things "
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
        "Afterwards, I met Sophie.."
    )

    # --------------------------------------------------------
    # QUESTION 42 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q42_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q42_2"
        ),
        types.InlineKeyboardButton(
            "3. I don’t know.",
            callback_data="q42_3"
        ),
        types.InlineKeyboardButton(
            "4. If both people genuinely wanted it.",
            callback_data="q42_4"
        )
    )
    IMAGE_URL42 = "https://i.ibb.co/qM7vXkX3/Sophie-2.jpg"
    # --------------------------------------------------------
    # QUESTION 42 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL42,
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
        "Sophie asks whether Daniel would maintain a long-distance relationship. \n\n"
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
        "q42_1": "Yes.",
        "q42_2": "No.",
        "q42_3": "I don’t know.",
        "q42_4": "If both people genuinely wanted it."
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


    # --------------------------------------------------------
    # QUESTION 43 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q43_1"
        ),
        types.InlineKeyboardButton(
            "2. Probably.",
            callback_data="q43_2"
        ),
        types.InlineKeyboardButton(
            "3. Only if she keeps practicing.",
            callback_data="q43_3"
        ),
        types.InlineKeyboardButton(
            "4. She should decide what success means to her.",
            callback_data="q43_4"
        )
    )
    IMAGE_URL43 = "https://i.ibb.co/9Hs8vKZL/Grace.jpg"
    # --------------------------------------------------------
    # QUESTION 43 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL43,
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
        "Grace asks Daniel whether he believes she can become a successful writer. \n\n"
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
        "q43_1": "Yes.",
        "q43_2": "Probably.",
        "q43_3": "Only if she keeps practicing.",
        "q43_4": "She should decide what success means to her."
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
        "Grace nods thoughtfully.\n\n"
        "She appreciates Daniel's answer and wonders how "
        "he would handle his life."
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
        "In the classroom, I meet Charlotte.. \n\n"
    )

    # --------------------------------------------------------
    # QUESTION 44 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q44_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q44_2"
        ),
        types.InlineKeyboardButton(
            "3. Definitely.",
            callback_data="q44_3"
        ),
        types.InlineKeyboardButton(
            "4. You seem more like yourself now.",
            callback_data="q44_4"
        )
    )
    IMAGE_URL44 = "https://i.ibb.co/gLmXNcn9/Charlotte-4.jpg"
    # --------------------------------------------------------
    # QUESTION 44 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL44,
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
        "Charlotte asks Daniel whether he thinks she has changed. \n\n"
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
        "q44_1": "Yes.",
        "q44_2": "No.",
        "q44_3": "Definitely.",
        "q44_4": "You seem more like yourself now."
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
        "She listens carefully and nods.\n\n"
        "She feels that Daniel understands her more . "
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


    # --------------------------------------------------------
    # QUESTION 45 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Confess.",
            callback_data="q45_1"
        ),
        types.InlineKeyboardButton(
            "2. Wait.",
            callback_data="q45_2"
        ),
        types.InlineKeyboardButton(
            "3. Write a letter.",
            callback_data="q45_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask whether she has noticed.",
            callback_data="q45_4"
        )
    )
    IMAGE_URL45 = "https://i.ibb.co/7m5h3f3/Early-Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 45 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL45,
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
        "Daniel has feelings for someone but hasn’t told her. \n\n"
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
        "q45_1": "Confess.",
        "q45_2": "Wait.",
        "q45_3": "Write a letter.",
        "q45_4": "Ask whether she has noticed."
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

    # --------------------------------------------------------
    # QUESTION 46 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q46_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q46_2"
        ),
        types.InlineKeyboardButton(
            "3. I care about you deeply.",
            callback_data="q46_3"
        ),
        types.InlineKeyboardButton(
            "4. I don’t want to answer until I’m certain.",
            callback_data="q46_4"
        )
    )
    IMAGE_URL46 = "https://i.ibb.co/7m5h3f3/Early-Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 46 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL46,
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
        "A girl asks Daniel whether he loves her. \n\n"
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
        "q46_1": "Yes.",
        "q46_2": "No.",
        "q46_3": "I care about you deeply.",
        "q46_4": "I don’t want to answer until I’m certain."
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


    # --------------------------------------------------------
    # QUESTION 47 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Ask her about it.",
            callback_data="q47_1"
        ),
        types.InlineKeyboardButton(
            "2. Pretend not to know.",
            callback_data="q47_2"
        ),
        types.InlineKeyboardButton(
            "3. Tell her he doesn’t want her to leave.",
            callback_data="q47_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask what she wants her future to look like.",
            callback_data="q47_4"
        )
    )
    IMAGE_URL47 = "https://i.ibb.co/JWmjm2Yy/Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 47 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL47,
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
        "Daniel discovers that a girl may leave the country after graduation.\n\n"
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
        "q47_1": "Ask her about it.",
        "q47_2": "Pretend not to know.",
        "q47_3": "Tell her he doesn’t want her to leave.",
        "q47_4": "Ask what she wants her future to look like."
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


    # --------------------------------------------------------
    # QUESTION 48 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Romance.",
            callback_data="q48_1"
        ),
        types.InlineKeyboardButton(
            "2. Career.",
            callback_data="q48_2"
        ),
        types.InlineKeyboardButton(
            "3. Both.",
            callback_data="q48_3"
        ),
        types.InlineKeyboardButton(
            "4. Neither should require abandoning the other.",
            callback_data="q48_4"
        )
    )
    IMAGE_URL48 = "https://i.ibb.co/Q34Zr43F/Class-1.jpg"
    # --------------------------------------------------------
    # QUESTION 48 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL48,
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
        "Daniel must decide whether to prioritize romance or his own future.\n\n"
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
        "q48_1": "Romance.",
        "q48_2": "Career.",
        "q48_3": "Both.",
        "q48_4": "Neither should require abandoning the other."
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



    # --------------------------------------------------------
    # QUESTION 49 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Loyalty.",
            callback_data="q49_1"
        ),
        types.InlineKeyboardButton(
            "2. Honesty.",
            callback_data="q49_2"
        ),
        types.InlineKeyboardButton(
            "3. Understanding.",
            callback_data="q49_3"
        ),
        types.InlineKeyboardButton(
            "4. Someone who chooses her own life while allowing me to choose mine.",
            callback_data="q49_4"
        )
    )
    IMAGE_URL49 = "https://i.ibb.co/7m5h3f3/Early-Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 49 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL49,
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
        "Someone asks Daniel what he expects from a future partner.\n\n"
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
        "q49_1": "Loyalty.",
        "q49_2": "Honesty.",
        "q49_3": "Understanding.",
        "q49_4": "Someone who chooses her own life while allowing me to choose mine."
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

    # --------------------------------------------------------
    # QUESTION 50 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. The memories.",
            callback_data="q50_1"
        ),
        types.InlineKeyboardButton(
            "2. The friendships.",
            callback_data="q50_2"
        ),
        types.InlineKeyboardButton(
            "3. The lessons.",
            callback_data="q50_3"
        ),
        types.InlineKeyboardButton(
            "4. The person he has become.",
            callback_data="q50_4"
        )
    )
    IMAGE_URL50 = "https://i.ibb.co/7m5h3f3/Early-Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 50 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL50,
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
        "Daniel looks back on his first year at Westbridge. "
        "What matters most? \n\n"
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
        "q50_1": "The memories.",
        "q50_2": "The friendships.",
        "q50_3": "The lessons.",
        "q50_4": "The person he has become."
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
        "The final year begins.\n\n"
        "University applications arrive.\n"
        "Graduation becomes real.\n\n"
        "The four girls begin moving toward completely different futures.\n\n"
        "Emily wants to study law.\n"
        "Sophie wants to pursue football.\n"
        "Grace wants to study literature.\n"
        "Charlotte wants to study business—but on her own terms.\n\n"
        "Daniel has his own future to consider.\n\n"
        "For the first time, he understands that choosing someone doesn't mean "
        "possessing them.\n"
        "It means asking whether two people can build something together."
    )

    # --------------------------------------------------------
    # QUESTION 51 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q51_1"
        ),
        types.InlineKeyboardButton(
            "2. I’d tell you if I disagreed.",
            callback_data="q51_2"
        ),
        types.InlineKeyboardButton(
            "3. I’d support your decision.",
            callback_data="q51_3"
        ),
        types.InlineKeyboardButton(
            "4. I’d help you think it through, but the decision is yours.",
            callback_data="q51_4"
        )
    )
    IMAGE_URL51 = "https://i.ibb.co/dw9wZM49/Emily-4.jpg"
    # --------------------------------------------------------
    # QUESTION 51 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL51,
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
        "Daniel: I was helping Emily with some of her tasks in the town.  "
        "Then she asked..		\n\n"
		"..."
		"Emily asks whether Daniel would support her if she chose a difficult university."
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
        "q51_1": "Yes.",
        "q51_2": "I’d tell you if I disagreed.",
        "q51_3": "I’d support your decision.",
        "q51_4": "I’d help you think it through, but the decision is yours."
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
        "understands the importance of patience "
        "and honest communication in life."
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

    # --------------------------------------------------------
    # QUESTION 52 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Celebrate.",
            callback_data="q52_1"
        ),
        types.InlineKeyboardButton(
            "2. Worry about the distance.",
            callback_data="q52_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask what she wants.",
            callback_data="q52_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her she should never abandon her dream for someone else.",
            callback_data="q52_4"
        )
    )
    IMAGE_URL52 = "https://i.ibb.co/qM7vXkX3/Sophie-2.jpg"
    # --------------------------------------------------------
    # QUESTION 52 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL52,
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
        "I met Sophie in the school.. \n"
        "She shares some important news with me about her life. \n\n"
		"Sophie receives an important football offer."
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
        "q52_1": "Celebrate.",
        "q52_2": "Worry about the distance.",
        "q52_3": "Ask what she wants.",
        "q52_4": "Tell her she should never abandon her dream for someone else."
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


    # --------------------------------------------------------
    # QUESTION 53 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Ask to read it.",
            callback_data="q53_1"
        ),
        types.InlineKeyboardButton(
            "2. Wait until she offers a copy.",
            callback_data="q53_2"
        ),
        types.InlineKeyboardButton(
            "3. Tell her you’re proud.",
            callback_data="q53_3"
        ),
        types.InlineKeyboardButton(
            "4. Ask what the story taught her about herself.",
            callback_data="q53_4"
        )
    )
    IMAGE_URL53 = "https://i.ibb.co/M5WsgtPQ/Grace-3.png"
    # --------------------------------------------------------
    # QUESTION 53 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL53,
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
        "Grace finishes her first novel.\n"
        "how to ask for it? \n\n"
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
        "q53_1": "Ask to read it.",
        "q53_2": "Wait until she offers a copy.",
        "q53_3": "Tell her you’re proud.",
        "q53_4": "Ask what the story taught her about herself."
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

    # --------------------------------------------------------
    # QUESTION 54 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q54_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q54_2"
        ),
        types.InlineKeyboardButton(
            "3. It can if people stop communicating.",
            callback_data="q54_3"
        ),
        types.InlineKeyboardButton(
            "4. Only when ambition becomes more important than the person.",
            callback_data="q54_4"
        )
    )
    IMAGE_URL54 = "https://i.ibb.co/gLmXNcn9/Charlotte-4.jpg"
    # --------------------------------------------------------
    # QUESTION 54 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL54,
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
        "Charlotte asks Daniel whether ambition can damage relationships. \n\n"
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
        "q54_1": "Yes.",
        "q54_2": "No.",
        "q54_3": "It can if people stop communicating.",
        "q54_4": "Only when ambition becomes more important than the person."
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
        "Change nods with a warm smile.\n\n"
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


    # --------------------------------------------------------
    # QUESTION 55 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. The prestigious one.",
            callback_data="q55_1"
        ),
        types.InlineKeyboardButton(
            "2. The nearby one.",
            callback_data="q55_2"
        ),
        types.InlineKeyboardButton(
            "3. The one with the best career prospects.",
            callback_data="q55_3"
        ),
        types.InlineKeyboardButton(
            "4. The one that feels right for him.",
            callback_data="q55_4"
        )
    )
    IMAGE_URL55 = "https://i.ibb.co/7m5h3f3/Early-Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 55 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL55,
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
        "Daniel must choose between two universities.\n\n"
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
        "q55_1": "The prestigious one.",
        "q55_2": "The nearby one.",
        "q55_3": "The one with the best career prospects.",
        "q55_4": "The one that feels right for him."
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
        "She asks him what he thinks two people should do."
        "when they want different things from their future."
    )

    # --------------------------------------------------------
    # QUESTION 56 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q56_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q56_2"
        ),
        types.InlineKeyboardButton(
            "3. Maybe.",
            callback_data="q56_3"
        ),
        types.InlineKeyboardButton(
            "4. Only if the relationship remained strong as both people changed.",
            callback_data="q56_4"
        )
    )
    IMAGE_URL56 = "https://i.ibb.co/dw9wZM49/Emily-4.jpg"
    # --------------------------------------------------------
    # QUESTION 56 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL56,
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
        "Then, she asks..\n "
        "She asks whether Daniel could imagine marrying someone someday.\n\n"
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
        "q56_1": "Yes.",
        "q56_2": "No.",
        "q56_3": "Maybe.",
        "q56_4": "Only if the relationship remained strong as both people changed."
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



    # --------------------------------------------------------
    # QUESTION 57 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q57_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q57_2"
        ),
        types.InlineKeyboardButton(
            "3. Sometimes.",
            callback_data="q57_3"
        ),
        types.InlineKeyboardButton(
            "4. Only if they learn to see each other as adults.",
            callback_data="q57_4"
        )
    )
    IMAGE_URL57 = "https://i.ibb.co/qM7vXkX3/Sophie-2.jpg"
    # --------------------------------------------------------
    # QUESTION 57 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL57,
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
        "Sophie asks whether childhood friends can become life partners. \n\n"
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
        "q57_1": "Yes.",
        "q57_2": "No.",
        "q57_3": "Sometimes.",
        "q57_4": "Only if they learn to see each other as adults."
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


    # --------------------------------------------------------
    # QUESTION 58 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q58_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q58_2"
        ),
        types.InlineKeyboardButton(
            "3. Not necessarily.",
            callback_data="q58_3"
        ),
        types.InlineKeyboardButton(
            "4. The strongest relationships might be the quiet ones.",
            callback_data="q58_4"
        )
    )
    IMAGE_URL58 = "https://i.ibb.co/Qt75KQM/Grace-4.jpg"
    # --------------------------------------------------------
    # QUESTION 58 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL58,
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
        "Grace asks Daniel whether love needs to be dramatic. \n\n"
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
        "q58_1": "Yes.",
        "q58_2": "No.",
        "q58_3": "Not necessarily.",
        "q58_4": "The strongest relationships might be the quiet ones."
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

    # --------------------------------------------------------
    # QUESTION 59 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q59_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q59_2"
        ),
        types.InlineKeyboardButton(
            "3. Temporarily.",
            callback_data="q59_3"
        ),
        types.InlineKeyboardButton(
            "4. I’d rather find a way for both people to grow.",
            callback_data="q59_4"
        )
    )
    IMAGE_URL59 = "https://i.ibb.co/gLmXNcn9/Charlotte-4.jpg"
    # --------------------------------------------------------
    # QUESTION 59 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL59,
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
        "Charlotte asks Daniel whether he would ever give up his ambitions for someone he loved. \n\n"
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
        "q59_1": "Yes.",
        "q59_2": "No.",
        "q59_3": "Temporarily.",
        "q59_4": "I’d rather find a way for both people to grow."
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


    # --------------------------------------------------------
    # QUESTION 60 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. A successful one.",
            callback_data="q60_1"
        ),
        types.InlineKeyboardButton(
            "2. A peaceful one.",
            callback_data="q60_2"
        ),
        types.InlineKeyboardButton(
            "3. An exciting one.",
            callback_data="q60_3"
        ),
        types.InlineKeyboardButton(
            "4. One where I don’t have to become someone else.",
            callback_data="q60_4"
        )
    )
    IMAGE_URL60 = "https://i.ibb.co/7m5h3f3/Early-Morning.jpg"
    # --------------------------------------------------------
    # QUESTION 60 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL60,
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
        "Daniel asks himself:\n"
        "“What kind of future do I want?”\n\n"
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
        "q60_1": "A successful one.",
        "q60_2": "A peaceful one.",
        "q60_3": "An exciting one.",
        "q60_4": "One where I don’t have to become someone else."
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
        "The final day arrives.\n\n"
        "The school hall is decorated.\n"
        "Everyone is dressed formally.\n"
        "Teachers give speeches.\n"
        "Students take photographs.\n\n"
        "The four girls stand together for one final photograph.\n\n"
        "Daniel looks at them.\n\n"
        "One of them may become the person who remains beside him.\n"
        "Or perhaps none of them will.\n\n"
        "For the first time, Daniel realizes that both possibilities can be good."
    )

    # --------------------------------------------------------
    # QUESTION 61 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Emily.",
            callback_data="q61_1"
        ),
        types.InlineKeyboardButton(
            "2. Sophie.",
            callback_data="q61_2"
        ),
        types.InlineKeyboardButton(
            "3. Grace.",
            callback_data="q61_3"
        ),
        types.InlineKeyboardButton(
            "4. Charlotte.",
            callback_data="q61_4"
        )
    )
    IMAGE_URL61 = "https://i.ibb.co/tMtWZRRG/General-3.jpg"
    # --------------------------------------------------------
    # QUESTION 61 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL61,
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
        "Who does Daniel look for first after the graduation ceremony?\n\n"
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
        "q61_1": "Emily.",
        "q61_2": "Sophie.",
        "q61_3": "Grace.",
        "q61_4": "Charlotte."
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


    # --------------------------------------------------------
    # QUESTION 62 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Emily.",
            callback_data="q62_1"
        ),
        types.InlineKeyboardButton(
            "2. Sophie.",
            callback_data="q62_2"
        ),
        types.InlineKeyboardButton(
            "3. Grace.",
            callback_data="q62_3"
        ),
        types.InlineKeyboardButton(
            "4. Charlotte.",
            callback_data="q62_4"
        )
    )
    IMAGE_URL62 = "https://i.ibb.co/tMtWZRRG/General-3.jpg"
    # --------------------------------------------------------
    # QUESTION 62 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL62,
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
        "Who does Daniel thank for helping him adjust to Westbridge? \n\n"
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
        "q62_1": "Emily.",
        "q62_2": "Sophie.",
        "q62_3": "Grace.",
        "q62_4": "Charlotte."
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


    # --------------------------------------------------------
    # QUESTION 63 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q63_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q63_2"
        ),
        types.InlineKeyboardButton(
            "3. A few things.",
            callback_data="q63_3"
        ),
        types.InlineKeyboardButton(
            "4. I learned from every mistake.",
            callback_data="q63_4"
        )
    )
    IMAGE_URL63 = "https://i.ibb.co/Q34Zr43F/Class-1.jpg"
    # --------------------------------------------------------
    # QUESTION 63 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL63,
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
        "Someone asks Daniel whether he regrets anything.\n\n"
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
        "q63_1": "Yes.",
        "q63_2": "No.",
        "q63_3": "A few things.",
        "q63_4": "I learned from every mistake."
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
        "Emily asks Daniel what he wants from the future."
    )

    # --------------------------------------------------------
    # QUESTION 64 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Success.",
            callback_data="q64_1"
        ),
        types.InlineKeyboardButton(
            "2. Stability.",
            callback_data="q64_2"
        ),
        types.InlineKeyboardButton(
            "3. Love.",
            callback_data="q64_3"
        ),
        types.InlineKeyboardButton(
            "4. Freedom to choose.",
            callback_data="q64_4"
        )
    )
    IMAGE_URL64 = "https://i.ibb.co/b5NxVBRp/Emily-5.jpg"
    # --------------------------------------------------------
    # QUESTION 64 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL64,
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
        "Emily asks Daniel what he wants from the future.\n\n"
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
        "q64_1": "Success.",
        "q64_2": "Stability.",
        "q64_3": "Love.",
        "q64_4": "Freedom to choose."
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
        "Sophie smiles at Daniel and pauses for a moment.\n\n"

    )

    # --------------------------------------------------------
    # QUESTION 65 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q65_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q65_2"
        ),
        types.InlineKeyboardButton(
            "3. I’ll miss the people.",
            callback_data="q65_3"
        ),
        types.InlineKeyboardButton(
            "4. I’ll miss who we were here.",
            callback_data="q65_4"
        )
    )
    IMAGE_URL65 = "https://ibb.co/HfH2TwjH"
    # --------------------------------------------------------
    # QUESTION 65 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL65,
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
        "Sophie asks whether Daniel will miss school. \n\n"
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
        "q65_1": "Yes.",
        "q65_2": "No.",
        "q65_3": "I’ll miss the people.",
        "q65_4": "I’ll miss who we were here."
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
        "Sophie smiles warmly.\n\n"

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


    # --------------------------------------------------------
    # QUESTION 66 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Absolutely.",
            callback_data="q66_1"
        ),
        types.InlineKeyboardButton(
            "2. If you let me.",
            callback_data="q66_2"
        ),
        types.InlineKeyboardButton(
            "3. Of course.",
            callback_data="q66_3"
        ),
        types.InlineKeyboardButton(
            "4. I’ll read everything you want me to read.",
            callback_data="q66_4"
        )
    )
    IMAGE_URL66 = "https://i.ibb.co/TD26Z7FQ/Grace-5.jpg"
    # --------------------------------------------------------
    # QUESTION 66 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL66,
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
        "Grace asks whether Daniel will read her next novel. \n\n"
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
        "q66_1": "Absolutely.",
        "q66_2": "If you let me.",
        "q66_3": "Of course.",
        "q66_4": "I’ll read everything you want me to read."
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



    # --------------------------------------------------------
    # QUESTION 67 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q67_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q67_2"
        ),
        types.InlineKeyboardButton(
            "3. They have to.",
            callback_data="q67_3"
        ),
        types.InlineKeyboardButton(
            "4. Change is how people discover who they really are.",
            callback_data="q67_4"
        )
    )
    IMAGE_URL67 = "https://i.ibb.co/twFpCTc9/Charlotte-5.jpg"
    # --------------------------------------------------------
    # QUESTION 67 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL67,
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
        "Charlotte asks whether Daniel thinks people can change.\n\n"
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
        "q67_1": "Yes.",
        "q67_2": "No.",
        "q67_3": "They have to.",
        "q67_4": "Change is how people discover who they really are."
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

    # --------------------------------------------------------
    # QUESTION 68 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Yes.",
            callback_data="q68_1"
        ),
        types.InlineKeyboardButton(
            "2. No.",
            callback_data="q68_2"
        ),
        types.InlineKeyboardButton(
            "3. Only if I were certain.",
            callback_data="q68_3"
        ),
        types.InlineKeyboardButton(
            "4. I would choose the person who chooses me too.",
            callback_data="q68_4"
        )
    )
    IMAGE_URL68 = "https://i.ibb.co/tMtWZRRG/General-3.jpg"
    # --------------------------------------------------------
    # QUESTION 68 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL68,
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
        "One of the girls asks Daniel: "
        "“If you could choose one person to spend the rest of your life with, would you choose now?” \n\n"
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
        "q68_1": "Yes.",
        "q68_2": "No.",
        "q68_3": "Only if I were certain.",
        "q68_4": "I would choose the person who chooses me too."
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



    # --------------------------------------------------------
    # QUESTION 69 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Confess.",
            callback_data="q69_1"
        ),
        types.InlineKeyboardButton(
            "2. Wait.",
            callback_data="q69_2"
        ),
        types.InlineKeyboardButton(
            "3. Ask how she feels first.",
            callback_data="q69_3"
        ),
        types.InlineKeyboardButton(
            "4. Tell her honestly without asking her for anything in return.",
            callback_data="q69_4"
        )
    )
    IMAGE_URL69 = "https://i.ibb.co/VYt11hfn/General-4.jpg"
    # --------------------------------------------------------
    # QUESTION 69 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL69,
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
        "Daniel finally has the opportunity to confess his feelings. \n\n"
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
        "q69_1": "Confess.",
        "q69_2": "Wait.",
        "q69_3": "Ask how she feels first.",
        "q69_4": "Tell her honestly without asking her for anything in return."
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
        "  “THE FINAL QUESTION”  \n\n"

    )

    # --------------------------------------------------------
    # QUESTION 70 BUTTONS
    # --------------------------------------------------------

    keyboard = types.InlineKeyboardMarkup(row_width=1)

    keyboard.add(
        types.InlineKeyboardButton(
            "1. Love.",
            callback_data="q70_1"
        ),
        types.InlineKeyboardButton(
            "2. Trust.",
            callback_data="q70_2"
        ),
        types.InlineKeyboardButton(
            "3. Shared dreams.",
            callback_data="q70_3"
        ),
        types.InlineKeyboardButton(
            "4. The decision to keep choosing each other.",
            callback_data="q70_4"
        )
    )
    IMAGE_URL70 = "https://i.ibb.co/JRfd6S67/Final-1.jpg"
    # --------------------------------------------------------
    # QUESTION 70 IMAGE
    # --------------------------------------------------------

    try:
        response = requests.get(
            IMAGE_URL70,
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
        "“What matters most when choosing someone to spend your life with?”\n\n"
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
            "Love.",

        "q70_2":
            "Trust.",

        "q70_3":
            "Shared dreams.",

        "q70_4":
            "The decision to keep choosing each other."
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

        "Those were special days..\n\n"
        "I really miss them! "
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
            f"🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉\n\n"
            f"Your strongest connection is with {winner}."
        )
    if winner == "Emily":

        bot.send_message(
            call.message.chat.id,
            "Several years have passed.\n\n"
            "Daniel and Emily both attend university.\n\n"
            "Their relationship survives the distance because neither expects the other "
            "to give up their ambitions.\n\n"
            "After graduation, Emily receives a job offer in another city.\n\n"
            "She meets Daniel at the same café where they once studied.\n\n"
            "Emily: \"I have something to tell you.\"\n\n"
            "Daniel smiles.\n\n"
            "Daniel: \"So do I.\"\n\n"
            "Emily looks nervous.\n\n"
            "Daniel: \"Go first.\"\n\n"
            "Emily: \"I got the job.\"\n\n"
            "She smiles.\n\n"
            "Daniel: \"That's wonderful.\"\n\n"
            "Then Daniel takes a small box from his pocket.\n\n"
            "Emily becomes completely silent.\n\n"
            "Daniel: \"Emily, I don't know exactly what the future will look like.\"\n\n"
            "He pauses.\n\n"
            "Daniel: \"But I know who I want beside me while we find out.\"\n\n"
            "She opens the box.\n\n"
            "Inside is a ring.\n\n"
            "Emily looks at him.\n\n"
            "Emily: \"Are you sure?\"\n\n"
            "Daniel: \"Yes.\"\n\n"
            "She smiles through tears.\n\n"
            "Emily: \"Then yes.\"\n\n"
            "Not long afterwards...\n\n"
            "Emily and I got married."
        )
    IMAGE_URLEmilyEND = "https://i.ibb.co/BKtdGk4p/Emily-Final.jpg"

    try:

        response = requests.get(
            IMAGE_URLEmilyEND,
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
            call.message.chat.id,
            photo
        )

    except Exception as e:

        print("QUESTION 70 IMAGE ERROR:", e)

        bot.send_message(
            call.message.chat.id,
            "The game is finished"
        )
    if winner == "Sophie":

        bot.send_message(
            call.message.chat.id,
            "Several years have passed.\n\n"
            "Daniel and Emily both attend university.\n\n"
            "Their relationship survives the distance because neither expects the other "
            "to give up their ambitions.\n\n"
            "After graduation, Emily receives a job offer in another city.\n\n"
            "She meets Daniel at the same café where they once studied.\n\n"
            "Emily: \"I have something to tell you.\"\n\n"
            "Daniel smiles.\n\n"
            "Daniel: \"So do I.\"\n\n"
            "Emily looks nervous.\n\n"
            "Daniel: \"Go first.\"\n\n"
            "Emily: \"I got the job.\"\n\n"
            "She smiles.\n\n"
            "Daniel: \"That's wonderful.\"\n\n"
            "Then Daniel takes a small box from his pocket.\n\n"
            "Emily becomes completely silent.\n\n"
            "Daniel: \"Emily, I don't know exactly what the future will look like.\"\n\n"
            "He pauses.\n\n"
            "Daniel: \"But I know who I want beside me while we find out.\"\n\n"
            "She opens the box.\n\n"
            "Inside is a ring.\n\n"
            "Emily looks at him.\n\n"
            "Emily: \"Are you sure?\"\n\n"
            "Daniel: \"Yes.\"\n\n"
            "She smiles through tears.\n\n"
            "Emily: \"Then yes.\"\n\n"
            "Not long afterwards...\n\n"
            "Emily and I got married."
        )
    IMAGE_URLEmilyEND = "https://i.ibb.co/BKtdGk4p/Emily-Final.jpg"

    try:

        response = requests.get(
            IMAGE_URLEmilyEND,
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
            call.message.chat.id,
            photo
        )

    except Exception as e:

        print("QUESTION 70 IMAGE ERROR:", e)

        bot.send_message(
            call.message.chat.id,
            "The game is finished"
        )


    if winner == "Grace":

        bot.send_message(
            call.message.chat.id,
            "Several years have passed.\n\n"
            "Daniel and Emily both attend university.\n\n"
            "Their relationship survives the distance because neither expects the other "
            "to give up their ambitions.\n\n"
            "After graduation, Emily receives a job offer in another city.\n\n"
            "She meets Daniel at the same café where they once studied.\n\n"
            "Emily: \"I have something to tell you.\"\n\n"
            "Daniel smiles.\n\n"
            "Daniel: \"So do I.\"\n\n"
            "Emily looks nervous.\n\n"
            "Daniel: \"Go first.\"\n\n"
            "Emily: \"I got the job.\"\n\n"
            "She smiles.\n\n"
            "Daniel: \"That's wonderful.\"\n\n"
            "Then Daniel takes a small box from his pocket.\n\n"
            "Emily becomes completely silent.\n\n"
            "Daniel: \"Emily, I don't know exactly what the future will look like.\"\n\n"
            "He pauses.\n\n"
            "Daniel: \"But I know who I want beside me while we find out.\"\n\n"
            "She opens the box.\n\n"
            "Inside is a ring.\n\n"
            "Emily looks at him.\n\n"
            "Emily: \"Are you sure?\"\n\n"
            "Daniel: \"Yes.\"\n\n"
            "She smiles through tears.\n\n"
            "Emily: \"Then yes.\"\n\n"
            "Not long afterwards...\n\n"
            "Emily and I got married."
        )
    IMAGE_URLEmilyEND = "https://i.ibb.co/BKtdGk4p/Emily-Final.jpg"

    try:

        response = requests.get(
            IMAGE_URLEmilyEND,
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
            call.message.chat.id,
            photo
        )

    except Exception as e:

        print("QUESTION 70 IMAGE ERROR:", e)

        bot.send_message(
            call.message.chat.id,
            "The game is finished"
        )


    if winner == "Emily":

        bot.send_message(
            call.message.chat.id,
            "Charlotte rejects the career her parents planned for her. \n\n"
            "She builds her own company. \n\n"
            "Daniel pursues his own career. \n"
            "They become partners not because they need each other to succeed, but because they respect each other’s ambitions.\n\n"
            "One evening, Charlotte asks Daniel to meet her at the place where they first spoke.\n\n"
            "Charlotte: “You remember?” \n\n"
            "Daniel: “Of course.”"\n\n"
            "She looks toward the school.\n\n"
            "Charlotte:“I used to think success meant proving everyone wrong.” \n\n"
            "Daniel:“And now?” \n\n"
            "Charlotte:“Now I think it’s choosing the life I actually want.”\n\n"
            "Daniel smiles.\n\n"
            "Charlotte reaches into her coat.\n\n"
            "She pulls out a small box.\n\n"
            "Daniel stares.\n\n"
            "Daniel: “Wait.”\n\n"
            "She laughs.\n\n"
            "Daniel: “I know what you’re thinking. Charlotte..”\n\n"
            "Charlotte:“You’ve never been very good at making decisions. \"\n\n"
            "She opens the box.\n\n"
            "Inside is a ring.\n\n"
            "Charlotte:“So I’ll make this one.”\n\n"
            "Daniel laughs.\n\n"
            "Daniel:“Are you proposing to me?”\n\n"
            "Charlotte:“Apparently.”\n\n"
            "He smiles.\n\n"
            "Daniel:“Then yes.”\n\n"
            "Charlotte starts laughing. Daniel takes her hand, and together they look toward the school where their story began."
            "“Some time later, we got married. Charlotte became my wife.”"
        )
    IMAGE_URLCharlotteEND = "https://i.ibb.co/q3D64c7W/Charlotte-Final.jpg"

    try:

        response = requests.get(
            IMAGE_URLCharlotteEND,
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
            call.message.chat.id,
            photo
        )

    except Exception as e:

        print("QUESTION 70 IMAGE ERROR:", e)

        bot.send_message(
            call.message.chat.id,
            "The game is finished"
        )



	

# ============================================================
# START BOT
# ============================================================

print("Bot is running...")

bot.delete_webhook(drop_pending_updates=True)
bot.infinity_polling()
