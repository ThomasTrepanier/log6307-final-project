from bs4 import BeautifulSoup as soup
import requests, re
from selenium import webdriver
def scrape_page(_d, _link):
   _head, _paras = _d.find('h1', {'class':'head--bordered'}).text, [i.text for i in _d.find_all('p')]
   images = [i.img['src'] for i in _d.find_all('a', {'class':'fancybox'})]
   for img in images:
      _result, _url = requests.get(f'{_link}{img}').content, re.findall("\w+\.ashx$", img)
      if _url:
        with open('electroresults/{}.png'.format(_url[0][:-5]), 'wb') as f:
          f.write(_result)    
   return _head, _paras, images   


d = webdriver.Chrome('/path/to/chromedriver')
d.get('https://www.cst.com/solutions#size=5&TemplateName=Application+Article')
results, page, _previous = [], 1, None
while True:
  _articles = [i.get_attribute('href') for i in d.find_elements_by_class_name('searchResults__detail')]
  page_results = []
  previous = d.current_url
  for article in _articles:
    d.get(article)
    try:
      d.find_elements_by_class_name('interaction')[0].click()
    except:
      pass
    page_results.append(dict(zip(['title', 'paragraphs', 'imgs'], scrape_page(soup(d.page_source, 'html.parser'), d.current_url))))
    results.append(page_results)
  d.get(previous)
  _next = d.find_elements_by_class_name('pagination-link-next')
  if _next:
    _next[0].click()
  else:
    break
