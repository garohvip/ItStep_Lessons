import telebot
import re

config = {
    "name": "",
    "token": ""
}

agent_ghost = telebot.TeleBot(config["token"])


@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "hi":
        agent_ghost.send_message(message.chat.id, "Hello")
    elif message.text.lower() == "палиндром":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Ну ка давай сюда слово, сейчас я его проверю на палиндром"), palindrom)
    elif message.text.lower() == "парное":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Кидай цыфру"), par)


def par(message):
    if message.text.isdigit():
        if int(message.text) % 2 == 0:
            agent_ghost.send_message(message.chat.id, "Число четное")
        else:
            agent_ghost.send_message(message.chat.id, "Число не четное!!")
    else:
        agent_ghost.send_message(message.chat.id, "Воспринимаю только цифры")


def palindrom(message):
    if re.findall(r"\d+", message.text):
        agent_ghost.send_message(message.chat.id, "Без цифр пожалуйста")
    else:
        if message.text.lower() == message.text.lower()[::-1]:
            agent_ghost.send_message(message.chat.id, "Это слово - палиндром")
        else:
            agent_ghost.send_message(message.chat.id, "Не является палиндромом")

agent_ghost.polling(none_stop=True, interval=0)