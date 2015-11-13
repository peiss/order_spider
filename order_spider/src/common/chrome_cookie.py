# coding: GB18030

"""
来自：http://www.redicecn.com/html/Python/20141204/480.html
先安装EditThisCookie插件（360浏览器貌似也支持这个插件）。打开要采集的网站，完成登录等操作，点击EditThisCookie图标，
点击“导出”按钮（向右箭头），当前页面（网站）的Cookies就被复制到剪贴板了，JSON格式的，将其粘贴到cookies.txt文件里，备用。
下面是相关代码，将cookies.txt里的数据加载到Python的CookieJar中：
"""

import json
import cookielib

def read_chrome_cookie(cookie_file):
    """读取使用EditThisCookie导出的chrome的cookie
    """
    cookie_jar = cookielib.MozillaCookieJar()
    cookies = open(cookie_file).read()
    for cookie in json.loads(cookies):
        cookie_jar.set_cookie(cookielib.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None, port_specified=False, domain=cookie['domain'], domain_specified=False, domain_initial_dot=False, path=cookie['path'], path_specified=True, secure=cookie['secure'], expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))    
    # cookie_jar中已经加载了当前页面的Cookie数据了，Enjoy!
    return cookie_jar
