def scor(vallin,wallin,penalties):
    scor=0
    for i in range(len(vallin)):
        if vallin[i] == wallin[i]:
            scor+=penalties[0]
        elif vallin[i] != wallin[i] and vallin[i]!="-" and  wallin[i] !="-":
            scor-=penalties[1]
        elif vallin[i] =="-" or wallin[i]:
            scor-=penalties[2]
    return scor

def formation(stringaligned):
    string=""
    for i in stringaligned:
        if i !="-":
            string+=i
    return string

def bactrackpred(backtrack,i,j):
    lst=list()
    lst.append(backtrack[i][j-1])
    lst.append(backtrack[i-1][j])
    lst.append(backtrack[i-1][j-1])
    return lst

def penalties_backtrack(v,w,penalties):
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
    return backtrack 

def global_alignement(v,w,penalties):
    backtrack=penalties_backtrack(v,w,penalties)
    i = len(v)
    j = len(w)
    vallin=""
    wallin=""
    testv=""
    testw=""
    while i != 0 or j !=0 :

        if backtrack[i][j]=="↓":
            vallin+=v[i-1]
            wallin+="-"
            adv=(i,j)
            i-=1
        elif backtrack[i][j]=="→":
            vallin+="-"
            wallin+=w[j-1]
            adv=(i,j)
            j-=1
        elif backtrack[i][j]=="↘":
            lst= bactrackpred(backtrack,i,j)
            if "." not in lst :
                vallin += v[i-1]
                wallin += w[j-1] 
                adv=(i,j)
                i-=1
                j-=1
            elif lst.count(".") == 2 :
                if lst[0]=="." :
                    if backtrack[adv[0]][adv[1]]=="↓":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        i-=1
                    elif backtrack[adv[0]][adv[1]]=="→":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        i-=1
                    elif backtrack[adv[0]][adv[1]]=="↓": 
                        if adv[0] != i and adv[1] == j :     
                            vallin += v[i-1]
                            wallin += "-"
                            adv=(i,j)
                            i-=1
                        elif adv[0] != i and adv[1] != j : 
                            vallin += v[i-1]
                            wallin += w[j-1] 
                            adv=(i,j)
                            i-=1
                elif lst[1]=="." :
                    if backtrack[adv[0]][adv[1]]=="→":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        j-=1
                    elif backtrack[adv[0]][adv[1]]=="↓":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        j-=1
                    elif backtrack[adv[0]][adv[1]]=="↘": 
                        if adv[0] == i and adv[1] != j :
                            vallin += "-"
                            wallin += w[j-1]
                            adv=(i,j)
                            j-=1
                        elif adv[0] != i and adv[1] != j : 
                            vallin += v[i-1]
                            wallin += w[j-1] 
                            adv=(i,j)
                            j-=1
            elif lst.count(".") == 3:
                if backtrack[adv[0]][adv[1]]=="↓":
                    vallin += v[i-1]
                    wallin += w[j-1]
                    i-=1
                    j-=1

                elif backtrack[adv[0]][adv[1]]=="→":
                    vallin += v[i-1]
                    wallin += w[j-1]
                    i-=1
                    j-=1                
                elif backtrack[adv[0]][adv[1]]=="↘":
                    if adv[0] != i and adv[1] != j :
                        vallin += v[i-1]
                        wallin += w[j-1]
                        i-=1
                        j-=1
                    
                    elif adv[0] == i and adv[1] != j :
                        vallin += "-"
                        wallin += w[j-1]
                        i-=1
                        j-=1

                    elif adv[0] != i and adv[1] == j :
                        vallin += v[i-1]
                        wallin +="-"
                        i-=1
                        j-=1

        if vallin==testv or testw==wallin:
            if len(formation(vallin))!=len(v):
                while i != 0:
                    vallin += v[i-1]
                    wallin += "-"
                    i-=1
            elif len(formation(wallin))!=len(w):
                while j != 0:
                    vallin += "-"
                    wallin += w[j-1]
                    j-=1
        
        testv=vallin
        testw=wallin

        if len(formation(vallin))==len(v) or len(formation(wallin))==len(w) :
            if backtrack[adv[0]][adv[1]]=="→":
                for x in range(1,len(backtrack[1])):
                    backtrack[1][x]="→"
            if len(formation(vallin))==len(v) and len(formation(wallin))==len(w):
                break

    valinn=''
    walinn=''
    for i in range(len(vallin)):
        valinn+=vallin[len(vallin)-i-1]
        walinn+=wallin[len(vallin)-i-1]
    score=scor(valinn,walinn,penalties)
    return str(score),valinn , walinn 
        




with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    v=data[0]
    w=data[1]
penalties=[0,1,1]
ans=global_alignement(v,w,penalties)

with open("answear.txt","w") as d :
    for a in ans : 
        d.write(a+"\n")
count=0
for i in range(len(ans[1])):
    if ans[1][i]!=ans[2][i]:
        count+=1
print(count)    