# http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
# Using as a base my own solution for task 17 (decode web page 1)
# NOTE: original given 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture' is no longer in
# ... 4 pages, so I'll use 'https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/' instead!

import requests
from bs4 import BeautifulSoup as bs


# goes through all pages on article and prints the content from those as text
def print_full_article(url):
    article = get_article(url)
    # print title lines and content of the first page only
    print article.h1.string
    print article.h2.string
    print_content(article)
    # go looking for more pages in the article and print ONLY content from those too
    has_next_page = True
    while has_next_page:
        next_page_element = article.find(id="nextpage")
        if next_page_element is not None:
            next_page_url = next_page_element.find('a', href=True)
            article = get_article((url + next_page_url['href']))
            print_content(article)
        else:
            has_next_page = False
            print("The end of the article")


# prints the content (body) of the article on page
def print_content(article):
    content = (article.find(id="body"))
    print content.text


# finds the id="article" part of the html (incl. page_nav) and returns it
def get_article(url):
    r = requests.get(url)
    r_html = r.text
    # now r_html contains the HTML of the page
    soup = bs(r_html, 'html.parser')
    article = soup.find(id="article")
    return article


print_full_article('https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/')
