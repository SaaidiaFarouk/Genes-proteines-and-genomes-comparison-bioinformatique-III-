import copy
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
    for a in s: 
        print(a)
    return backtrack 

def middle_edge(v,w,penalties):
    print(v)
    print(w)
    vrev=""
    wrev=""
    p=-1
    # Determining mid
    mid=len(w)/2
    if len(w) % 2 == 0 : 
        val = True
    elif len(w) % 2 != 0 : 
        val = False
        mid=int(mid)
    # Ceating reverse strings
    for i in range(len(v)):
        vrev+=v[len(v)-i-1]
    for i in range(len(w)):
        wrev+=w[len(w)-i-1]
    lst=[(v,w),(vrev,wrev)]
    # Finding middle columns
    for strings in lst:
        p+=1
        if p == 0:
            backtrack=list()
        elif p == 1 : 
            v=strings[0]
            w=strings[1]
        s=[[0,-penalties[2]]]
        for i in range(0,len(v)):
            s.append([-penalties[2]*(i+1)])
        for j in range(0,len(w)):
            if j!=0:
                for i in range(0,len(v)+1):
                    s[i][0]=s[i][1]
                    s[i].pop()
                s[0].append(s[0][0]-penalties[2])
            for i in range(1,len(v)+1):
                if v[i-1] == w[j] :
                    match = penalties[0]
                elif v[i-1] != w[j] :
                    match = -penalties[1]
                s[i].append(0)
                s[i][1]=max(s[i-1][1]-penalties[2],s[i][0]-penalties[2],s[i-1][0]+match)
                if j == mid and p == 0:    
                    if s[i][1] == s[i-1][1]-penalties[2]:
                        backtrack.append("↓")
                    elif s[i][1] == s[i][0]-penalties[2]:
                        backtrack.append("→")
                    elif s[i][1] == s[i-1][0]+match:
                        backtrack.append("↘")

            if val == True : 
                if j == mid :
                    if p == 0 :
                        simiddle=copy.deepcopy(s)
                        break
                if j == mid-1:
                    if p ==1 :
                        tosinkii=copy.deepcopy(s)
                        tosinkii.reverse()
                        tosinki=[elem[::-1] for elem in tosinkii]
                        break
            elif val == False :
                if j == mid :
                    if p == 0 :
                        simiddle=copy.deepcopy(s)
                        break
                if j == mid :
                    if p == 1 :
                        tosinkii=copy.deepcopy(s)
                        tosinkii.reverse()
                        tosinki=[elem[::-1] for elem in tosinkii]
                        break

    #         for a in s : 
    #             print(a)
    #         print("\n")
 
    
    for a in simiddle : 
        print (a)
    print("\n")  
    # for a in backtrack : 
    #     print(a)
    # print("\n")

    for a in tosinki : 
        print (a)
    print("\n")       

    # Finding middle edge
    sums=list()
    middlenode=[[float("-inf"),float("-inf")]]
    for i in range(len(tosinki)):
        sums.append([tosinki[i][0]+simiddle[i][0],tosinki[i][1]+simiddle[i][1]])
        if sums[i][0] > middlenode[0][0] :
            middlenode[0]=sums[i]
            imdl=i
            middle=simiddle[i]
            sinki=simiddle[i+1]
    middlenode.append(sums[imdl+1])
    print(middle)
    print(sinki)
    print(middlenode)
    if middlenode[0][0]==middlenode[0][1]:
        print(int(mid),imdl)
        print(int(mid),imdl+1)
    elif middlenode[0][0]==middlenode[1][0]:
        print(int(mid),imdl)
        print(int(mid),imdl+1)
    elif middlenode[0][0]==middlenode[1][1]:
        print(int(mid),imdl)
        print(int(mid),imdl+1)

    return s


with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    w=data[1]
    v=data[2]

penalties_backtrack(v,w,penalties)

middle_edge(v,w,penalties)

