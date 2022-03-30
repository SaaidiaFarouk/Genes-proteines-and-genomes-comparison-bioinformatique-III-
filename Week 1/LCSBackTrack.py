def lcsbacktrack(v,w):
    s=list()
    backtrack=list()
    for i in range(len(v)+1):
        s.append([0])
        backtrack.append(["."])
    for j in range(len(w)+1):
        s[0].append(0)
        backtrack[0].append(".")
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match=0
            if v[i-1] == w[j-1] :
                match = 1
            s[i].append(0)
            s[i][j]=max(s[i-1][j],s[i][j-1],s[i-1][j-1]+match)
            if s[i][j] == s[i-1][j]:
                backtrack[i].append(".")
                backtrack[i][j]="↓"
            elif s[i][j] == s[i][j-1]:
                backtrack[i].append(".")
                backtrack[i][j]="→"
            elif s[i][j] == s[i-1][j-1]+match:
                backtrack[i].append(".")
                backtrack[i][j]="↘"
    backtrack.pop(0)
    for lst in backtrack :
        l=len(lst)
        i=0
        while i < l :
            if lst[i]==".":
                lst.remove(lst[i])
                i-=1
                l-=1
            i+=1
    return backtrack

with open("dataset.txt","r") as f : 
    data=f.readlines()
    f.close()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    v=data[0]
    w=data[1]

print(lcsbacktrack(v,w))