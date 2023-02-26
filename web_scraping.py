from bs4 import BeautifulSoup
import requests

##with open('index.html','r') as f:
##    doc = BeautifulSoup(f, 'html.parser')

##tag = doc.title
##print(tag)

##tag = doc.title
##print(tag.string)

##tags = doc.find_all('p')
##print(tags)

##tags = doc.find_all('p')[0]
##print(tags.find_all('b'))

url = 'https://en.wikipedia.org/wiki/Madagascar'

result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')

contents = doc.findAll(text='Madagascar')
print(contents[0].parent)