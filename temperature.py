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
    print (f'current temperature in {place}: {weather(place)}')
