import requests
import bs4

website = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = website.text

soup = bs4.BeautifulSoup(website, features="html.parser")

titles_raw = soup.find_all(name="h3", class_="title")
titles = [title.getText() for title in reversed(titles_raw)]

# ok SO APPARENtly you don't have to isolate the title so just ignore this code
# for title in titles_raw[::-1]:
#     try:
#         titles.append(title.getText().split(")")[1].strip())
#     except IndexError:
#         titles.append(title.getText().split(":")[1].strip())
#     #titles.append(title.getText().split(")"))

with open('movies.txt', 'w') as movies:
    for title in titles:
        movies.write(title + '\n')