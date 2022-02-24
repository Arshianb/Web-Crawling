import urllib.parse as urlparse
from urllib.parse import parse_qs
url = 'https://rd.bizrate.com/rd2?t=http%3A%2F%2Fclickserve.cc-dt.com%2Flink%2Fclick%3Flid%3D41000000005587322&mid=17213&catId=1&pos=1&tokenId=33&bId=23&cobrand=1&countryCode=US&sessionid=0&br=99999999999999999999999999999999999&data=_time%3A%3Astart_time%3D1583934417%3Btimestamp%3D1583934417%7Ctracker%3A%3Ahtcnt%3D1%3Brf%3Dbot%3Brf2%3Ddus'
parsed = urlparse.urlparse(url)
print(parse_qs(parsed.query)['t'][0])