def bactrackpred(backtrack,i,j):
    lst=list()
    lst.append(backtrack[i][j-1])
    lst.append(backtrack[i-1][j])
    lst.append(backtrack[i-1][j-1])
    return lst

def score(val1,val2,blos62):
    for k in blos62.keys():
        if val1 == k : 
            for v in blos62[k]:
                if val2 == v[0] :
                    score=v[1]
    return int(score)

def localalignment(v,w,blos62):
    s=list()
    backtrack=[["."]]
    s.append([0])
    for i in range(len(v)):
        s.append([0])
        backtrack.append(["."])
    for i in range(len(w)):
        val2=v[0]
        s[0].append(score("-",val2,blos62)*(i+1))
        backtrack[0].append(".")
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            s[i].append(0)
            s1=s[i-1][j]+score(v[i-1],"-",blos62)
            s2=s[i][j-1]+score("-",w[j-1],blos62)
            s3=s[i-1][j-1]+score(v[i-1],w[j-1],blos62)
            s[i][j]=max(0,s1,s2,s3)
            if s[i][j] == 0 :
                backtrack[i].append(".")
                backtrack[i][j]="F"
            elif s[i][j] == s1:
                backtrack[i].append(".")
                backtrack[i][j]="↓"
            elif s[i][j] == s2:
                backtrack[i].append(".")
                backtrack[i][j]="→"
            elif s[i][j] == s3:
                backtrack[i].append(".")
                backtrack[i][j]="↘"
    sink=0
    for i in range(len(s)): 
        if s[i][len(w)] >= sink:
            sink=s[i][j]
            ix=i
    for a in s :
        print(a)
    for bac in backtrack :
        print(bac)
    return backtrack,s[ix][j],ix

def localsource(backtrack,i):
    j=len(backtrack[0])-1
    while j!=1 :
        if backtrack[i][j]=="F":
            j-=1
        elif backtrack[i][j]=="↓":
            i-=1
        elif backtrack[i][j]=="→":
            j-=1
        elif backtrack[i][j]=="↘":
            i-=1
            j-=1
    return i,j

def iterativelocalalignment(backtrack,v,w,isource,jsource,isink,jsink):
    valin=""
    walin=""
    i=isink
    j=jsink
    while i != isource-1  and j != jsource-1 :
        if backtrack[i][j]=="↓":
            valin+=v[i-1]
            walin+="-"
            i-=1
        elif backtrack[i][j]=="→":
            valin+="-"
            walin+=w[j-1]
            j-=1
        elif backtrack[i][j]=="F":
            valin+="-"
            walin+=w[j-1]
            j-=1
        elif backtrack[i][j]=="↘":
            valin+=v[i-1]
            walin+=w[j-1]
            lst= bactrackpred(backtrack,i,j)
            if "." in lst and ("↓" in lst or "→" in lst or "↘" in lst) :
                if lst[0]!=".":
                    j-=1
                elif lst[1]!=".":
                    i-=1
            else :
                j-=1
                i-=1
    valinn=''
    walinn=''
    for i in range(len(valin)):
        valinn+=valin[len(valin)-i-1]
        walinn+=walin[len(valin)-i-1]
    return valinn , walinn 
 




with open ("dataset.txt","r") as f : 
    data=f.readlines()
    v=data[0].replace("\n","")
    w=data[1].replace("\n","")
    f.close()

with open("Blossum_62.txt","r") as g :
    data=g.readlines()
    g.close()
    blos62=dict()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    alpha=data[0].split(" ")
    for i in range(1,len(data)):
        alphas=data[i].split(" ")
        blos62[alphas[0]]=[]
        for j in range(1,len(alphas)):
            tpl=(alpha[j-1],alphas[j])
            blos62[alphas[0]].append(tpl)

ans=localalignment(v,w,blos62)
backtrack=ans[0]
scor=ans[1]
isink=ans[2]
jsink=len(backtrack[0])-1
print(isink)


ans=localsource(backtrack,isink)
isource=ans[0]
jsource=ans[1]
print(ans)


ans=iterativelocalalignment(backtrack,v,w,isource,jsource,isink,jsink)
for a in ans:
    print(a)

print("Score = ",scor)
scor=0
for i in range(len(ans[0])):
    scor+=score(ans[0][i],ans[1][i],blos62)
print("Score = ",scor)
with open("answear.txt","w") as d :
    d.write(str(scor)+"\n")
    for an in ans :
        d.write(an+"\n")