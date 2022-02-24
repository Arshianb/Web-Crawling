import os
import pandas as pd

# Each website is a separate project (folder)
def create_project_dir(project_name):
    if not os.path.exists(project_name):
        print('Creating directory ' + project_name)
        os.makedirs(project_name)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name  , 'queue.txt')
    crawled = os.path.join(project_name ,"crawled.txt")
    ecommerce = os.path.join(project_name ,"ecommerce.txt")
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


