import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

total_pages = 200

for page_no in range (143,total_pages+1):
    titles = []
    categories = []
    views = []
    contents = []
    print(f'page_number {page_no}')
    URL = f'https://www.techtunes.io/page/{page_no}'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.findAll("h3",class_='h5 card-title')

    for item in items:
        link = item.find("a",href=True)
        titles.append(link.get_text())
        detail_page = requests.get(link['href'])
        soup = BeautifulSoup(detail_page.content, "html.parser")
        
        try:
            categories.append(soup.find('span',class_='mdb badge badge-default badge-pill z-depth-1').get_text())
        except:
            categories.append("Not Defined")
        view_text = soup.find('a',class_='mdb btn btn-outline-primary white btn-rounded waves-effect px-1 py-2 z-depth-1-half w-30').get_text()
        views.append(''.join(re.findall(r'\d+,*\d+', view_text)))
        contents.append(soup.find('div',class_='card-body px-3 px-sm-4 mb-3').get_text().strip())

        df = pd.DataFrame({'Title':titles,'Category':categories,'Views':views,'Content': contents})
    # print(page_no)
    if page_no == 1: 
        # print('yo')
        df.to_csv('techtunes_data.csv', index=False, encoding='utf-8')
    else:
        df.to_csv('techtunes_data.csv', mode='a',index=False, header=False,  encoding='utf-8')
        

