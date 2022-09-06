import requests
from bs4 import BeautifulSoup
import pandas as pd

titles = []
categories = []
contents = []
total_pages = 69

for page in range (1,total_pages+1):
    print(f'page_number {page}')
    URL = f'https://banglatech.info/page/{page}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.findAll("h2",class_='entry-title')

    for item in items:
        link = item.find("a",href=True)
        detail_page = requests.get(link['href'])
        soup = BeautifulSoup(detail_page.content, "html.parser")
        titles.append(soup.find('h1',class_='entry-title').get_text())
        categories.append(soup.find('span',class_='cat-links').get_text())
        contents.append(soup.find('div',class_='entry-content').get_text().strip())
    
df = pd.DataFrame({'Title':titles,'Category':categories,'Content': contents}) 
df.to_csv('blog_data.csv', index=False, encoding='utf-8')