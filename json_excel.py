'''
输入json变量
提取特定值
输出到excel表格中
'''
import json
import pandas as pd

# 封装数据
class Record:
    def __init__(self, name, model, unit, num, price, money, tax, tax_rate):
        self.name = name  # 材料名称
        self.model = model  # 型号
        self.unit = unit  # 单位
        self.num = num  # 数量
        self.price = price # 单价
        self.money = money  # 金额
        self.tax_rate = tax_rate  # 税率
        self.tax = tax  # 税额

        self.pack = [name,model,unit,num,price,money,tax_rate,tax]
    def __str__(self):
        return f"材料名称:{self.name}\n\规格型号:{self.model}\n单位:{self.unit}\n数量:{self.num}\n单价:{self.price}\n金额:{self.money}\n税率:{self.tax_rate}\n税额:{self.tax}"

class Invoice:
    def __init__(self, InvoiceCode, InvoiceNum, InvoiceNumDigit, SellerRegisterNum, SellerName, PurchaserRegisterNum, PurchaserName, InvoiceDate, TotalAmount, TotalTax, AmountInFiguers):
        self.InvoiceCode = InvoiceCode
        self.InvoiceNum = InvoiceNum
        self.InvoiceNumDigit =  InvoiceNumDigit
        self.SellerRegisterNum = SellerRegisterNum
        self.SellerName = SellerName
        self.PurchaserRegisterNum = PurchaserRegisterNum
        self.PurchaserName = PurchaserName
        self.InvoiceDate = InvoiceDate
        self.TotalAmount = TotalAmount
        self.TotalTax = TotalTax
        self.AmountInFiguers = AmountInFiguers

        self.pack = [InvoiceCode,InvoiceNum,InvoiceNumDigit,SellerRegisterNum,SellerName,PurchaserRegisterNum,PurchaserName,InvoiceDate,TotalAmount,TotalTax,AmountInFiguers]
    def __str__(self):
        return f"发票代码:{self.InvoiceCode}\n发票号码:{self.InvoiceNum}\n数电票号:{self. InvoiceNumDigit}\n销售方纳税人识别号:{self.SellerRegisterNum}\n销售方名称:{self.SellerName}\n购买方识别号:{self.PurchaserRegisterNum}\n购方名称:{self.PurchaserName}\n开票日期:{self.InvoiceDate}\n合计金额:{self.TotalAmount}\n合计税额:{self.TotalTax}\n价税合计:{self.AmountInFiguers}"
# 提取需要的值
def Invoive_read(json_data: str) -> Invoice:
    data = json.loads(json_data)['words_result']
    Invoice_data = Invoice(data['InvoiceCode'],data['InvoiceNum'],data['InvoiceNumDigit'],data['SellerRegisterNum'],data['SellerName'],data['PurchaserRegisterNum'],data['PurchaserName'],data['InvoiceDate'],data['TotalAmount'],data['TotalTax'],data['AmountInFiguers'])
    return Invoice_data
def JsonReader(json_data: str) -> list[Record]:
    record_list: list[Record] = []
    data = json.loads(json_data)['words_result']
    for l in data['CommodityName']:
        name  = l['word']# 材料名称
        row = l['row']
        try:
            model = list(filter(lambda d: d.get('row') == row, data['CommodityType']))[0]['word']
        except IndexError:
            model = ' '
        try:
            unit = list(filter(lambda d: d.get('row') == row, data['CommodityUnit']))[0]['word']# 单位
        except IndexError:
            unit = ' '
        try:
            num  = float(list(filter(lambda d: d.get('row') == row, data['CommodityNum']))[0]['word'])# 数量
        except IndexError:
            num = ' '
        try:
            price  = list(filter(lambda d: d.get('row') == row, data['CommodityPrice']))[0]['word']# 数量
        except IndexError:
            price = 0
        try:
            money = list(filter(lambda d: d.get('row') == row, data['CommodityAmount']))[0]['word']# 金额
        except IndexError:
            money = 0
        try:
            tax_rate = list(filter(lambda d: d.get('row') == row, data['CommodityTaxRate']))[0]['word']# 税额
        except IndexError:
            tax_rate = 0
        try:
            tax = list(filter(lambda d: d.get('row') == row, data['CommodityTax']))[0]['word']# 税额
        except IndexError:
            tax = 0


        record = Record(name, model, unit, num, float(price), float(money), tax_rate, float(tax))
        record_list.append(record)
    return record_list

# 输出到excel表格中
def list_output_excel(l, output_path):
    df = pd.DataFrame(l,
                      columns=['文件名', '页数', '发票代码', '发票号码', '数电票号', '销售方纳税人识别号', '销售方名称','购买方识别号', '购方名称', '开票日期', '合计金额', '合计税额', '价税合计', '名称','规格型号', '单位', '数量', '单价', '金额', '税率', '税额'
                               ]
                      )
    df.to_excel(output_path, index=False)

def data_manage(json_data, filename, page):
    data_list: list[Record] = JsonReader(json_data)
    Invoice_data: Invoice = Invoive_read(json_data)
    data = []
    data0 = [filename, page] + Invoice_data.pack
    for l in data_list:
        a = ['']*13 + l.pack
        data.append(a)
    data.insert(0,data0)
    return data

if __name__ == '__main__':
    path = r'C:\Users\Admin\Desktop\FH\研二上\实验室\2\4.txt'
    f = open(path, 'r', encoding='UTF-8')
    json_data = f.read()
    data = data_manage(json_data)
    list_output_excel(data)