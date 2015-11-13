# coding: gbk
import xlrd

def read_excel_to_list(excel_file_path):
    ll = []    
    data = xlrd.open_workbook(excel_file_path)    
    table = data.sheets()[0]    
    curr_row = 0    
    while  curr_row < table.nrows:        
        ll.append(table.row_values(curr_row))        
        curr_row += 1    
    return ll
