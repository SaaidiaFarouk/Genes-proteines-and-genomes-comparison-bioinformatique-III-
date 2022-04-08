def bactrackpred(backtrack,i,j):
    lst=list()
    lst.append(backtrack[i][j-1])
    lst.append(backtrack[i-1][j])
    lst.append(backtrack[i-1][j-1])
    return lst

def fitting_source(backtrack,i):
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
    return i

def score(val1,val2,blos62):
    for k in blos62.keys():
        if val1 == k : 
            for v in blos62[k]:
                if val2 == v[0] :
                    score=v[1]
    return int(score)

def Blos_backtrack_Fitting(v,w,blos62):
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
 

    return backtrack , s[ix][j] ,ix 

def Fitting_prot_alignement(v,w,blos62):
    ans =Blos_backtrack_Fitting(v,w,blos62)
    backtrack=ans[0]
    scor = ans[1]
    i = ans[2]
    j = len(backtrack[0])-1
    isource = fitting_source(backtrack,i)
    jsource = 1
    vallin=""
    wallin=""
    while i >= isource  and j >= jsource :
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


ans=Fitting_prot_alignement(v,w,blos62)

with open("answear.txt","w") as d :
    for a in ans : 
        d.write(a+"\n")



