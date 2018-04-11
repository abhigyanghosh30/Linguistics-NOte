from urllib.request import urlopen
from bs4 import BeautifulSoup

page = urlopen("http://www.englishinuse.net/")
soup = BeautifulSoup(page, "lxml")
texts = soup.find_all("tr", attrs={"class": "font1"})
f = open("english.txt", "a+")
for text in texts:
    sentence = text.find(
        "td", attrs={"style": "border-bottom:1px dotted #484848;"})
    f.write(sentence.string+"\n")
