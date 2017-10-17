from bs4 import BeautifulSoup

soup = BeautifulSoup(open('htmlsample\index.html'), "lxml")
#print(soup.prettify())

print(soup.title)

count = 1
for child in soup.body.children:
    print("child:", count)
    print(child)
    count = count + 1

count = 1
for child in soup.descendants:
    print("descendants:", count)
    print(child)
    count = count + 1