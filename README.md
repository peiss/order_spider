# order_spider
抓取购物网站（京东、淘宝、亚马逊）的个人订单页面的物品列表以及物品详情

# 自动抓取京东的个人订单，并提取出书籍列表
1、按照/order_spider/src/common/chrome_cookie.py的提示，将获取的cookie，粘贴到/order_spider/datas/cookie_file/jd_cookie_file.txt
2、进入京东的个人订单页面，把所有的订单页面的URL，添加到/order_spider/datas/url_file/jd_url_list.txt
3、修改/order_spider/src/conf/project_paths.py中的PROJECT_DIR为自己的代码路径
4、运行/order_spider/src/spider_main/jd_spider.py
5、生成结果在/order_spider/datas/output/jd_data，包括所有的商品、书籍商品、非书籍商品三个列表文件

# 自动生成博客书单
步骤：
1、修改excel中的书单，地址在/order_spider/datas/my_books/input_my_booklist.xlsx
2、运行/order_spider/src/outputers/generate_my_booklist.py即可生成书单的HTML
3、输出HTML地址为：/order_spider/datas/my_books/output_my_booklist.html
4、复制HTML中的内容，到博客文章页面即可


