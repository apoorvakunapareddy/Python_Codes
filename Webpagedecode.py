from bs4 import BeautifulSoup
import requests

url='https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
a=requests.get(url)
soup= BeautifulSoup(a.text,'html.parser')

for i in soup.find_all(class_='article__chunks'):
    title =i.text
    title2= title.replace(".",'.\n')
    # print(i.contents[0].strip())
    openfile=open("Sample.txt",'w')
    openfile.write(title2)
    openfile.close()