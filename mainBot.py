# Я просто напишу импорт библиотеки, и вход в бота, а дальше фантазия придумает.

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
        
                
methods = []
for x in client.callbacks.chat_methods:
	methods.append(client.callbacks.event(client.callbacks.chat_methods[x].__name__)(on_message))

        

socketDelay() 
