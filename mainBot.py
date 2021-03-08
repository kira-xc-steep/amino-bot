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
time.sleep(1) # Пишет это хуйня, когда бот зашëл на аккаунт. 
ban = 0
tim = 1
hm = [0]
av = []
nom = 0

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
        time.sleep(1) # Обновляет сокеты. 

def on_message(data):
	global ban
	global tim
	global nom
	chatId = data.message.chatId
	nickname = data.message.author.nickname
	content = data.message.content
	vrem = data.message.createdTime[17:19]
	id = data.message.messageId
	
	print(f"# Log: {nickname}: {content}: {chatId} : {ban}: {data.message.type}") # Выводит сообщение в консоль. 

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
	if content[0] == "имя_бота":
		sub_client.send_message(message=(f"Звали, {nickname}?"), chatId=chatId, replyTo=id)  # Зовëт бота. :/
        if content[0][1:].lower()=="!inv":
		sub_client.join_chat(chatId=chatInfo.chatId)
		x=client.get_from_code(str(content[1])).objectId
		sub_client.invite_to_chat([x], chatId=chatInfo.chatId)
	if content[0] == "!зачистка-100":
	           if data.message.author.role != 0:
	               for msgId in sub_client.get_chat_messages(chatId=data.message.chatId, size=100).messageId:
	               	sub_client.delete_message(reason="зачистка", chatId=data.message.chatId, messageId=msgId, asStaff=True) # Зачистка чата например от спама, нужен лидер, либо стоит "asStaff=True", "reason=зачистка"
        
        if content[0][0] == "!" and content[0][1:].lower() == "on":
		tim = -tim
	
        ##################################Защита чата##################################################

	global nazvan
	global opisan
	global fonsss
	
	if content[0][0] == "!":
		if content[0][1:].lower() == "save":
			nazvan = sub_client.get_chat_thread(chatId=data.message.chatId).title
			opisan = sub_client.get_chat_thread(chatId=data.message.chatId).content
			fonsss = sub_client.get_chat_thread(chatId=data.message.chatId).backgroundImage
			sub_client.send_message(message="Saved!", chatId=data.message.chatId, replyTo=id)
			print('# Log Save: Чат сохранëн!')
		if content[0][1:].lower() == "loadsave":
			sub_client.edit_chat(chatId=data.message.chatId, title=str(nazvan), content=str(opisan))
			try:
				sub_client.edit_chat(chatId=data.message.chatId, backgroundImage=str(fonsss))
			except:
				sub_client.send_message(message='Сейв был успешно загружен.', chatId=data.message.chatId)
		if content[0][1:].lower() == "a" and sub_client.get_chat_thread(chatId).author.userId:
			sub_client.invite_to_chat(userId=str(client.get_from_code(str(content[1][:])).objectId), chatId=chatId)
			nom = 1
			
	if data.message.content != None and data.message.type in [1, 50, 57, 59, 100, 101, 102, 103, 104, 105, 106, 107, 109, 110, 113, 114, 115, 116, 124, 125, 126]:
		sub_client.send_message(message=(f'Рейдер {nickname} был кикнут из чата навсегда.'), chatId=data.message.chatId)
		sub_client.kick(userId=data.message.author.userId, chatId=data.message.chatId, allowRejoin = False)
		nom = 0

methods = []
for x in client.callbacks.chat_methods:
	methods.append(client.callbacks.event(client.callbacks.chat_methods[x].__name__)(on_message))

        

socketDelay() 
