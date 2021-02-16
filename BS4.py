from bs4 import BeautifulSoup
import requests

url='https://www.nytimes.com/'
a=requests.get(url)
soup = BeautifulSoup(a.content,'html.parser')

for i in soup.find_all("span",""):
    title =i.text
    print(title)