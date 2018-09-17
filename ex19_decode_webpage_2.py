# http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
# Using as a base my own solution for task 17 (decode web page 1)
# NOTE: original given 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture' is no longer in
# ... 4 pages, so I'll use 'https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/' instead!
# TODO: actual task 19
# TODO: need for to loop over all pages to print each out! And to figure out how to do that navigation between pages...

import requests
from bs4 import BeautifulSoup as bs


# finds the id="article" part of the html (incl. page_nav)
def get_article(url):
    r = requests.get(url)
    r_html = r.text
    # now r_html contains the HTML of the page
    soup = bs(r_html, 'html.parser')
    article = soup.find(id="article")

    print article.h1.string #prints the title of the article
    print article.h2.string #prints second title of the article
    # TODO: now I should go through each page (can edit url with the href value) and print out contents
    # TODO: ... of those while there still is 'next page' available
    # while next_page_a:
    #     article = soup.find(id="article")
    #     print_section(article)
    #     next_page_a = soup.find(id="nextpage").find('a', href=True)
    # a_href = next_page_a['href']
    # print a_href
    return article


print "Printing full article stretching over several pages: "
get_article('https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/')