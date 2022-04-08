import copy 
def formation(stringaligned):
    string=""
    for i in stringaligned:
        if i !="-":
            string+=i
    return string

def scor(vallin,wallin,penalties):
    scor=0
    for i in range(len(vallin)):
        if vallin[i] == wallin[i]:
            scor+=penalties[0]
        elif vallin[i] != wallin[i] and vallin[i]!="-" and  wallin[i] !="-":
            scor-=penalties[1]
        elif vallin[i] =="-" and vallin[i-1]!="-":
            scor-=penalties[2]
        elif wallin[i]=="-" and wallin[i-1]!="-":
            scor-=penalties[2]
        elif vallin[i]=="-" and vallin[i-1]=="-":
            scor-=penalties[3]
        elif wallin[i]=="-" and wallin[i-1]=="-":
            scor-=penalties[3]
    return scor

def bactrackpred(backtrack,i,j):
    lst=list()
    lst.append(backtrack[i][j-1])
    lst.append(backtrack[i-1][j])
    lst.append(backtrack[i-1][j-1])
    return lst

def threelevelgraph(penalties,v,w):
    ### Initialisation of the three level grpahs
    lower=[[-float('inf')]]
    lowerbacktrack=[["."]]
    upper=[[-float('inf')]]
    upperbacktrack=[["."]]
    middle=[[0]]
    middlebacktrack=[["."]]

    for i in range(len(v)):
        lower.append([-penalties[2]-penalties[3]*(i+1)])
        lowerbacktrack.append(["."])
        upper.append([-float('inf')])
        upperbacktrack.append(["."])
        middle.append([-penalties[2]-penalties[3]*(i+1)])
        middlebacktrack.append(["."])

    for i in range(len(w)):
        lower[0].append(-float('inf'))
        lowerbacktrack[0].append(".")
        upper[0].append(-penalties[2]-penalties[3]*(i+1))
        upperbacktrack[0].append(".")
        middle[0].append(-penalties[2]-penalties[3]*(i+1))
        middlebacktrack[0].append(".")


    ### completing the graphs 
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match=0
            if v[i-1] == w[j-1] :
                match = penalties[0]
            elif v[i-1] != w[j-1] :
                match = -penalties[1]

            lower[i].append(0)
            lower[i][j]=max(lower[i-1][j]-penalties[3],middle[i-1][j]-penalties[2])
            lowerbacktrack[i].append(".")
            if lower[i][j] == lower[i-1][j]-penalties[3]:
                lowerbacktrack[i][j] = "↓"
            elif lower[i][j] == middle[i-1][j]-penalties[2] :
                lowerbacktrack[i][j] = "M"
            
            

            upper[i].append(0)
            upper[i][j]=max(upper[i][j-1]-penalties[3],middle[i][j-1]-penalties[2])
            upperbacktrack[i].append(".")
            if upper[i][j] == middle[i][j-1]-penalties[2] :
                upperbacktrack[i][j] = "M"
            elif upper[i][j] == upper[i][j-1]-penalties[3] :
                upperbacktrack[i][j] = "→" 
            
              

            middle[i].append(0)
            middle[i][j]=max(lower[i][j],upper[i][j], middle[i-1][j-1]+match)
            middlebacktrack[i].append(".")
            if middle[i][j] == lower[i][j] : 
                middlebacktrack[i][j] = "L"
            elif middle[i][j] == middle[i-1][j-1]+match :
                middlebacktrack[i][j] = "↘"
            elif middle[i][j]  == upper[i][j] :
                middlebacktrack[i][j] = "U"
            
            
    for i in range(len(upper)):
        print (upper[i],"   " ,middle[i],"    ",lower[i])
    
    print("       upper                    middle                    lower")
    for i in range(len(upperbacktrack)):
        print(upperbacktrack[i],"   ",middlebacktrack[i],"   ",lowerbacktrack[i])

    return upperbacktrack , lowerbacktrack , middlebacktrack, middle[i][j]

def backtrackingthreelevels(penalties,v,w):
    testv=''
    testw=''
    graphs=threelevelgraph(penalties,v,w)
    upper=graphs[0]
    lower=graphs[1]
    middle=graphs[2]
    i = len(v)
    j = len(w)
    vallin=""
    wallin=""
    graph = copy.deepcopy(middle)
    while i != 0 or j !=0 :
        if graph[i][j] == "↘":
            lst= bactrackpred(graph,i,j)
            if "." not in lst :
                vallin += v[i-1]
                wallin += w[j-1] 
                adv=(i,j)
                i-=1
                j-=1
            elif lst.count(".") == 2 :
                if lst[0]=="." :
                    if graph[adv[0]][adv[1]]=="U":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        i-=1
                    elif graph[adv[0]][adv[1]]=="L":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        i-=1
                    elif graph[adv[0]][adv[1]]=="↘": 
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
                    if graph[adv[0]][adv[1]]=="U":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        j-=1
                    elif graph[adv[0]][adv[1]]=="L":
                        vallin += v[i-1]
                        wallin += w[j-1] 
                        adv=(i,j)
                        j-=1
                    elif graph[adv[0]][adv[1]]=="↘": 
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
                if graph[adv[0]][adv[1]]=="U":
                    vallin += v[i-1]
                    wallin += w[j-1]
                    i-=1
                    j-=1

                elif graph[adv[0]][adv[1]]=="L":
                    vallin += v[i-1]
                    wallin += w[j-1]
                    i-=1
                    j-=1
                
                elif graph[adv[0]][adv[1]]=="↘":
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
        elif graph[i][j] == "↓":
            vallin += v[i-1]
            wallin += "-"
            adv=(i,j) 
            i-=1
        elif graph[i][j]=="→":
            vallin += "-"
            wallin += w[j-1]
            adv=(i,j)    
            j-=1     
        elif graph[i][j]=="L" :
            graph=copy.deepcopy(lower)
            if graph[i][j] == "↓" or graph[i][j] =="M":
                vallin += v[i-1]
                wallin += "-"
                adv=(i,j)
                if graph[i][j] =="M":
                    graph=copy.deepcopy(middle)
                i-=1
        elif graph[i][j]=="U" :
            graph=copy.deepcopy(upper)
            if graph[i][j] == "→" or graph[i][j] =="M":
                vallin += "-"
                wallin += w[j-1]
                adv=(i,j)
                if graph[i][j] =="M":
                    graph=copy.deepcopy(middle)
                j-=1
        elif graph[i][j]=="M" :
            if graph == lower :
                if graph[i][j] == "↓" or graph[i][j] =="M":
                    vallin += v[i-1]
                    wallin += "-"
                    adv=(i,j)
                    i-=1
            elif graph == upper:
                if graph[i][j] == "→" or graph[i][j] =="M":
                    vallin += "-"
                    wallin += w[j-1]
                    adv=(i,j)
                    j-=1
            graph=copy.deepcopy(middle)
        
        print(vallin)
        print(wallin)

        if vallin==testv or testw==wallin:
            print(i,j)
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
        print("here")


        testv=vallin
        testw=wallin


        if len(formation(vallin))==len(v) or len(formation(wallin))==len(w) :
            if graph[adv[0]][adv[1]]=="U":
                for x in range(1,len(graph[1])):
                    graph[1][x]="U"
            if len(formation(vallin))==len(v) and len(formation(wallin))==len(w):
                break
    valinn=''
    walinn=''
    for i in range(len(vallin)):
        valinn+=vallin[len(vallin)-i-1]
        walinn+=wallin[len(vallin)-i-1]
    print(valinn)
    print(walinn)    
    score=scor(valinn,walinn,penalties)
    print(score)        
    return str(score),valinn , walinn 

with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    v=data[1]
    w=data[2]

ans=backtrackingthreelevels(penalties,v,w)
with open("answear.txt","w") as d :
    for a in ans : 
        d.write(a+"\n")