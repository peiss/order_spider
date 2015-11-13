# coding: GB18030
from conf.project_paths import JD_URL_LIST_FILE, JD_DATA_DIR
from parsers import jd_order_html_parser, jd_book_html_parser
from downloaders import jd_page_downloader

item_ids = []
for item_page_url in open(JD_URL_LIST_FILE):
    print "##############################"
    html_cont = jd_page_downloader.down_jd_page(item_page_url)
    item_ids.extend(jd_order_html_parser.get_item_ids(item_page_url, html_cont))
    
print item_ids

fout_all_data = open("%s/my_all_data.txt" % JD_DATA_DIR, 'w')
fout_book_data = open("%s/my_jd_books.txt" % JD_DATA_DIR, 'w')
fout_not_book_data = open("%s/my_jd_not_books.txt" % JD_DATA_DIR, 'w')

for item_id in set(item_ids):
    item_url = "http://item.jd.com/%s.html" % item_id
    print item_url

    item_html = jd_page_downloader.down_jd_page(item_url)
    if not item_html:
        continue
    
    item_data = jd_book_html_parser.get_jd_book_data(item_url, item_html)
    if item_data is not None:
        fout_all_data.write("\t".join((item_url, item_data["page_title"].encode('GB18030'))) + "\n")
        if item_data['is_book_page']:
            print item_data["title"], item_data["author"]
            fout_book_data.write("\t".join((item_data["title"], item_data["author"])) + "\n")
        else:
            print "not a book page:" + item_data["page_title"]
            fout_not_book_data.write(item_data["page_title"].encode('GB18030') + "\n")

fout_all_data.flush()
fout_all_data.close()
fout_book_data.flush()
fout_book_data.close()
fout_not_book_data.flush()
fout_not_book_data.close()
