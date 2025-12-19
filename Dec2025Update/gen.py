def tostringlenl(n,l):
    ret = []
    for i in range(l):
        ret.append("0")
    idx=l-1
    while(n):
        ret[idx] = str(n%10)
        n//=10
        idx-=1
    return "".join(ret)

for i in range(99):
    f = open(f'fourdigitfiles{tostringlenl(i,4)}.txt',"w")
    for j in range(i):
        f.write(str(i))
    f.close()
