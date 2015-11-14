# coding: gb18030

from conf import project_paths
from common import excel_utils

# for sort
readig_types = ["正在读", "已读", "翻阅类", "未读", "已丢失"]

def read_excel_to_list():
    """read the book list excel to list
    """
    return excel_utils.read_excel_to_list(project_paths.MY_BOOK_LIST_EXCEL)

def read_books_by_type(book_list):
    """ organize the books by reading type
    """
    books = {}
    for data in book_list:
        reading_type = data[0].encode('gb18030')
        if reading_type not in books:
            books[reading_type] = []
        book_name = data[1].encode('gb18030')
        book_author = data[2].encode('gb18030')
        books[reading_type].append((book_name, book_author))
    return books

def out_data(books):
    """ books[reading_type] = (book_name, book_author)
    output: reading form
    """
    fout = open(project_paths.MY_BOOK_LIST_OUTHTML, "w")
    
    if len(books) != len(readig_types):
        raise Exception("缺少了分类")
    
    for reading_type in readig_types:
        fout.write("<h2>%s</h2>\n" % reading_type)
        fout.write("<ul>\n")
        for (book_name, book_author) in books.get(reading_type):
            fout.write("<li>%s,%s</li>\n" % (book_name, book_author))
        fout.write("</ul>\n")    
    fout.flush()
    fout.close()

if __name__ == "__main__":
    print "read_excel_to_list"
    book_list = read_excel_to_list()
    print "read_books_by_type"
    book_data = read_books_by_type(book_list)
    print "out_data"
    out_data(book_data)
    print "over"

