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
    print (f'current temperature in {place}: {weather(place)}')
