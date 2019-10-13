import requests
import bs4

url =  "https://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, "lxml")

def course_info(id):
    valute = soup.find("valute", {"id": id})
    value = float(valute.value.text.replace(",", "."))
    return value

num_usd = 10

print(f"Чтобы купить {num_usd} долларов, нужно {course_info('R01235') * num_usd} рубля")



