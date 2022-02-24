from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
import urllib.parse as urlparse
from urllib.parse import parse_qs

class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    twitter_file = ''
    facebook_file = ''
    shop_file = ''
    queue = set()
    crawled = set()
    shops = set()
    mail = set()
    facebook = set()
    twitter = set()


    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.shop_file= Spider.project_name + '/shops.txt'
        # Spider.twitter_file = Spider.project_name + '/Twitter.txt'
        # Spider.facebook_file = Spider.project_name + '/Facebook.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        # Spider.shops = file_to_set(Spider.facebook_file)
        # Spider.facebook = file_to_set(Spider.twitter_file)
        Spider.shops = file_to_set(Spider.shop_file)

    # Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    # Converts raw response data into readable information and checks for proper html formatting
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Saves queue data to project files
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                # if url.lower().find('@') > -1:
                #     Spider.mail.add(url)
                # if url.lower().find('facebook') > -1 :
                #     Spider.facebook.add(url)
                # if url.lower().find('twitter') > -1 :
                #     Spider.twitter.add(url)    
                continue
            if url.lower().find('http://www.bizrate.com/{}/ratings_guide/listing'.format(Spider.project_name)) ==-1:
                if url.lower().find('rd.bizrate') >-1:
                    parsed = urlparse.urlparse(url)
                    Spider.shops.add(parse_qs(parsed.query)['t'][0])
                else:
                    continue
            else:
                Spider.queue.add(url)
            

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        set_to_file(Spider.shops , Spider.shop_file)
        # set_to_file(Spider.mail , 'bizrate\mail.txt')
        # set_to_file(Spider.twitter , Spider.twitter_file)
        # set_to_file(Spider.facebook , Spider.facebook_file)
    @staticmethod
    def how_is_there():
        return len(Spider.queue)
    