import copy

def middle_edge(v,w,penalties):
    vrev=""
    wrev=""
    p=-1
    # Determining mid
    mid=len(w)/2
    if len(w) % 2 == 0 : 
        val = True
        mid=int(mid)
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
        if p == 1 : 
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

            if val == True : 
                if j == mid :
                    if p == 0 :
                        simiddle=copy.deepcopy(s)
                        break
                if j == mid-1 :
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
             

    
    
    
    # Finding middle edge
    sums=list()
    middlenode=[[float("-inf"),float("-inf")]]
    for i in range(len(simiddle)):
        sums.append([tosinki[i][0]+simiddle[i][0],tosinki[i][1]+simiddle[i][1]])


    sums_zero=list()
    for sum in sums:
        sums_zero.append(sum[0])
    maxi=float("-inf")
    for sum in sums :
        if sum[0] > maxi :
            maxi=sum[0]
            if sums_zero.count(sum[0])!=1:
                sums_zero.reverse()
                x=sums_zero.index(sum[0])
                sums_zero.reverse()
                x=len(sums)-1-x
                middlenode[0]=sums[x]
            else:
                x=sums_zero.index(sum[0])
                middlenode[0]=sums[x]
            
    if len(v)!=1 and x!=len(v):
        middlenode.append(sums[x+1])
    elif len(v) == 1 and x == 0:
        middlenode.append(sums[x+1])
    if len(middlenode)==1:
        middlenod=(x,mid)
        nextnode=(x,mid+1)
        edge="→"
        return middlenod ,nextnode ,edge
    if middlenode[0][0]==middlenode[1][1]:
        middlenod=(x,mid)
        nextnode=(x+1,mid+1)
        edge="↘"
    elif middlenode[0][0]==middlenode[0][1]:
        middlenod=(x,mid)
        nextnode=(x,mid+1)
        edge="→"
    elif middlenode[0][0]==middlenode[1][0]:
        middlenod=(x,mid)
        nextnode=(x+1,mid)
        edge="↓"
    
    
    return middlenod ,nextnode ,edge

with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    w=data[1]
    v=data[2]



ans=middle_edge(v,w,penalties)
for a in ans :
    print(a)

