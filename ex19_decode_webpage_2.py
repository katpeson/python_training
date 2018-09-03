# http://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
# Using as a base my own solution for task 17 (decode web page 1)
# NOTE: original given 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture' is no longer in
# ... 4 pages, so I'll use 'https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/' instead!
# TODO: actual task 19
# TODO: need for to loop over all pages to print each out! And to figure out how to do that navigation between pages...

import requests
from bs4 import BeautifulSoup as bs


# My function to return titles from the main page (top only since rest is dynamic content)
def get_text(url):
    r = requests.get(url)
    r_html = r.text
    # now r_html contains the HTML of the page
    soup = bs(r_html, 'html.parser')
    # lists all articles in the top section of the website (seems the rest of the page is outside html)
    # TODO: here comes the code!


print "Printing full article stretching over several pages from: "
print_titles('https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/')