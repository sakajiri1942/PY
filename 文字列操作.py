
aaa = 'おはよう'
bbb = 'ございます'
ccc = aaa + bbb
print(ccc)

aaa = 'おはよう'
bbb =  100
ccc = aaa + str(bbb)
print(ccc)

aaa = 200
bbb = 100
ccc = aaa + bbb
print(ccc)

aaa = 200
bbb = 100
ccc = str(aaa) + str(bbb)
print(ccc)



aaa = 200
bbb = 100
ccc = str(aaa) + str(bbb)
print(ccc)
ddd = int(ccc) - 200
print(ddd)


##################################
#文字列操作
aaa = 'ABCDEF'
bbb = aaa.replace('CD','xyz')
print(bbb)

aaa = '3,5,7,11,13,17,19'
bbb = aaa.split(',')
print(bbb)


aaa = 'おはようございます'
bbb = aaa.split('よ')
print(bbb)


aaa = '3,5,7,11,13,17,19'
bbb = aaa.split(',')
print(bbb[3])



