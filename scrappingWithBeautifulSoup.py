import requests
from bs4 import BeautifulSoup
url ="https://cnnespanol.cnn.com/"
resp = requests.get(url)
if resp.status_code == 200:
     cont =resp.content
     soup = BeautifulSoup(cont,"html.parser")
     print(soup)
     print(soup.title.string)
     data=soup.find_all("a",href=True)
     print(type(data))
     for x in data:
          print(x["href"])
          print(x.get_text().strip())