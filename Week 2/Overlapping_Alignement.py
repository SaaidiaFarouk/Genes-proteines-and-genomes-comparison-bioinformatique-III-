def lcsbacktrack(v,w,penalties):
    s=list()
    backtrack=[["."]]
    s.append([0])
    for i in range(len(v)):
        s.append([0])
        backtrack.append(["."])
    for j in range(len(w)):
        s[0].append(-(j+1)*penalties[1])
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

    sink=0
    for j in range(1,len(s[0])): 
        if s[len(v)][j] >= sink:
            sink=s[len(v)][j]
            jx=j  
    return backtrack , s[len(v)][jx] ,jx


def Overlapping_Alignement(backtrack,v,w,jsink):
    valin=""
    walin=""
    i=len(v)
    j=jsink
    while j != 0 :
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
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    v=data[1]
    w=data[2]



donnes=lcsbacktrack(v,w,penalties)

backtrack=donnes[0]

scor=donnes[1]

jx = donnes[2]



ans=Overlapping_Alignement(backtrack,v,w,jx)


scor=0
for i in range(len(ans[0])):
    if ans[0][i]==ans[1][i]:
        scor+=penalties[0]
    elif ans[0][i]!=ans[1][i] and (ans[0][i]!="-"and ans[1][i]!="-"):
        scor-=penalties[1]
    elif ans[0][i]=="-" or ans[1][i]=="-":
        scor-=penalties[2]



with open("answear.txt","w") as d :
    d.write(str(scor)+"\n")
    for an in ans :
        d.write(an+"\n")