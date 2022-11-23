import random
import requests
from bs4 import BeautifulSoup

id_channel ="-1001850542070"
token_bot = "5734489075:AAE74AvK6mV5qtbWBzQw88xHlC3bQMN0Ulk"
url ="https://cnnespanol.cnn.com/"
news_dictionary={}

def send_telegram(title,link):
    base_url = f"https://api.telegram.org/bot{token_bot}/sendMessage"
    params = {'id_channel' : id_channel, 'text' : f'{title}: {link}'}
    # params = {'id_channel' : id_channel, 'text' : 'Message text'}
    resp = requests.get(base_url, data= params)
    print("Server: ", resp.text) 

send_telegram()

resp = requests.get(url)
if resp.status_code == 200:
     cont =resp.content
     soup = BeautifulSoup(cont,"html.parser")
     data=soup.find_all("a",href=True)
     for x in data:
        news_dictionary[x.get_text().strip()] = x["href"]
        randomLink = random.choice(list(news_dictionary.keys()))
        print(news_dictionary[randomLink])
