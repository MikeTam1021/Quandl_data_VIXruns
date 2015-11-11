"""
Created on Sat Nov 07 08:47:42 2015

@author: MikeTam
"""

from bs4 import BeautifulSoup
import requests

url = 'http://www.oecd.org/unitedstates/'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print link.get('href')
