import requests
from bs4 import BeautifulSoup

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

#match = soup.find_all('div', class_='matches   ')

#to match a video source
videoSource = soup.find_all('iframe')
print(videoSource)
