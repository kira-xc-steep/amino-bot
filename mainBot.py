# Я просто напишу импорт библиотеки, и вход в бота, а дальше фантазия придумает.
# Логи добавлены и команды.

# Update log:
	# Сделано под 1.2.13 амино.пай версии
	# Добавил текст для измены статуса, чтобы бот сообщал.

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
print(' ')
time.sleep(1)
ban = 0
tim = 1
hm = [0]
av = []
nom = 0


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
	
	lis = ['🌠 - Думаю, да', '🌠 - Думаю что нет', '🌠 - Нет.', '🌠 - Не знаю, сам думай', '🌠 - Да.', '🌠 - Сложный вопросик конечно.', '🌠 - Повтори вопрос.', '🌠 - Ты уверен, что хочешь этого знать?', '🌠 - Не знаю.', '🌠 - Гляжу у себя в голове, а думать не в состоянии', '🌠 - Отрицаю.', '🌠 - Не согласен с вашим вопросом.', '🌠 - Посмотри в интернете ответы, или же у Яндекс Алисы спроси'] # команда вопроса
	randomnumb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100'] # рандом число
	gayper = ['🏳‍🌈 Вы гей/лесбиянка на: 0%', '🏳‍🌈 Вы гей/лесбиянка на: 0.5%', '🏳‍🌈 Вы гей/лесбиянка на: 1%', '🏳‍🌈 Вы гей/лесбиянка на: 2.56%', '🏳‍🌈 Вы гей/лесбиянка на: 3%', '🏳‍🌈 Вы гей/лесбиянка на: 5%', '🏳‍🌈 Вы гей/лесбиянка на: 13.45%', '🏳‍🌈 Вы гей/лесбиянка на: 23.75%', '🏳‍🌈 Вы гей/лесбиянка на: 35.93%', '🏳‍🌈 Вы гей/лесбиянка на: 41.99%', '🏳‍🌈 Вы гей/лесбиянка на: 49%', '🏳‍🌈 Вы гей/лесбиянка на: 69.34%', '🏳‍🌈 Вы гей/лесбиянка на: 79.33%', '🏳‍🌈 Вы гей/лесбиянка на: 95.55%', '🏳‍🌈 Вы гей/лесбиянка на: 100%'] # гей тест
	
	content = str(content).split(" ")
	if content[0][0] == "!" and content[0][1:].lower() == "хелп":
		sub_client.send_message(message="[C]0. !гс — Делает из текста в гс.\n[C]1. !ping — Бот сообщает, что он работает.\n[C]2. !adpanel — Ну тут итак понятно.\n[C]3. !кикнименя — Нужна роль помощника, чтобы бот кикнул вас.\n[C]4. !say — Пересказывает сообщение.\n[C]5. имя_бота — Позовите бота, если хотите.\n[C]6. !code — Это команда подскажет, что это.\n[C]7. !saycontent — Пересказывает ваше сообщение в контексном виде.\n[C]8. !infobot — Информация о боте.", chatId=chatId, replyTo=id)
	if content[0] == "!гс":
		myobj = gTTS(text=data.message.content[4:], lang='ru', slow=False)
		myobj.save("gs.mp3")
		with open("gs.mp3", "rb") as file:
			sub_client.send_message(chatId=chatId, file=file, fileType="audio")
	if content[0] == "!ping":
                sub_client.send_message(message="Ping!", chatId=chatId, replyTo=id)
	if content[0][0] == "?":
		sub_client.send_message(message=str(random.choice(lis)), chatId=chatId, replyTo=id)
	if content[0] == "!adpanel":
		sub_client.send_message(message="[BC][💻]Админ панель\n[C]1. !зачистка-100 — Удаляет 100 сообщении, но нужен лидер\n[C]2. !night — Пожелать участникам спокойной ночи.\n[C]3. !morn — Пожелать доброго утро участникам.\n[C]4. !chatId — Узнать айди данного чата, в котором вы находитесь.\n[C]5. !save — Сохранить чат.\n[C]6. !loadsave — Загрузить сохранëнный чат, но нужен помощник.\n7. !online-status, !offline-status — Изменить статус боту.\n8. !кикнименя — Бот вас с радостью ëбнет с чата, если напишите эту команду. :)", chatId=chatId, replyTo=id)
	if content[0] == "!кикнименя":
		sub_client.send_message(message=f"Кикнул вас, {nickname}", chatId=chatId, replyTo=id)
		sub_client.kick(userId=data.message.author.userId, chatId=data.message.chatId, allowRejoin = True)
	if content[0] == "!night":
		sub_client.send_message(message="Спокойной всем ночи.", chatId=chatId)
	if content[0] == "!morn":
		sub_client.send_message(message="Доброе всем утро.", chatId=chatId)
	if content[0] == "!online-status":
		sub_client.activity_status('online')
		sub_client.send_message(message="Im going to online", chatId=chatId, replyTo=id)
	if content[0] == "!offline-status":
		sub_client.activity_status('offline')
		sub_client.send_message(message="Im going to offline", chatId=chatId, replyTo=id)
	if content[0] == "!say":
		sub_client.send_message(message=(f"{data.message.content[4:]}"), chatId=chatId) # Тоже бесполезная команда. 
	if content[0] == "Васяныч":
		sub_client.send_message(message=(f"Звали, {nickname}?"), chatId=chatId, replyTo=id)  # Зовëт бота. :/
	if content[0] == "Привет":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "привет":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "Дарова":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "Дратути.":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "Дратути":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "дратути":
		sub_client.send_message(message='И тебе привет', chatId=chatId, replyTo=id)
	if content[0] == "Приветствую.":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "Приветствую":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "приветствую":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "Здраствуйте.":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "Здраствуйте":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
	if content[0] == "здраствуйте":
		sub_client.send_message(message='И тебя приветствую', chatId=chatId, replyTo=id)
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
	if content[0] == "!saycontent":
		sub_client.send_message(message=(f"{nickname}: {content}"), chatId=chatId) # Команда, но с контексным сообщением.
	if content[0] == "!infobot":
		sub_client.send_message(message='[BC][📄]Информация о боте\n[C]Создатели бота: Vasyajopa228, onaosuperpro2015, whoname01\n[C]Версия бота: 0.8', chatId=chatId, replyTo=id)
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
for x in client.chat_methods:
	methods.append(client.event(client.chat_methods[x].__name__)(on_message))
