# coding: GB18030
'''
@author: crazyant
'''
import urllib2

from cookies import jd_cookies


def get_jd_opener():
    handler = urllib2.HTTPCookieProcessor(jd_cookies.get_cookiejar())
    opener = urllib2.build_opener(handler)
    return opener

def get_jd_request(url):
    request = urllib2.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64)")
    request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    return request

def down_jd_page(jd_url):
    print "download jd url:%s" % jd_url
    urllib2.install_opener(get_jd_opener())
    response = urllib2.urlopen(get_jd_request(jd_url))
    if response.getcode() != 200:
        print "url can not access"
        return None
    html_doc = response.read()
    return html_doc

