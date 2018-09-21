# http://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html
# Take the code from the How To Decode A Website exercise, and instead of printing the results...
#  to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.
#
# Extras:
# Ask the user to specify the name of the output file that will be saved.

import requests
from bs4 import BeautifulSoup as bs


# goes through all pages on article and prints the content from those as text
def save_full_article_to_file(url):
    article = get_article(url)
    # save all content to a file
    with open('ex21_saved_article.txt', 'w') as open_file:
        print "Got inside writing method"
        open_file.write(
            "Writing to file multi-page article from: " + '\n'
            + url + '\n' + '\n' + '\n' + '\n'
            + article.h1.string + '\n' + '\n'
            + article.h2.string + '\n' + '\n'
            + get_full_content_as_string(url) + '\n' + '\n'
            + "The end of article")
    print "Saving article to file was finished"


def get_full_content_as_string(url):
    # go looking for more pages in the article and get ONLY content from those too
    has_next_page = True
    article = get_article(url)
    content = (article.find(id="body")).text
    while has_next_page:
        next_page_element = article.find(id="nextpage")
        if next_page_element is not None:
            next_page_url = next_page_element.find('a', href=True)
            article = get_article(url + next_page_url['href'])
            new_content = (article.find(id="body")).text
            content = content + '/n' + new_content
        else:
            has_next_page = False
    content = content.encode('ascii', 'ignore')
    return content


# finds the id="article" part of the html (incl. page_nav) and returns it
def get_article(url):
    r = requests.get(url)
    r_html = r.text
    # now r_html contains the HTML of the page
    soup = bs(r_html, 'html.parser')
    article = soup.find(id="article")
    return article


# main to run the task
if __name__ == "__main__":
    url_a = "https://www.theregister.co.uk/2014/08/26/top_ten_gaming_keyboard_and_mouse_combos/"
    save_full_article_to_file(url_a)
