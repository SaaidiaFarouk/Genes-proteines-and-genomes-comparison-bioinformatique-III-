import copy 
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
            if upper[i][j] == upper[i][j-1]-penalties[3] :
                upperbacktrack[i][j] = "→"  
            elif upper[i][j] == middle[i][j-1]-penalties[2] :
                upperbacktrack[i][j] = "M"
              

            middle[i].append(0)
            middle[i][j]=max(lower[i][j],upper[i][j], middle[i-1][j-1]+match)
            middlebacktrack[i].append(".")
            if middle[i][j] == lower[i][j] : 
                middlebacktrack[i][j] = "L"
            elif middle[i][j] == middle[i-1][j-1]+match :
                middlebacktrack[i][j] = "↘"
            elif middle[i][j]  == upper[i][j] :
                middlebacktrack[i][j] = "U"
            
            
    print("lower = ")
    for a in lower : 
        print(a)
    print("middle = ")
    for a in middle : 
        print(a)
    print("upper = ")
    for a in upper : 
        print(a)
    
    
    print("lowerbacktrack = ")
    for b in lowerbacktrack : 
        print(b)
    print("middlebacktrack = ")
    for b in middlebacktrack :
        print(b)

    print("upperbacktrack = ")
    for b in upperbacktrack : 
        print(b)

    return upperbacktrack , lowerbacktrack , middlebacktrack, middle[i][j]

def backtrackingthreelevels(penalties,v,w):
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
        if graph[i][j] == "↘" :
            vallin += v[i-1]
            wallin += w[j-1]
            i-=1
            j-=1
        elif graph[i][j] == "→" : 
            vallin += "-"
            wallin += w[j-1]
            j-=1
        elif graph[i][j] == "↓":
            vallin += v[i-1]
            wallin += "-"
            i-=1
        if graph[i][j] == "U" :
            graph[i][j] = upper[i][j]
        elif graph[i][j] == "L" :
            graph[i][j] = lower[i][j]
        elif graph[i][j] == "M" :
            graph[i][j] = middle[i][j]

        print(vallin)
        print(wallin)
        if len(vallin)==2:
            break
    return vallin , wallin 

with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    v=data[1]
    w=data[2]

backtrackingthreelevels(penalties,v,w)