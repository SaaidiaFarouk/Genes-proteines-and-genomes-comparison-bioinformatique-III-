def manhattantourist(n,m,down,right):
    s=[[0]]
    for i in range(1,n+1):
        s.append([0])
        s[i][0]=s[i-1][0] + down[i-1][0]
    for j in range(1,m+1):
        s[0].append([0])
        s[0][j]=s[0][j-1] + right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1][j]+down[i-1][j] >= s[i][j-1]+right[i][j-1]:
                s[i].append(0)
                s[i][j]=s[i-1][j]+down[i-1][j]
            elif s[i-1][j]+down[i-1][j] <= s[i][j-1]+right[i][j-1]:
                s[i].append(0)
                s[i][j]=s[i][j-1]+right[i][j-1]
        
    return s[n][m]





with open("dataset.txt","r") as f : 
    data = f.readlines()
    f.close()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    mn=data[0].split(" ")
    n=int(mn[0])
    m=int(mn[1])
    p=data.index("-")
    down=list()
    right=list()
    for i in range(1,p):
        lst=data[i].split(" ")
        for j in range(len(lst)):
            lst[j]=int(lst[j])
        down.append(lst)
    for i in range(p+1,len(data)):
        lst=data[i].split()
        for j in range(len(lst)):
            lst[j]=int(lst[j])
        right.append(lst)
    
print(manhattantourist(n,m,down,right))