def bactrackpred(backtrack,i,j):
    lst=list()
    lst.append(backtrack[i][j-1])
    lst.append(backtrack[i-1][j])
    lst.append(backtrack[i-1][j-1])
    return lst

def score(val1,val2,pam250):
    for k in pam250.keys():
        if val1 == k : 
            for v in pam250[k]:
                if val2 == v[0] :
                    score=v[1]
    return int(score)

def localalignment(v,w,pam250):
    s=list()
    backtrack=[["."]]
    s.append([0])
    for i in range(len(v)):
        val2=w[0]
        s.append([score("-",val2,pam250)*(i+1)])
        backtrack.append(["."])
    for i in range(len(w)):
        val2=v[0]
        s[0].append(score("-",val2,pam250)*(i+1))
        backtrack[0].append(".")
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            s[i].append(0)
            s1=s[i-1][j]+score(v[i-1],"-",pam250)
            s2=s[i][j-1]+score("-",w[j-1],pam250)
            s3=s[i-1][j-1]+score(v[i-1],w[j-1],pam250)
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
        for j in range(len(s[i])):
            if s[i][j] > sink:
                sink=s[i][j]
                ix=i
                jx=j
    return backtrack,s[ix][jx],ix,jx

def localsource(backtrack,i,j):
    while i > 0 or j > 0 :
        if backtrack[i][j]=="F":
            return i,j
        elif backtrack[i][j]=="↓":
            i-=1
        elif backtrack[i][j]=="→":
            j-=1
        elif backtrack[i][j]=="↘":
            i-=1
            j-=1
    return 0,0

def iterativelocalalignment(backtrack,v,w,isource,jsource,isink,jsink):
    valin=""
    walin=""
    i=isink
    j=jsink
    while i >isource  and j > jsource :
        if backtrack[i][j]=="↓":
            valin+=v[i-1]
            walin+="-"
            i-=1
        elif backtrack[i][j]=="→":
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

with open("PAM_250.txt","r") as g :
    data=g.readlines()
    g.close()
    pam250=dict()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    alpha=data[0].split(" ")
    for i in range(1,len(data)):
        alphas=data[i].split(" ")
        pam250[alphas[0]]=[]
        for j in range(1,len(alphas)):
            tpl=(alpha[j-1],alphas[j])
            pam250[alphas[0]].append(tpl)
    
            

ans=localalignment(v,w,pam250)
backtrack=ans[0]
scor=ans[1]
isink=ans[2]
jsink=ans[3]


ans=localsource(backtrack,isink,jsink)
isource=ans[0]
jsource=ans[1]

ans=iterativelocalalignment(backtrack,v,w,isource,jsource,isink,jsink)
with open("answear.txt","w") as d :
    d.write(str(scor)+"\n")
    for an in ans :
        d.write(an+"\n")