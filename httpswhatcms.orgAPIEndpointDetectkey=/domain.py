from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(urls):
    try:
        results = get_sub_domain_name(urls).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''






# aa = url.find('=http://')
# b = url[aa:].find('.com')
# print(url[aa+1:b+4+aa])
# aa = url.find('=http')
# a= url[aa:].find('www.')
# b = url[a+aa:].find('.com')
# print(url[a+aa:b+4+a+aa])