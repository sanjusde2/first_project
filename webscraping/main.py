import requests
from bs4 import BeautifulSoup 
response=requests.get('https://www.google.com/?zx=1794930881902')

s=BeautifulSoup(response.text)
print(s.find('title').text)
for each in s.find_all('a'):
    print(each.text)
    

