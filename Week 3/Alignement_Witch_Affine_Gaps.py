def threelevelgraph(penalties,v,w):
    upper=[[0]]
    lower=[[0]]
    middle=[[0]]
    for i in range(len(v)):
        lower.append([0])
        upper.append([0])
        middle.append([0])
    for i in range(len(w)):
        lower[0].append(0)
        upper[0].append(0)
        middle[0].append(0)
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match=0
            if v[i-1] == w[j-1] :
                match = penalties[0]
            elif v[i-1] != w[j-1] :
                match = -penalties[1]
            lower[i].append(0)
            lower[i][j]=max(lower[i-1][j]-penalties[3],middle[i-1][j]-penalties[2])
            upper[i].append(0)
            upper[i][j]=max(upper[i][j-1]-penalties[3],middle[i][j-1]-penalties[2])
            middle[i].append(0)
            middle[i][j]=max(lower[i][j],upper[i][j], middle[i-1][j-1]+match)
    print("lower = ")
    for a in lower : 
        print(a)
    print("upper = ")
    for a in upper : 
        print(a)
    print("middle = ")
    for a in middle : 
        print(a)

    return upper , lower , middle



with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    v=data[1]
    w=data[2]

threelevelgraph(penalties,v,w)