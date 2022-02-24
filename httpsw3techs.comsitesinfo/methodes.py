from urllib.request import urlopen
from domain import *
from general import *
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import sys
def add_links_to_ecommerce(queue , crawled , page_url , category):
    
    ecommerce_array = []
    try:
        page_url = page_url.split('\n')[0]
    except Exception :
        pass
    try:
        r=True
        # driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
        # driver.get(page_url)
        # # time.sleep(10)
        page = requests.get(page_url)
        contents = page.content
        soup = BeautifulSoup(contents ,  features="html.parser")
        a_tags = soup.findAll('a')
        h1 = soup.findAll('h1')
        buttons_tags = soup.findAll('input')
        for j in buttons_tags:
            if j.attrs['type'].find('submit')>-1 and j.attrs['value'].find('Crawl ')>-1  :
                driver = webdriver.Chrome()
                driver.minimize_window()
                driver.get(page_url)
                button = driver.find_element_by_name('add_site')
                button.click()
                contents = driver.page_source
                soup = BeautifulSoup(contents ,  features="html.parser")
                a_tags = soup.findAll('a')
                h1 = soup.findAll('h1')
                driver.close()
            else:
                r=False

        for i in a_tags:
            if i.attrs['href'].find('technologies/details/cm')>-1 :
                ecommerce_array.append(i.text)
            else:
                r=False
        for i in h1:
            if i.string==('Site under maintenance'):
                sys.exit()
    
            # print('ecommerce_array = {}' .format(ecommerce_array))
        
        # print('len(ecommerce_array) = {}' .format(len(ecommerce_array)))
    except Exception as e :
        print(str(e))
    time.sleep(10)

            # print('queue = {} | page_url = {} | category = {}' .format( queue , page_url , category))
    return ecommerce_array
def update_files(crawled_file ,queue_file , queue , crawled ):
    set_to_file(queue, queue_file)
    set_to_file(crawled, crawled_file)

# def get_CMS(apikey , page_url):
#     with urllib.request.urlopen("https://whatcms.org/APIEndpoint/Detect?key={}={}" .format(apikey , page_url)) as url:
#         data = json.loads(url.read().decode())
#         return data["result"]["name"]