aaa = '\
田中,20歳,女性\n\
佐藤,30際,女性\n\
森田,25際,男性\n\
'
ddd = 'ggg.csv'
f = open(ddd, 'w', encoding="utf-8")
f.write(aaa)
f.close()

ff = open(ddd, 'r', encoding="utf-8")
ddd_data = ff.readlines()
ff.close()

for l_ddd_data in ddd_data:
    rrr = l_ddd_data.split(',')
    print(rrr[1])





