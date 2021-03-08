# Я просто напишу импорт библиотеки, и вход в бота, а дальше фантазия придумает.
# Логи добавлены и команды.

import amino
import random
import datetime
from gtts import gTTS
import requests
import os
import time
import threading
from threading import Thread
import subprocess
from io import BytesIO
from getpass import getpass

client = amino.Client()
client.login(email="email", password="password") #вводим пароль и почту от аккаунта бота
sub_client = amino.SubClient(comId='194234106', profile=client.profile) #вместо "id" введите айди сообщества, в котором будет работать чат
print('Bot status: True! Bot was login')
time.sleep(1)

def socketDelay():
    j = 0
    while True:
        if j >= 300: # = 5 min
            print("Выполняю обнову сокетов...")
            client.socket.close()
            client.socket.start()
            print("Обновление сокетов выполено.")
            j = 0
        j += 1
        time.sleep(1)

def on_message(data):
	global ban
	global tim
	global nom
	chatId = data.message.chatId
	nickname = data.message.author.nickname
	content = data.message.content
	vrem = data.message.createdTime[17:19]
	id = data.message.messageId
	
	print(f"# Log: {nickname}: {content}: {chatId} : {ban}: {data.message.type}")

        content = str(content).split(" ")
	if content[0][0] == "!" and content[0][1:].lower() == "хелп":
		sub_client.send_message(message="Help(beta): !test", chatId=chatId, replyTo=id)
        if content[0] == "!ping":
                sub_client.send_message(message"Ping!", chatId=chatId, replyTo=id)
	if content[0] == "!online-status":
		subclient.activity_status('online') #бесполезная команда
	if content[0] == "!offline-status":
		subclient.activity_status('offline')
        if content[0] == "!say":
		sub_client.send_message(message=(f"{data.message.content[4:]}"), chatId=chatId) # Тоже бесполезная команда. 
	if content[0] == "whoname00":
		sub_client.send_message(message=(f"Звали, {nickname}?"), chatId=chatId, replyTo=id)  # Зовëт бота. :/
	if content[0][1:].lower()=="!inv":
		sub_client.join_chat(chatId=chatInfo.chatId)
		x=client.get_from_code(str(content[1])).objectId
		sub_client.invite_to_chat([x], chatId=chatInfo.chatId)
	if content[0] == "!chatId":
		sub_client.send_message(message=(f"айди этого чата: {chatId}"), chatId=chatId, replyTo=id)

methods = []
for x in client.callbacks.chat_methods:
	methods.append(client.callbacks.event(client.callbacks.chat_methods[x].__name__)(on_message))

        

socketDelay() 
