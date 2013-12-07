"""
Totally created by http://stackoverflow.com/a/17357552/1401639
"""

import urllib2
import json

API_URL = 'https://www.googleapis.com/urlshortener/v1/url'

def shorten(url):
    postdata = {'longUrl':url}
    headers = {'Content-Type':'application/json'}
    req = urllib2.Request(
        API_URL,
        json.dumps(postdata),
        headers
    )
    ret = urllib2.urlopen(req).read()
    return json.loads(ret)['id']


"""
Return **True** if *url* looks like a result of
the *shorten* function. Return **False** other way.
"""
def is_short(url):
    return url.startswith('http://goo.gl/')


def expand(url):
    """
    :url: short url to expand.
    :returns: string, full url.
    """
    return json.loads(urllib2.urlopen(\
        '{0}?shortUrl={1}'.format(API_URL, url)).\
        read())['longUrl']
