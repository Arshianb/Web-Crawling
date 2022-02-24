import os
import pandas as pd
from queue import Queue

# Each website is a separate project (folder)
def create_project_dir(project_name):
    if not os.path.exists(project_name):
        print('Creating directory ' + project_name)
        os.makedirs(project_name)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name  , 'queue.txt')
    crawled = os.path.join(project_name ,"crawled.txt")
    ecommerce = os.path.join(project_name ,"ecommerce.csv")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(ecommerce):
        write_file(ecommerce, '')

    

# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)



# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
 
# Add data onto an existing file
def append_to_csv_file(path, data):
    with open(path, 'a') as file:
        file.write(data)



def read_file(path_dir ):
    with open(path_dir , 'r') as f:
        ff = []
        for line in f:
            ff.append(line)
        return(ff)


    
# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")


def shops_name_in_there (category_name):
    a = pd.read_csv('EXCEL\{}\shop.csv'.format(category_name))
    return(a)

def how_many_shop_is_there (category_name):
    a = pd.read_csv('EXCEL\{}\shop.csv'.format(category_name))
    return(a.shape[0])
def convert_set_to_array (set_data):
    f=[]
    for i in set_data:
        f.append(i)
    return f

def read (ecommerce_file):
    try:
        return pd.read_csv(ecommerce_file)
    except Exception:
        f = []
        for i in range(30):
            f.append(i)
        return pd.DataFrame(columns=f)
def get_first():
    f = []
    for i in range(30):
        f.append(i)
    return pd.DataFrame(columns=f)

def save_in_file (df , ecommerce_file):
    df.to_csv(ecommerce_file)

def add_array_in_csv_file (path ,array , page_url ):
    # url = page_url.split('builtwith.com/')[1]
    url = page_url
    try:
        string = url.split('\n')[0] + ',' + ' | '.join(array) + '\n'
    except Exception:
        string = url + ',' + ' | '.join(array) + '\n'
    with open(path, 'a') as f:
        f.write(string)


# from bs4 import BeautifulSoup
# import requests
# page_url = 'https://builtwith.com/poshmark.com'
# print('page url = ' + page_url)
# page = requests.get(page_url)
# contents = page.content
# soup = BeautifulSoup(contents , features="html.parser")
# a_tags = soup.find_all('a')

# for i in a_tags:
#     if i.get('href').find('.com/shop/')>-1  :
#         print( 'ecommerce = ' + i.text)


        
# page_url = 'https://builtwith.com/store.yahoo.com'
# print('page url = ' + page_url)
# page = requests.get(page_url)
# contents = page.content
# soup = BeautifulSoup(contents , features="html.parser")
# a_tags = soup.find_all('a')

# for i in a_tags:
#     if i.get('href').find('.com/shop/')>-1  :
#         print( 'ecommerce = ' + i.text)



# page_url = 'https://builtwith.com/www.Adorama.com'
# print('page url = ' + page_url)
# page = requests.get(page_url )
# contents = page.content
# soup = BeautifulSoup(contents , features="html.parser")
# a_tags = soup.find_all('a')

# for i in a_tags:
#     if i.get('href').find('.com/shop/')>-1  :
#         print( 'ecommerce = ' + i.text)



# page_url = 'https://builtwith.com/www.americanbookwarehouse.com'
# print('page url = ' + page_url)
# page = requests.get(page_url )
# contents = page.content
# soup = BeautifulSoup(contents , features="html.parser")
# a_tags = soup.find_all('a')

# for i in a_tags:
#     if i.get('href').find('.com/shop/')>-1  :
#         print( 'ecommerce = ' + i.text)



# page_url = 'https://builtwith.com/www.basspro.com'
# print('page url = ' + page_url)
# page = requests.get(page_url )
# contents = page.content
# soup = BeautifulSoup(contents , features="html.parser")
# a_tags = soup.find_all('a')

# for i in a_tags:
#     if i.get('href').find('.com/shop/')>-1  :
#         print( 'ecommerce = ' + i.text)

# import urllib
# import json
# print('page url = ' + page_url)
# page = requests.get(page_url )
# contents = page.content
# soup = BeautifulSoup(contents , features="html.parser")
# a_tags = soup.find_all('a')

# for i in a_tags:
#     if i.get('href').find('.com/shop/')>-1  :
#         print( 'ecommerce = ' + i.text)
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import requests
# driver = webdriver.Chrome()
# page_url = 'https://w3techs.com/sites/info/www.zazzle.com'

# contents = driver.page_source
# soup = BeautifulSoup(contents ,  features="html.parser")
# a_tags = soup.findAll('a')
# buttons_tags = soup.findAll('input')
# for j in buttons_tags:
#     if j.get('type').find('submit')>-1 :
#         if j.get('wtx-context') :
#             driver = webdriver.Chrome()
#             driver.get(page_url)
#             button = driver.find_element_by_name('add_site')
#             button.click()
#             contents = driver.page_source
#             soup = BeautifulSoup(contents ,  features="html.parser")
#             a_tags = soup.findAll('a')
# for i in a_tags:
#     print(i)
    # if i.get('href').find('/details/cm-')>-1  :
    #     print(i.text)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import requests
# import time
# from selenium import webdriver


# page_url = 'https://w3techs.com/sites/info/brittandjules.com'
# page = requests.get(page_url)
# contents = page.content
# soup = BeautifulSoup(contents ,  features="html.parser")
# a_tags = soup.findAll('a')
# buttons_tags = soup.findAll('input')
# for j in buttons_tags:
#     print(j)
#     if j.attrs['type'].find('submit')>-1 and j.attrs['value'].find('Crawl ')>-1  :
#         driver = webdriver.Chrome()
#         driver.get(page_url)
#         button = driver.find_element_by_name('add_site')
#         button.click()
#         contents = driver.page_source
#         soup = BeautifulSoup(contents ,  features="html.parser")
#         a_tags = soup.findAll('a')
#         driver.close()

# for i in a_tags:
#     if i.attrs['href'].find('/details/cm-')>-1  :
