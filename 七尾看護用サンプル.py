import glob
import openpyxl
import mojimoji
import re

files = glob.glob("C:/Users/sakajiri/Desktop/七尾看護答案/七尾看護答案0614excel4/*xlsx")

kaitou_file = "C:/Users/sakajiri/Desktop/七尾看護答案/回答例/回答例総合問題4.xlsx"
book = openpyxl.load_workbook(kaitou_file, data_only=True)
kaitou_sheet = book['Sheet1']

# kaitou_cell = kaitou_sheet['B1'].font.color.rgb
# kaitou_cell = kaitou_sheet['B1'].font.b

yoko = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
tate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print (yoko)
dummy = 0
all_inf = ''

for file in files:
    genten = 0
    seito = file.split('/')
    # print(seito[5])

    # 名前だけの表示
    # t2 = t1.replace('\n','')
    seito[5] = seito[5].replace(' ', '')
    seito[5] = seito[5].replace('　', '')
    seito[5] = seito[5].replace('七尾看護答案0614excel4\\', '')
    seito[5] = mojimoji.zen_to_han(str(seito[5]))
    seito[5] = seito[5].replace('Excel', '')
    seito[5] = re.sub('\d+', '', seito[5])

    print(seito[5])
    book = openpyxl.load_workbook(file, data_only=True)
    sheet = book['Sheet1']

    # cell2 = sheet['B1'].rgb
    B1cell = sheet['B1'].value

    for yokoz in yoko:
        for tatez in tate:
            cellnum = yokoz + str(tatez)
            henkan_kaitou_value = kaitou_sheet[cellnum].value
            henkan_value = sheet[cellnum].value

            if henkan_value != None:
                # len(str(henkan_value))
                henkan_value = mojimoji.zen_to_han(str(henkan_value))
                henkan_kaitou_value = mojimoji.zen_to_han(str(henkan_kaitou_value))
                # print (cellnum)

            if henkan_value != henkan_kaitou_value:
                genten = genten + 1
                # print(kaitou_sheet[cellnum].value)
                # print(sheet[cellnum].value)

    # print (cell)
    # 色
    if kaitou_sheet['B1'].font.color.rgb != sheet['B1'].font.color.rgb:
        genten = genten + 1
        # dummy = dummy
    # 太さ
    if kaitou_sheet['B1'].font.b != sheet['B1'].font.b:
        genten = genten + 1
        # dummy = dummy

    # if cell == kaitou_cell:
    #    print ("ok")

    print(genten)
    all_inf = all_inf + str(genten) + ',' + seito[5] + '\n'

f = open('七尾看護エクセル４の採点.csv', 'w', encoding='cp932')
f.writelines(all_inf)
f.close()