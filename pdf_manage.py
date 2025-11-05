"""
输入文件夹位置
输出文件夹中所有pdf文件的位置、名称、页数
"""
import os
from PyPDF2 import PdfReader

class pdf_m:
    pdf_files = []
    pdf_page = []
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def print_all_pdfs_in_folder(self):
        # 获取文件夹中所有文件的列表
        file_list = os.listdir(self.folder_path)

        # 筛选出所有的PDF文件
        self.pdf_files = [f for f in file_list if f.lower().endswith('.pdf')]
        self.pdf_page = []
        if not self.pdf_files:
            print("文件夹中没有PDF文件。")
            return

        for filename in self.pdf_files:
            reader = PdfReader(self.folder_path + '\\' + filename)
            # 不解密可能会报错：PyPDF2.utils.PdfReadError: File has not been decrypted
            if reader.is_encrypted:
                reader.decrypt('')
            self.pdf_page.append(len(reader.pages))
        # return self.pdf_files, self.pdf_page

if __name__ == '__main__':
    path = r''
    folder = pdf_m(path)
    # files, pages = folder.print_all_pdfs_in_folder()
    folder.print_all_pdfs_in_folder()
    print(type(folder.pdf_files), folder.pdf_files)

    print(type(folder.pdf_page), folder.pdf_page)
