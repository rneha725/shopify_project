#pip3 install requests bs4 html5lib pandas
#python3 scrape-shopify.py


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

domains = {}
search = ["", "designer", "jewelry", "watches", "t-shirt", "garden"]
# search=[""]

for searchStr in search:
    page = 1
    while(page < 101):
        URL = "https://www.globalshoplist.com/"+searchStr + \
            "?searchFields=domain,title,description&page="+str(page)
        print(URL)
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html5lib')
        for div in soup.findAll('div', attrs={'class': "gsl-shopList__ItemDomain"}):
            if(re.search(".com", div.text)):
                domains[div.text] = div.text
        page = page+1
    # print(URL)


df = pd.DataFrame(
    {'Domain Name': list(domains.values())})
df.to_csv('domains.csv', index=False, encoding='utf-8')
