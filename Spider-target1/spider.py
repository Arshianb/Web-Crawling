from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
import urllib.parse as urlparse
from urllib.parse import parse_qs

class Spider:

    project_name = ''
    base_urls = []
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    ecommerce_file = ''
    queue = set()
    crawled = set()
    ecommerce = set()


    def __init__(self, project_name, base_urls, domain_name):
        Spider.project_name = project_name
        Spider.base_urls = base_urls
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.ecommerce_file= Spider.project_name + '/ecommerce.txt'
        # Spider.twitter_file = Spider.project_name + '/Twitter.txt'
        # Spider.facebook_file = Spider.project_name + '/Facebook.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_urls)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_urls[0])
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        Spider.ecommerce = file_to_set(Spider.ecommerce_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_urls):
        i = 0
        for page_url in page_urls:
            if page_url not in Spider.crawled and page_url.split('\n')[0] not in Spider.crawled:
                
                
                print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
                Spider.add_links_to_ecommerce(Spider.gather_links(page_url))
                
                Spider.queue.clear()
                Spider.queue.add(page_urls[i])
                Spider.crawled.add(page_url)
                Spider.update_files()
            if i < len(page_urls) - 1 :
                    i=i+1

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_ecommerce(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            if url.lower().find('https://trends.builtwith.com/shop/') > -1:
                Spider.ecommerce.add(url.split('/shop/')[1])
            else:
                continue
            



            

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        set_to_file(Spider.ecommerce , Spider.ecommerce_file)
        # set_to_file(Spider.mail , 'bizrate\mail.txt')
        # set_to_file(Spider.twitter , Spider.twitter_file)
        # set_to_file(Spider.facebook , Spider.facebook_file)
