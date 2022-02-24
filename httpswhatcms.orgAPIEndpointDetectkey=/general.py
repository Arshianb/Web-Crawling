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
        string = url.split('\n')[0] + ',' + ' | {}'.format(array) + '\n'
    except Exception:
        string = url + ',' + ' | {}'.format(array)+ '\n'
    with open(path, 'a') as f:
        f.write(string)



urls = set()
for i in read_file('category.txt'):
    try:
        i = i.split('\n')[0]
    except Exception :
        pass
    for c in  shops_name_in_there(i)['Shops']:
        try:
            c = c.split('\n')[0]
        except Exception :
                pass
        if c.lower().find('www') >-1:
            c = c[c.lower().find('www'):]
            if c.lower().find('/')>-1:
                c = c[c.lower().find('www'):c.lower().find('/')]
            else:
                c = c[c.lower().find('www'):]
        elif c.lower().find('http://')>-1:
            c = c[c.lower().find('http://')+7:]
            if c.lower().find('/')>-1:
                c = c[:c.lower().find('/')]
            else:
                c = c
        elif c.lower().find('https://')>-1:
            c = c[c.lower().find('https://')+8:]
            if c.lower().find('/')>-1:
                c = c[:c.lower().find('/')]
            else:
                c = c
        
        urls.add(c)
write_file('urls.txt' , '')
set_to_file(urls ,'urls.txt' )
# import csv
# reader = csv.DictReader(open("ecommerce.csv"))
# for raw in reader:
#     print(raw)
import csv




def read_all_urls():
    with open('ecommerce.csv','rt')as f:
        data = csv.reader(f)
        urls = []
        for row in data:
                urls.append(row[0])
    return urls
def read_all_urls_in_category(file):

    try:
        with open('{}\ecommerce.csv'.format(file),'rt')as f:
            data = csv.reader(f)
            urls = []
            for row in data:
                urls.append(row[0])
        return urls
    except Exception:
        return False
def give_me_ecommerce_of_this_site(url):
    with open('ecommerce.csv','rt')as f:
        data = csv.reader(f)
        urls = []
        for row in data:
                if url == row[0]:
                    return row[1][row[1].find("['")+2 : row[1].find("']")]
def give_me_ecommerce_of_each_categorys(stringg , category):
    try:
        with open('{}\ecommerce.csv'.format(category),'rt')as f:
            data = csv.reader(f)
            for row in data:
                if row[0].find(stringg)>-1:
                    return row[1]
    except Exception:
        return False
# # # # # # # # # # # # # # # # all_urls = set()
# # # # # # # # # # # # # # # # all_urls = file_to_set('urls.txt')
# # # # # # # # # # # # # # # # all_urls_in_csv = read_all_urls()
# # # # # # # # # # # # # # # # bbbb = set()
# # # # # # # # # # # # # # # # bbbb = file_to_set('urls.txt')
# # # # # # # # # # # # # # # # for url in all_urls:

# # # # # # # # # # # # # # # #     if url in all_urls_in_csv :
# # # # # # # # # # # # # # # #         bbbb.remove(url)
# # # # # # # # # # # # # # # # # set_to_file(bbbb , 'urls.txt')
# # # # # # # # # # # # # # # # set_to_file(bbbb , 'remaind_urls.txt')



# set_to_file(bbbb , 'urls.txt')
                
# for file in read_file('category.txt'):
#     try:
#         file = file.split('\n')[0]
#     except Exception :
#         pass
#     urls_in_each_categorys = read_all_urls_in_category(file)
#     if urls_in_each_categorys != False :
#         urls = read_all_urls()
#         for url in urls_in_each_categorys :
#             if not url in urls :
#                 ecommerce = give_me_ecommerce_of_each_categorys(url , file)
#                 if ecommerce != False :
#                     add_array_in_csv_file('ecommerce.csv' ,ecommerce , url )
        # os.remove('{}\crawled.txt'.format(file))
        # os.remove('{}\ecommerce.csv'.format(file))
        # os.remove('{}\queue.txt'.format(file))
        # os.rmdir(file)
        



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
# import urllib , json , request
# # for i in a_tags:
# #     if i.attrs['href'].find('/details/cm-')>-1  :
# with urllib.request.urlopen("https://whatcms.org/APIEndpoint/Detect?key={}&url={}" .format('4274ab6009a7fffcfc759a2dcdaa9e623b510d975ff0a13e9da7e47e174994f897f2a8' , 'brittandjules.com')) as url:
#     # print(url)
#     # response = urllib.urlopen(url)
#     data = json.loads(url.read().decode())
#     print(data)
#     if data["result"]["name"] != 'null':
#         print (data["result"]["name"])
#     elif data["result"]["msg"] == 'Too Many Requests':
#         print ('give_me_another_apikey')
#     elif data["result"]["msg"] == 'Failed: CMS or Host Not Found':
#         print ('Host Not Found')

# # # # # # # # # # # # # # # # # # # # # from urllib.request import urlopen
# # # # # # # # # # # # # # # # # # # # # import urllib , json , request
# # # # # # # # # # # # # # # # # # # # # import requests
# # # # # # # # # # # # # # # # # # # # # import time
# # # # # # # # # # # # # # # # # # # # # import sys







# # # # # # # # # # # # # # # # # # # # # def get_CMS_of_remaind_urls(page_url):
# # # # # # # # # # # # # # # # # # # # #     try:
# # # # # # # # # # # # # # # # # # # # #         apikey = '4316d11fe3223877493cae63fe69ed097e599c72f0db738a7c536828d84bfabb0e84c6'
# # # # # # # # # # # # # # # # # # # # #         with urllib.request.urlopen("https://whatcms.org/APIEndpoint/Detect?key={}&url={}" .format(apikey , page_url)) as url:
        
# # # # # # # # # # # # # # # # # # # # #             data = json.loads(url.read().decode())
# # # # # # # # # # # # # # # # # # # # #             if data["result"]["name"] != None:
# # # # # # # # # # # # # # # # # # # # #                 return data["result"]["name"]
# # # # # # # # # # # # # # # # # # # # #             elif data["result"]["msg"].find('Too Many Requests')>-1:
# # # # # # # # # # # # # # # # # # # # #                 return 'give_me_another_apikey'
# # # # # # # # # # # # # # # # # # # # #             elif data["result"]["msg"] == 'Failed: CMS or Host Not Found':
# # # # # # # # # # # # # # # # # # # # #                 return 'Host Not Found'
# # # # # # # # # # # # # # # # # # # # #             elif data["result"]["msg"] == 'Requested Url Was Unavailable':
# # # # # # # # # # # # # # # # # # # # #                 return data["result"]["msg"]
# # # # # # # # # # # # # # # # # # # # #             elif data["result"]["msg"].find('Server Failure')>-1:
# # # # # # # # # # # # # # # # # # # # #                 print('Server Failure')
# # # # # # # # # # # # # # # # # # # # #                 sys.exit()
# # # # # # # # # # # # # # # # # # # # #             elif data["result"]["msg"].find('Account disabled per violation of Terms and Conditions')>-1:
# # # # # # # # # # # # # # # # # # # # #                 print('Account disabled per violation of Terms and Conditions')
# # # # # # # # # # # # # # # # # # # # #                 sys.exit()
# # # # # # # # # # # # # # # # # # # # #             else:
# # # # # # # # # # # # # # # # # # # # #                 return data["result"]["msg"]
# # # # # # # # # # # # # # # # # # # # #     except Exception as e :
# # # # # # # # # # # # # # # # # # # # #         print('no internet access = ' + str(e))
# # # # # # # # # # # # # # # # # # # # #         sys.exit()

# # # # # # # # # # # # # # # # # # # # # urls_that_remaind = file_to_set('remaind_urls.txt')
# # # # # # # # # # # # # # # # # # # # # urls_that_remaindd = file_to_set('remaind_urls.txt')
# # # # # # # # # # # # # # # # # # # # # for i in urls_that_remaind:
    
# # # # # # # # # # # # # # # # # # # # #     cms = []
# # # # # # # # # # # # # # # # # # # # #     cms.append(get_CMS_of_remaind_urls(i))
# # # # # # # # # # # # # # # # # # # # #     add_array_in_csv_file('ecommerce.csv' ,cms , i )
# # # # # # # # # # # # # # # # # # # # #     print("add_array_in_csv_file('ecommerce.csv' ,{} , {} )".format(cms , i))
# # # # # # # # # # # # # # # # # # # # #     urls_that_remaindd.remove(i)
# # # # # # # # # # # # # # # # # # # # #     set_to_file(urls_that_remaindd , 'remaind_urls.txt')
# # # # # # # # # # # # # # # # # # # # #     print('{} removed from remaind_urls.txt' .format(i))
# # # # # # # # # # # # # # # # # # # # #     time.sleep(10)