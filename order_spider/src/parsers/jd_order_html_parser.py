# coding: GB18030
from bs4 import BeautifulSoup

def get_order_id(href):
    """从再购买的URL中，提取订单ID，从http://cart.jd.com/cart/dynamic/reBuyForOrderCenter.action?wids=362458&amp;nums=1&amp;rid=1447404250976
    """
    href = str(href)
    fields = href.split("wids=")
    wids = str(fields[1]).split("&")[0]
    return wids.split(',')
    

def get_item_ids(url, html_doc):
    print "get url jd book data, url=%s" % (url)
    
    """解析jd的书籍的数据
    """
    bs_soup = BeautifulSoup(html_doc, "html.parser", from_encoding='GB18030')
    
    links = bs_soup.find_all("a", class_="btn-again")
    order_ids = []
    for link in links:
        href = link['href']
        order_ids.extend(get_order_id(href))
        
    return order_ids
        
