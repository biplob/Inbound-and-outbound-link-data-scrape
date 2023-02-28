# Import all necessary libaries
import requests
from bs4 import BeautifulSoup
import  re


# funcation to extract html documents from giver url
def getHTMLdocument(url):
    # Request for Html document from given url
    response = requests.get(url_to_scrape)
    # response will be provide in JSON formate
    return response.text


# Assign url
url_to_scrape = 'https://eshikhon.com.bd/all-courses/'
# create documents
html_documents = getHTMLdocument(url_to_scrape)
# create soup object
soup = BeautifulSoup(html_documents, 'html.parser')

# find all the anchor tags with "href"
# attribute starting with "htpps://"
for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    # display actual url
    print(link.get('href'))



