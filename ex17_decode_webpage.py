# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# Task: Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
# ...on the New York Times homepage
# TODO: this prints currently NOTHING! Need to recognize articles and collect those and then print their summary as list

import requests
from bs4 import BeautifulSoup


url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text
# now r_html contains the HTML of the page as a string
soup = BeautifulSoup(r_html, 'html.parser')
# print (soup.prettify())
for article in soup.find_all('Article'):
    print(article.get('summary'))