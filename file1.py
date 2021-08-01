aaa = 'aaa\nbbb\nccc\n'
ddd = 'ggg.txt'
f = open(ddd, 'w', encoding="utf-8")
f.writelines(aaa)
f.close()
