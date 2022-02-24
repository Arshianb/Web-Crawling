from urllib.request import urlopen
# from link_finder import LinkFinder
from domain import *
from general import *
from methodes import *
import urllib.parse as urlparse
from urllib.parse import parse_qs
import pandas as pd

class Spider:

    project_name = ''
    category = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    ecommerce_file = ''
    queue = set()
    crawled = set()
    ecommerce = set()


    def __init__(self, project_name, category, domain_name):
        Spider.project_name = project_name
        Spider.category = category
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.ecommerce_file= Spider.project_name + '/ecommerce.csv'
        self.boot()
        self.crawl_page('First spider', Spider.category)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.category[0])
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        Spider.ecommerce = file_to_set(Spider.ecommerce_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, category ):
        
        crawled = set()
        queue = set()
        j = 0
        queue_file = category + '/queue.txt'
        crawled_file = category + '/crawled.txt'
        ecommerce_file= category + '/ecommerce.csv'
        crawled = file_to_set(crawled_file)
        page_urls = []
        shop_names = shops_name_in_there(category)
        while j < how_many_shop_is_there(category):

            shop_name = shop_names.iloc[j]['Shops']
            if shop_name.lower().find('www') >-1:
                shop_name = shop_name[shop_name.find('www'):]
                if shop_name.lower().find('/')>-1:
                    shop_name = shop_name[shop_name.find('www'):shop_name.find('/')]
                else:
                    shop_name = shop_name[shop_name.find('www'):]
            elif shop_name.lower().find('http://')>-1:
                shop_name = shop_name[shop_name.find('http://')+7:]
                if shop_name.lower().find('/')>-1:
                    shop_name = shop_name[:shop_name.find('/')]
                else:
                    shop_name = shop_name
            elif shop_name.lower().find('https://')>-1:
                shop_name = shop_name[shop_name.find('https://')+8:]
                if shop_name.lower().find('/')>-1:
                    shop_name = shop_name[:shop_name.find('/')]
                else:
                    shop_name = shop_name
            page_urls.append(shop_name)
            j = j + 1

        i = 0
        for page_url in page_urls:
            ecommerce = set()
            if page_url not in crawled and page_url.split('\n')[0] not in crawled:
                if i < len(page_urls) - 1 :
                    queue.add(page_urls[i])
                ecommerce_array = []
                print(str(thread_name) + ' is in the category of  ' + category +  '|| and Queue ' + str(len(queue)) + ' | Crawled  ' + str(len(crawled))+ '|| in file of =  ' + category)
                ecommerce_array = add_links_to_ecommerce(queue , crawled , page_url , category , read_all_urls())
                if len(ecommerce_array)!= 0:
                    # for bb in ecommerce_array :
                    ecommerce.add(ecommerce_array)
                    queue.clear()
                    try : 
                        crawled.add(page_url.split('\n')[0])
                    except Exception :
                        crawled.add(page_url)
                    
                    ecommerce_arrayrrrr = convert_set_to_array(ecommerce)
                    add_array_in_csv_file(ecommerce_file ,ecommerce_arrayrrrr , page_url )
                    if not page_url in read_all_urls():
                        add_array_in_csv_file('ecommerce.csv' ,ecommerce_arrayrrrr , page_url )
                    # print('ecommerce_file = {} | ecommerce_array = {} | page_url = {}'.format(ecommerce_file , ecommerce_array , page_url) )
                    update_files(crawled_file ,queue_file,  queue , crawled )
                    if i < len(page_urls) - 1 :
                            i=i+1

    
