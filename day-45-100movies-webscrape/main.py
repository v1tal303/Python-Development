import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

list_of_films_html = soup.find_all(name="h3", class_="title")

list_of_films = [i.getText() for i in list_of_films_html]
list_of_films_reversed = "\n".join(list_of_films[::-1])

with open("movies.txt", "w") as file:
    file.write(list_of_films_reversed)



print(list_of_films_reversed)
# print(list_of_ranking)