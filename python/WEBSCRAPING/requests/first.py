#here we examine how to parse a htmlFile

from bs4 import BeautifulSoup
import requests

with open('siteToScrape.html') as htmlFile:
	soup = BeautifulSoup(htmlFile, 'lxml')

#print(soup.prettify())			#makes the identation and pretifies the output

#the examples below will only return the first argument like using find
match = soup.title
print('\n', match)

match2 = soup.title.text
print('\n', match2)

div= soup.find('div', class_='', )			#can take other arguments like class_
print('\n', div)

#to get a list that matches all the queries we use find_all method
div1 = soup.find_all('div')
print('\n\nPrinting Multiple Lines')
for x in div1:
	print('\n', x)