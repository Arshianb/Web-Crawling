import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

ALL_OF_MY_CATEGORYS = read_file('category.txt')
i = read_file('category.txt')[0]
PROJECT_NAME = ALL_OF_MY_CATEGORYS[0].split('\n')[0]
DOMAIN_NAME = get_domain_name('https://w3techs.com/sites/')
NUMBER_OF_THREADS = 10
queue = Queue()
queue1 = set()
Spider(PROJECT_NAME, ALL_OF_MY_CATEGORYS[0].split('\n')[0], DOMAIN_NAME)

queue1 = file_to_set('category.txt')


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
        create_project_dir(category)
        create_data_files(category, Spider.category[0])
        Spider.crawl_page(threading.current_thread().name, category )
        queue.task_done()
        queue1.remove(category)
        set_to_file(queue1 , 'category.txt')
        


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