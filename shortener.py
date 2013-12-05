"""
Totally created by http://stackoverflow.com/a/17357552/1401639
"""

import urllib2
import json

def shorten(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url'
    postdata = {'longUrl':url}
    headers = {'Content-Type':'application/json'}
    req = urllib2.Request(
        post_url,
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
