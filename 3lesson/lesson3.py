import requests
from bs4 import BeautifulSoup


def weather(html):
    return html.find("div", {"class" : "link__condition day-anchor i-bem"}).text

def temp(html):
     return html.find("span", {"class" : "temp__value"}).text


url = "https://yandex.ru/pogoda/moscow?from=serp_title"
response = requests.get(url)
html = BeautifulSoup(response.content,"lxml")
print(weather(html))
print("Сегодня",temp(html),"Состояние", weather(html))

hours = 3

sunset = 13
sunrise = 2

if hours >= sunrise and hours <= sunset:
    print("На улице солнце")
