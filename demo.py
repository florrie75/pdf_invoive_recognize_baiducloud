"""
已知文件夹的位置path
得到发票识别的excel表格
仅针对pdf形式的发票文件
"""
import time
import pdf_manage
from baidu_cloud import main
from json_excel import data_manage, list_output_excel

# 文件夹位置
path = r''
output_path = r""
folder = pdf_manage.pdf_m(path)
folder.print_all_pdfs_in_folder()
filenum = 0
Invoive_excel_data : list = []
for filename in folder.pdf_files:
    i = 0
    while i < folder.pdf_page[filenum]:

        text_data = main(path + '\\' + filename, i+1)
        time.sleep(5)
        Invoive_excel_data += data_manage(text_data, filename, i+1)
        i += 1
    filenum += 1
print(Invoive_excel_data)
list_output_excel(Invoive_excel_data, output_path)