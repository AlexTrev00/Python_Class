from openpyxl import Workbook
import os

#creamos objeto workbook()
wb = Workbook()

filesheet = "./demosheet.xlsx"

wb.save(filesheet)


