from urllib.request import urlopen
import urllib , json , request
from domain import *
from general import *
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import sys
def add_links_to_ecommerce(queue , crawled , page_url , category , urlss):
    apikeys = ['4316d11fe3223877493cae63fe69ed097e599c72f0db738a7c536828d84bfabb0e84c6']
    i = 0
    j = 1
    if not page_url in urlss:
        if not page_url in crawled :
            while True :
                ecommerce_array = get_CMS(apikeys[i] , page_url)
                if ecommerce_array.find('give_me_another_apikey')>-1:
                    if i == 0:
                        i=0
                    else:
                        i = i + 1
                elif ecommerce_array.find('exceeded your monthly request')>-1:
                    print(apikeys[i])
                    if i == 0:
                        i=0
                    else:
                        i = i + 1
                else:
                    break
                
                j = j+1
            # print('how many apikey used ======> {}' .format(j))
    else:
        ecommerce_array = give_me_ecommerce_of_this_site(page_url)
        

    print('ecommerce_array = {}' .format(ecommerce_array))
            # print('queue = {} | page_url = {} | category = {}' .format( queue , page_url , category))
    return ecommerce_array
def update_files(crawled_file ,queue_file , queue , crawled ):
    set_to_file(queue, queue_file)
    set_to_file(crawled, crawled_file)

def get_CMS(apikey , page_url):
    time.sleep(10)
    try:
        with urllib.request.urlopen("https://whatcms.org/APIEndpoint/Detect?key={}&url={}" .format(apikey , page_url)) as url:
        
            data = json.loads(url.read().decode())
            if data["result"]["name"] != None:
                return data["result"]["name"]
            elif data["result"]["msg"].find('Too Many Requests')>-1:
                return 'give_me_another_apikey'
            elif data["result"]["msg"] == 'Failed: CMS or Host Not Found':
                return 'Host Not Found'
            elif data["result"]["msg"] == 'Requested Url Was Unavailable':
                return data["result"]["msg"]
            elif data["result"]["msg"].find('Server Failure')>-1:
                print('Server Failure')
                sys.exit()
            else:
                return data["result"]["msg"]
    except Exception as e :
        print('no internet access = ' + str(e))
        sys.exit()