import requests
import bs4

website = requests.get("https://news.ycombinator.com/news")
website_text = website.text

websoup = bs4.BeautifulSoup(website_text, "html.parser")
titles = websoup.find_all(name="a", rel="noreferrer")
articles = [title.text for title in titles]
links = [title.get("href") for title in titles]

print(articles)
print(links)