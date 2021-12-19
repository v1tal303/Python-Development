from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

anchor_tags = soup.find_all(name="a")

for tag in anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")

print(heading)

section_heading = soup.find(name="h3", class_="heading")

print(section_heading.name)
print(section_heading.get("class"))
print(section_heading.getText())

company_url = soup.select_one(selector="p a")
name = soup.select_one(selector="#name")
print(company_url)
print(name)

headings = soup.select(".heading")

print(headings)