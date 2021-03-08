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
	
	randomnumb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'] # рандом число
	
	content = str(content).split(" ")
	if content[0][0] == "!" and content[0][1:].lower() == "хелп":
		sub_client.send_message(message="Help(beta): !test", chatId=chatId, replyTo=id)
	if content[0] == "!гс":
		myobj = gTTS(text=data.message.content[4:], lang='ru', slow=False)
		myobj.save("gs.mp3")
		with open("gs.mp3", "rb") as file:
			sub_client.send_message(chatId=chatId, file=file, fileType="audio")
	if content[0] == "!ping":
                sub_client.send_message(message="Ping!", chatId=chatId, replyTo=id)
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
	if content[0] == "!chatId":
		sub_client.send_message(message=(f"Айди этого чата: {chatId}"), chatId=chatId, replyTo=id)
	if content[0] == "!code":
		sub_client.send_message(message="[BC][💳]Коды из цифр\n\n[C]Что это? А это — пасхальные коды, если собрать интересную комбинацию из !randomnumber то, вы получите какой-то секрет из бота. Пример, как их вводить: !code<цифры>", chatId=chatId, replyTo=id)
	if content[0] == "!code<цифры>":
		sub_client.send_message(message=f"[BC][🚄]Предупреждение\n\n[C]Дорогой юзер, чтобы получить код, нужно ввести !randomnumber и из цифр, соберите комбинацию.", chatId=chatId, replyTo=id)
	if content[0][0] == "!" and content[0][1:].lower() == "code10046771213158262":
	  	sub_client.send_message(message='!гс Вася топ чел!', chatId=chatId, replyTo=id)
	if content[0][0] == "!" and content[0][1:].lower() == "code63498794405073559":
	  	sub_client.send_message(message=f'{nickname} Ты крутой!', chatId=chatId, replyTo=id)
	if content[0] == "!code50999291251433077":
		sub_client.send_message(message="Nsercet", chatId=chatId)
	if content[0] == "Nsercet":
		myobj = gTTS(text=data.message.content[4:], lang='ru', slow=False)
		myobj.save("gs.mp3")
		with open("gs.mp3", "rb") as file:
			sub_client.send_message(chatId=chatId, file=file, fileType="audio")
	if content[0] == "!code44636141429130357":
		sub_client.send_message(message="Онао крутой.", chatId=chatId)
	if content[0] == "!code76879235334512112":
		sub_client.send_message(message="Люблю есть КФС.", chatId=chatId)
	if content[0] == "!code96877830231156515":
		sub_client.send_message(message=f"{nickname} Боты не живые материи. Боты — роботы, которые выполняют команды, для обслуживание и прочее.", chatId=chatId)
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
