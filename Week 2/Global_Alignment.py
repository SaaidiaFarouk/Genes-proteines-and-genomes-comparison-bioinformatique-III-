def bactrackpred(backtrack,i,j):
    lst=list()
    lst.append(backtrack[i][j-1])
    lst.append(backtrack[i-1][j])
    lst.append(backtrack[i-1][j-1])
    return lst



def lcsbacktrack(v,w,penalties):
    s=list()
    backtrack=[["."]]
    s.append([0])
    for i in range(len(v)):
        s.append([-penalties[2]*(i+1)])
        backtrack.append(["."])
    for j in range(len(w)):
        s[0].append(-penalties[2]*(j+1))
        backtrack[0].append(".")
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match=0
            if v[i-1] == w[j-1] :
                match = penalties[0]
            elif v[i-1] != w[j-1] :
                match = -penalties[1]
            s[i].append(0)
            s[i][j]=max(s[i-1][j]-penalties[2],s[i][j-1]-penalties[2],s[i-1][j-1]+match)
            if s[i][j] == s[i-1][j]-penalties[2]:
                backtrack[i].append(".")
                backtrack[i][j]="↓"
            elif s[i][j] == s[i][j-1]-penalties[2]:
                backtrack[i].append(".")
                backtrack[i][j]="→"
            elif s[i][j] == s[i-1][j-1]+match:
                backtrack[i].append(".")
                backtrack[i][j]="↘"

    return backtrack , s[i][j]


def iteraticeoutputlcs(backtrack,v,w):
    i=len(v)
    j=len(w)
    print(i,"  ",j)
    valin=""
    walin=""
    while i >0  and j > 0 :
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

    return valin , walin 







with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    v=data[1]
    w=data[2]


donnes=lcsbacktrack(v,w,penalties)
backtrack=donnes[0]
score=donnes[1]
ansos=list()
ans=iteraticeoutputlcs(backtrack,v,w)
with open ("answear.txt","w") as d : 
    d.write(str(score)+"\n")
    for i in range(len(ans)):
        anso=""
        for j in range(len(ans[i])):
            anso+=ans[i][len(ans[i])-1-j]
        ansos.append(anso)
        d.write(ansos[i]+"\n")








