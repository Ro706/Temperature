import pyttsx3
from tqdm import tqdm
import time
import requests
import os
from bs4 import BeautifulSoup
from pyfiglet import Figlet
f = Figlet(font='slant')
print (f.renderText('Temperature'))
def speech(a):
    engine = pyttsx3.init()
    engine.say(a)
    engine.runAndWait()
    print(a)
def weather(place):
    url = f"https://www.google.com/search?q=weather in {place}"
    r = requests.get(url)
    s = BeautifulSoup(r.text,'html.parser')
    temperature = s.find('div',class_='BNeawe').text
    return temperature

if __name__=='__main__':
    place = str(input('place: '))
    for i in tqdm(range(100)):
        time.sleep(0.01)
    a = f'current temperature in {place}: {weather(place)}'
    speech(a)

