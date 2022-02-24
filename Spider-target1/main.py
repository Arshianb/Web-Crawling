import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

ALL_OF_MY_CATEGORYS = read_file('category.txt')
HOW_MANY_CATEGORYS_I_READ = []
for i in ALL_OF_MY_CATEGORYS:
    shop_names = shops_name_in_there(i.split('\n')[0])
    j = 0 
    PROJECT_NAME = i.split('\n')[0]
    HOMEPAGE = []
    while j < how_many_shop_is_there(i.split('\n')[0]):

        shop_name = shop_names.iloc[j]['Shops']
        a = shop_name
        if shop_name.find('www') >-1:
            shop_name = shop_name[shop_name.find('www'):]
            if shop_name.find('/')>-1:
                shop_name = shop_name[shop_name.find('www'):shop_name.find('/')]
            else:
                shop_name = shop_name[shop_name.find('www'):]
        elif shop_name.find('http://')>-1:
            shop_name = shop_name[shop_name.find('http://')+7:]
            if shop_name.find('/')>-1:
                shop_name = shop_name[:shop_name.find('/')]
            else:
                shop_name = shop_name
        elif shop_name.find('https://')>-1:
            shop_name = shop_name[shop_name.find('https://')+8:]
            if shop_name.find('/')>-1:
                shop_name = shop_name[:shop_name.find('/')]
            else:
                shop_name = shop_name
        HOMEPAGE.append('https://builtwith.com/{}'.format(shop_name))
        j = j +1    
    DOMAIN_NAME = get_domain_name('https://builtwith.com')
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    NUMBER_OF_THREADS = 8
    queue = Queue()
    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)



# # Create worker threads (will die when main exits)
# def create_workers():
#     for _ in range(NUMBER_OF_THREADS):
#         t = threading.Thread(target=work)
#         t.daemon = True
#         t.start()


# # Do the next job in the queue
# def work():
#     while True:
#         url = queue.get()
#         Spider.crawl_page(threading.current_thread().name, url)
#         queue.task_done()


# # Each queued link is a new job
# def create_jobs():
#     for categoty in ALL_OF_MY_CATEGORYS:
#         HOW_MANY_CATEGORYS_I_READ.append(categoty)

#     crawl()


# # Check if there are items in the queue, if so crawl them
# def crawl():
#     if len(ALL_OF_MY_CATEGORYS)>0:
#         print('how many categotys left = ' + str(ALL_OF_MY_CATEGORYS))
#         create_jobs()


# create_workers()
# crawl()
