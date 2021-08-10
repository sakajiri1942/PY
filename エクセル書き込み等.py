#Excelへの新規書き込み
import openpyxl
ttt = openpyxl.Workbook()
sss = ttt.active
sss.title = 'eee'
sss['C3'] = 'bbb'
ttt.save('aaa.xlsx')

#Excelの読み込みはここから
ttt2 = openpyxl.load_workbook('aaa.xlsx')
sss2 = ttt2["eee"]
print(sss2["C3"].value)