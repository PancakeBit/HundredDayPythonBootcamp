from bs4 import BeautifulSoup

with open('website.html', 'r') as website:
    text = website.read()

soup = BeautifulSoup(text, features="html.parser")
anchors = soup.find_all(id="name")
heading = soup.select(selector=".heading")
