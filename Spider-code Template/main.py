import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# 52


def s (i): 

    if i<=category_len('HELP/crawled.txt') :
        
        print("_____________________________________________________{}________________________________________________________________".format(i) )
        x1 = aaaaa('HELP/crawled.txt' , i).split('/')
        x=x1[3]
        PROJECT_NAME = x
        HOMEPAGE = 'http://www.bizrate.com/{}/ratings_guide/listing/'.format(x)
        DOMAIN_NAME = get_domain_name(HOMEPAGE)
        QUEUE_FILE = PROJECT_NAME + '/queue.txt'
        CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
        NUMBER_OF_THREADS = 5
        queue = Queue()
        Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

        # Create worker threads (will die when main exits)
        def create_workers():
            for _ in range(NUMBER_OF_THREADS):
                t = threading.Thread(target=work)
                t.daemon = True
                t.start()

            
            

        # Do the next job in the queue
        def work():
            while True:
                url = queue.get()
                Spider.crawl_page(threading.current_thread().name, url)
                queue.task_done()


        # Each queued link is a new job
        def create_jobs(i):
            for link in file_to_set(QUEUE_FILE):
                queue.put(link)
            queue.join()
            crawl(i)


        # Check if there are items in the queue, if so crawl them
        def crawl(i):
            queued_links = file_to_set(QUEUE_FILE)
            if len(queued_links) > 0:
                print(str(len(queued_links)) + ' links in the queue')
                create_jobs(i)
            else:
                for _ in range(NUMBER_OF_THREADS):
                    threading.current_thread()._stop
                    threading.current_thread()._delete
                s(i+1)
                # for _ in range(NUMBER_OF_THREADS):
                #     t = threading.Thread(target=work)
                #     t._stop

        create_workers()
        crawl(i)
s(0)