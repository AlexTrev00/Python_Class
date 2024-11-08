from openpyxl import Workbook
import datetime

wb=Workbook()
ws = wb.active
ws.append([1,2,3])
#imprime la hora en excel 
ws['A2']=datetime.datetime.now()
wb.save("sample.xlsx")


