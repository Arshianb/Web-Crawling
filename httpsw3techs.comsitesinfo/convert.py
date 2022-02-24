import os
import pandas as pd
import numpy as np

# Each website is a separate project (folder)
def create_project_dir(project_name):
    if not os.path.exists(project_name):
        print('Creating directory ' + project_name)
        os.makedirs(project_name)


category_txt_path = 'category.txt'
# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name  , 'queue.txt')
    crawled = os.path.join(project_name ,"crawled.txt")
    shops = os.path.join(project_name ,"shops.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(shops):
        write_file(shops, '')



# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)



# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data )
 


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


def read_file(path_dir ):
    with open(path_dir , 'r') as f:
        ff = []
        for line in f:
            ff.append(line)
        return(ff)

# print(read_file('categorys.txt'))
# for i in read_file('categorys.txt'):
#     append_to_file('category.txt' , i.split('/')[3])

def category_len(file_name):
    with open(file_name , 'r') as f:
        ff = []
        for line in f:
            ff.append(line)
        return(len(ff))


def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")


# pd.DataFrame(read_file(category_txt_path)).to_csv(category_excel_path, mode='a', header=False)
# for i in read_file(category_txt_path):
#     a = read_file('TXT\{}\{}'.format(i.split('\n')[0],'shops.txt'))
#     aa = pd.DataFrame(a)
#     # write_file('EXCEL\{}\{}'.format(i.split('\n')[0],'shops.csv') , '')
#     # aa.to_csv('EXCEL\{}\{}'.format(i.split('\n')[0],'shops.csv'))
