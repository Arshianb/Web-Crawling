import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

ALL_OF_MY_CATEGORYS = read_file('category.txt')
i = read_file('category.txt')[0]
PROJECT_NAME = ALL_OF_MY_CATEGORYS[0].split('\n')[0]
DOMAIN_NAME = get_domain_name('https://builtwith.com')
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
queue1 = Queue()
queue1 = file_to_set('category.txt')
Spider(PROJECT_NAME, ALL_OF_MY_CATEGORYS[0].split('\n')[0], DOMAIN_NAME)
queue1.remove(ALL_OF_MY_CATEGORYS[0].split('\n')[0])
set_to_file(queue1 , 'category.txt')



# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        category = queue.get()
        Spider(category, category , DOMAIN_NAME)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for categoty in file_to_set('category.txt'):
        queue.put(categoty)
    queue.join()
    crawl()



# Check if there are items in the queue, if so crawl them
def crawl():
    queue_categorys = file_to_set('category.txt')
    if len(queue_categorys)>0:
        print(str(len(queue_categorys)) + ' categorys left')
        create_jobs()


create_workers()
crawl()
