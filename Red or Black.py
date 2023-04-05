import telebot
import random
token = "6132800133:AAGowZCMJvi2nfmFjm8suUXpDzCN9yXW2Tw"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
  keyboard = telebot.types.ReplyKeyboardMarkup()
  red_button = telebot.types.KeyboardButton("🟥")
  black_button = telebot.types.KeyboardButton("⬛️")
  keyboard.row(red_button)
  keyboard.row(black_button)
  bot.send_message(message.chat.id, "Выбери Цвет: 🟥 или ⬛️", reply_markup=keyboard)
  bot.register_next_step_handler(message, answer_card)

def answer_card(message):
  value, suit = random_card()
  if message.text == "🟥" and suit in ["H", "D"]:
    bot.send_message(message.chat.id, f"Правильно. Kарта была {value}{suit}")
  elif message.text == "⬛️" and suit in ["C", "S"]: #else + if = elif:
    bot.send_message(message.chat.id, f"Правильно. Kарта была {value}{suit}")
  else:
    bot.send_message(message.chat.id, f"Неправильно. Kарта была {value}{suit}")
  start(message)

def random_card():
  value = random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
  suit = random.choice(["H", "D", "C", "S"])
  return value, suit


bot.infinity_polling()