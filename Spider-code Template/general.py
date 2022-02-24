import os


# Each website is a separate project (folder)
def create_project_dir(project_name):
    if not os.path.exists(project_name):
        print('Creating directory ' + project_name)
        os.makedirs(project_name)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name  , 'queue.txt')
    crawled = os.path.join(project_name ,"crawled.txt")
    shops = os.path.join(project_name ,"shops.txt")
    # mail = os.path.join(project_name ,"mail.txt")
    # twitter = os.path.join(project_name ,"Twitter.txt")
    # facebook = os.path.join(project_name ,"Facebook.txt")
    # print(queue) this is printed 'arshia\queue.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    if not os.path.isfile(shops):
        write_file(shops, '')
    # if not os.path.isfile(mail):
    #     write_file(mail, '')
    # if not os.path.isfile(twitter):
    #     write_file(twitter, '')
    # if not os.path.isfile(facebook):
    #     write_file(facebook, '')
    

# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
 



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


def aaaaa(file_name , a):
    with open(file_name , 'r') as f:
        ff = []
        for line in f:
            ff.append(line)
        return(ff[a])
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
