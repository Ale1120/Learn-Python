c = 0
while c < 5:
    c+=1
    print('c vale',c)
else:
    print('se termino c',c)


c = 0
while c < 5:
    c+=1
    if c==2:
        print('detenimos c con un break en ,',c)
        break
    print('c vale',c)
else:
    print('se termino c',c)



c = 0
while c < 5:
    c+=1
    if c==3:
        print('continuamos c con un continue en ,',c)
        continue
    print('c vale',c)
else:
    print('se termino c',c)
