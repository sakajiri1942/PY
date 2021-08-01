aaa = 'aaa\nbbb\nccc\n'
ddd = 'ggg.txt'
f = open(ddd, 'w', encoding="utf-8")
f.writelines(aaa)
f.close()

ff = open(ddd, 'r', encoding="utf-8")
ddd_data = ff.readlines()
ff.close()

print(ddd_data)