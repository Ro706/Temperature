from gtts import gTTS
from tqdm import tqdm
import time
import requests
import os
from bs4 import BeautifulSoup
os.system('clear')
def weather(place):
    url = f"https://www.google.com/search?q=weather in {place}"
    r = requests.get(url)
    s = BeautifulSoup(r.text,'html.parser')
    temperature = s.find('div',class_='BNeawe').text
    return temperature
os.system('figlet Temperature')
if __name__=='__main__':
    place = str(input('place: '))
    for i in tqdm(range(100)):
        time.sleep(0.2)
    a = f'current temperature in {place}: {weather(place)}'
    language ='en'
    output = gTTS(text=a,lang=language)
    output.save('temp.mp3')
    os.system("mpv /data/data/com.termux/files/home/temp.mp3")
