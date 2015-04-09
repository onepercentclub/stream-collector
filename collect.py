import urllib2
from settings import *

for server_url in SERVER_URLS:
    try:
        server_token = SERVER_TOKENS[server_url]

        api_headers = {'Authorization':'Token {0}'.format(server_token)}

        # Latest donations
        donations_source_url = "{0}{1}".format(server_url, '/api/donations/latest-donations/')
        request = urllib2.Request(donations_source_url, headers=api_headers)

        response = urllib2.urlopen(request)
        donation_json = response.read()

        donations_url = "{0}{1}".format(STREAM_SERVER, '/api/donations/')
        request = urllib2.Request(donations_url, donation_json, {'Content-Type': 'application/json'})

        print urllib2.urlopen(request).read()

    except KeyError:
        print 'Not token found for: {0}'.format(server_url)

