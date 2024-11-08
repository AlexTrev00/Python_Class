from openpyxl import load_workbook

#leer datos de excel

filesheet = "./demosheet.xlsx"
wb = load_workbook(filesheet)
sheet = wb.active
A1 = sheet['A1'].value
B5 = sheet['B5'].value
C5 = sheet['C5'].value
celdas = [A1,B5,C5]
for i in celdas:
    print(i)
    
