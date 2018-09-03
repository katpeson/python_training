# http://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# Task: Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
# ...on the New York Times homepage
# TODO: could try to expand this to access the other 'top' pages after front one to gather the titles also from there

import requests
from bs4 import BeautifulSoup as bs


# My function to return titles from the main page (top only since rest is dynamic content)
def print_titles(url):
    nro = 1
    r = requests.get(url)
    r_html = r.text
    # now r_html contains the HTML of the front page as a string
    soup = bs(r_html, 'html.parser')
    # lists all articles in the top section of the website (seems the rest of the page is outside html)
    for tag in soup.find_all('article'):
        title = tag.h2.string
        print nro, ":", title
        nro += 1


# # Testing other peoples solution to bring all article titles
# # returns 'None' on 3.9.2018 so I assume the html has changed and this can no longer locate the article titles
# def test(url):
#     res = requests.get(url)
#     soup = bs(res.text, 'html.parser')
#     stories = soup.findAll("h2", {"class": "story-heading"})
#     for i in stories:
#         cleantitle = i.text.strip()
#         return(cleantitle)


print "Article titles on front page: "
print_titles('http://www.nytimes.com/')
# print test('http://www.nytimes.com/')
