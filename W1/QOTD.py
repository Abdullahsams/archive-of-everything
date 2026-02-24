import random

MESSAGES = ["You earned this", "Rest, reset, repeat", "Silence the noise", "Time to recharge", "Enjoy your peace", "Relax, breathe deeply", "Guilt-free rest today", "Work hard, rest hard", "Unplug and unwind", "Celebrate your stillness"]

def get_random_messages(n):
    return random.sample(MESSAGES, n)