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

def localsource(backtrack,i,j):
    while i > 0 and j > 0 :
        if backtrack[i][j]=="F":
            return i,j
        elif backtrack[i][j]=="↓":
            i-=1
        elif backtrack[i][j]=="→":
            j-=1
        elif backtrack[i][j]=="↘":
            i-=1
            j-=1

    return i,j

def DNA_backtrack_Local(v,w,penalties):
    s=list()
    backtrack=[["."]]
    s.append([0])
    for i in range(len(v)):
        s.append([0])
        backtrack.append(["."])
    for j in range(len(w)):
        s[0].append(0)
        backtrack[0].append(".")
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match=0
            if v[i-1] == w[j-1] :
                match = penalties[0]
            elif v[i-1] != w[j-1] :
                match = -penalties[1]
            s[i].append(0)
            s[i][j]=max(0,s[i-1][j]-penalties[2],s[i][j-1]-penalties[2],s[i-1][j-1]+match)
            
            if s[i][j] == 0 :
                backtrack[i].append(".")
                backtrack[i][j]="F"
            elif s[i][j] == s[i-1][j]-penalties[2]:
                backtrack[i].append(".")
                backtrack[i][j]="↓"
            elif s[i][j] == s[i][j-1]-penalties[2]:
                backtrack[i].append(".")
                backtrack[i][j]="→"
            elif s[i][j] == s[i-1][j-1]+match:
                backtrack[i].append(".")
                backtrack[i][j]="↘"
            
    sink=0
    for i in range(len(s)): 
        for j in range(len(s[i])):
            if s[i][j] > sink:
                sink=s[i][j]
                ix=i
                jx=j    
    for b in s :
        print(b)
    for a in backtrack : 
        print(a)
    return backtrack , s[ix][jx] ,ix ,jx


def DNA_local_alignement(v,w,penalties):
    ans=DNA_backtrack_Local(v,w,penalties)
    backtrack = ans[0]
    scor = ans[1]
    i = ans [2]
    j = ans [3]
    ans=localsource(backtrack,i,j)
    isource = ans[0]
    jsource = ans[1]
    vallin=""
    wallin=""
    while i > isource  and j > jsource :
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
                    elif backtrack[adv[0]][adv[1]]=="↘": 
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
        elif backtrack[i][j]=="F":
            vallin += v[i-1]
            wallin += w[j-1] 
            adv=(i,j)
            i-=1
            j-=1

    
    valinn=''
    walinn=''
    for i in range(len(vallin)):
        valinn+=vallin[len(vallin)-i-1]
        walinn+=wallin[len(vallin)-i-1]

    print(scor)
    print(valinn)
    print(walinn)
    return str(scor),valinn , walinn 
        






with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    v=data[1]
    w=data[2]

ans=DNA_local_alignement(v,w,penalties)
with open("answear.txt","w") as d :
    for a in ans : 
        d.write(a+"\n")

