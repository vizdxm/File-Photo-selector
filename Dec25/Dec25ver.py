import os
import shutil
import random

allf = os.listdir()
print(os.listdir())
#allf.pop(0)
fbylen= dict()
for i in allf:
    if len(i) in fbylen:
        fbylen[len(i)].append(i)
    else:
        fbylen[len(i)] = [i]
if len(fbylen[15])==1:
    del fbylen[15]
else:
    #fbylen[15].remove("_RunSelector.py")
    fbylen[15].remove("_Selected_Files")

def findse(x):
    variance = []
    for i in range(len(x[0])):
        variance.append(False)
    """
    for k in range(3):
        #a=random.randint(1,len(x)-1)
        for i in x:
            for j in range(len(i)):
                if i[j]!=x[a][j]:
                    variance[j] = True
    """

    for j in range(len(x[0])):
        s= set()
        for i in range(len(x)):
            s.add(x[i][j])
        if len(s)!=1:
            variance[j]=True
    s,e = -1,-1
    for i in range(len(x[0])):
        if variance[i] and s==-1:
            s=i
        elif not variance[i] and s!=-1:
            e=i
            break
    return s,e

def tostringlenl(n,l):
    ret = []
    for i in range(l):
        ret.append("0")
    print(ret)
    idx=l-1
    while(n):
        ret[idx] = str(n%10)
        n//=10
        idx-=1
    return "".join(ret)


while True:
    id = input("Paste ID list or type \"exit\" to end\n")
    if id=="exit":
        break
    else:
        id = id.strip().split()


    print(id)
    selected = []
    print(fbylen)
    for lenn in fbylen:
        s,e = findse(fbylen[lenn])
        print(s,e)
        form = fbylen[lenn][0]
        for i in id:
            selected.append(form[:s]+tostringlenl(int(i),e-s)+form[e:])

    os.makedirs("_Selected_Files",exist_ok=True)
    for i in selected:
        shutil.copy(i,"_Selected_Files/"+i)
    
