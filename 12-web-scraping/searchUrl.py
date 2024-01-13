#! python3
# searchUrl.py - Opens several search results on the given search engine.

import requests, sys, webbrowser, bs4

if len(sys.argv) < 3:
    print('Usage: searchUrl.py <searchUrl> <keywords>...')
    print('Where searchUrl can be: pypi, amazon')
    sys.exit()

print('Searching...')  # display text while downloading the search result page

# Get the searchUrl, assume it should start with "https://", otherwise assume it's just a keyword so use the default pypi.org
if sys.argv[1].lower() == 'pypi':
    searchUrl = 'https://pypi.org/search/?q='
    selector = '.package-snippet'
elif sys.argv[1].lower() == 'amazon':
    searchUrl = 'https://www.amazon.com/s?k='
    selector = 'div[data-component-type="s-search-result"] a'
else:
    print('Invalid search!')
    sys.exit()

res = requests.get(searchUrl + ' '.join(sys.argv[2:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select(selector)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = searchUrl[len('https://'):searchUrl.find('/', len('https://'))] + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
