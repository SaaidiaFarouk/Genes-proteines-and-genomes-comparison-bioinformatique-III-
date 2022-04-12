def bactrackpred(backtrack,i,j):
    lst=list()
    lst.append(backtrack[i][j-1])
    lst.append(backtrack[i-1][j])
    lst.append(backtrack[i-1][j-1])
    return lst

def overlapping_source(backtrack,i,j):
    while j!=1 or backtrack[i][j]=="↓":
        if backtrack[i][j]=="↓":
            i-=1
        elif backtrack[i][j]=="→":
            j-=1
        elif backtrack[i][j]=="↘":
            i-=1
            j-=1
        elif backtrack[i][j]==".":
            i+=1
            j+=1
            break
    return i

def Overlapping_DNA_Backtrack(v,w,penalties):
    s=list()
    backtrack=[["."]]
    s.append([0])
    for i in range(len(v)):
        s.append([0])
        backtrack.append([(".")])
    for j in range(len(w)):
        s[0].append(-(j+1)*penalties[2])
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
    
def Overlapping_DNA_ALignement(v,w,penalties):
    ans=Overlapping_DNA_Backtrack(v,w,penalties)
    backtrack=ans[0]
    i=len(v)
    scor=ans[1]
    j=ans[2]
    vallin=""
    wallin=""
    isource=overlapping_source(backtrack,i,j)
    while   j > 0 and i>=isource:
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
                        j-=1
                    elif backtrack[adv[0]][adv[1]]=="→":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        i-=1
                        j-=1
                    elif backtrack[adv[0]][adv[1]]=="↘": 
                        if adv[0] != i and adv[1] == j :     
                            vallin += v[i-1]
                            wallin += "-"
                            adv=(i,j)
                            i-=1
                            j-=1
                        elif adv[0] != i and adv[1] != j : 
                            vallin += v[i-1]
                            wallin += w[j-1] 
                            adv=(i,j)
                            i-=1
                            j-=1
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
        
    valinn=''
    walinn=''
    for i in range(len(vallin)):
        valinn+=vallin[len(vallin)-i-1]
        walinn+=wallin[len(vallin)-i-1]

    print(scor)
    print(valinn)
    print(walinn)
    return str(scor),valinn , walinn
    
    return

with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    v=data[1]
    w=data[2]


ans=Overlapping_DNA_ALignement(v,w,penalties)

with open("answear.txt","w") as d :
    for a in ans : 
        d.write(a+"\n")