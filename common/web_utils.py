# coding=utf-8

import urllib
import urllib2

# Local modules
from common import debug, constants


def post_http(url, data, headers):
    data = urllib.urlencode(data)
    request = urllib2.Request(url, data)
    request.addheader(headers)

    response = urllib2.urlopen(request)


# HTML to BeautifulSoup
def fetch_url(url):
    debug.log("Fetching url: " + url)

    try:
        response = urllib2.urlopen(url)
        html = response.read()
        url = response.geturl()
    except urllib2.URLError:
        debug.log("Error fetching: " + text_utils.stringify(e))
        debug.err(e)
        return None

    return url, html
