import urllib2
from secrets import *

# Latest donations

url = "{0}{1}".format(ONEPERCENT_SERVER, '/api/fund/latest-donations/')
req = urllib2.Request(url, headers = {'Authentication' : 'Token {0}'.format(ONEPERCENT_API_TOKEN)})

