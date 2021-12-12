import pandas as pd
import codecs

from openpyxl import Workbook

xd = pd.ExcelFile("D:\\1.xlsx")
df = xd.parse()
with codecs.open("D:\\1.html","w","utf-8") as html_file:
    html_file.write(df.to_html(header = True,index = False))

wb = Workbook("d:\\1.xlsx")

st = wb.get_sheet_by_name()


