import os
import shutil

allf = os.listdir()
fbylen= dict()
for i in allf:
    if len(i) in fbylen:
        fbylen[len(i)].append(i)
    else:
        fbylen[len(i)] = [i]
if "_Selected_Files" in fbylen[15]:
    fbylen[15].remove("_Selected_Files")
if len(fbylen[15])==1:
    del fbylen[15]
else:
    fbylen[14].remove("_runsource.bat")
if len(fbylen[14])==1:
    del fbylen[14]
else:
    fbylen[14].remove("_runsource.bat")

    

def findse(x):
    variance = []
    for j in range(len(x[0])):
        s= set()
        for i in range(len(x)):
            s.add(x[i][j])
        variance.append(True if len(s)!=1 else False)
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
    selected = []
    for lenn in fbylen:
        s,e = findse(fbylen[lenn])
        form = fbylen[lenn][0]
        for i in id:
            selected.append(form[:s]+tostringlenl(int(i),e-s)+form[e:])
    os.makedirs("_Selected_Files",exist_ok=True)
    for i in selected:
        shutil.copy(i,"_Selected_Files/"+i)
