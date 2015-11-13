# coding: GB18030

import re
from bs4 import BeautifulSoup
import urllib2
import logging

logging.basicConfig(level=logging.INFO)

def _is_book_page(html_doc):
    """判断页面是不是图书类
    """
    if re.search(r"图书", str(html_doc)):
        return True
    return False

def _parse_book_html(bs_soup):
    """解析图书页面，获得标题和作者
    """
    pdata = {}
    
    try:
        item_info_node = bs_soup.find("div", id="product-intro").find("div", id="itemInfo")
    
        pdata['title'] = item_info_node.find("div", id="name").find("h1").get_text()
        pdata['author'] = item_info_node.find("div", id="name").find("div", id="p-author").get_text()
    
        pdata['title'] = pdata['title'].encode("GB18030").strip()
        pdata['author'] = pdata['author'].encode("GB18030").strip()
    except Exception as e:
        print '解析出现异常：'
        print e
        return None
    
    return pdata

def _get_title(bs_soup):
    """获取页面的title
    """
    return bs_soup.find("title").get_text()


def get_jd_book_data(url, html_doc):
    print "get url jd book data, url=%s" % (url)
    
    """解析jd的书籍的数据
    """
    rs_data = {}
    bs_soup = BeautifulSoup(html_doc, "html.parser", from_encoding='GB18030')
    
    rs_data['page_title'] = _get_title(bs_soup)
    
    if not _is_book_page(html_doc):
        rs_data['is_book_page'] = False
    else:
        rs_data['is_book_page'] = True
        parse_data = _parse_book_html(bs_soup)
        if parse_data is not None:
            for k, v in parse_data.items():
                rs_data[k] = v
        else:
            return None
    return rs_data

if __name__ == "__main__":
    book_url = "http://item.jd.com/11322972.html"
    book_cont = urllib2.urlopen(book_url).read()
    book_data = get_jd_book_data(book_url, book_cont)
    print book_data["title"], book_data["author"]
    
    other_url = "http://item.jd.com/1045864.html"
    other_cont = urllib2.urlopen(other_url).read()
    other_data = get_jd_book_data(other_url, other_cont)
    print other_data
