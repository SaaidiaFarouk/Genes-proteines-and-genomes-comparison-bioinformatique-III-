import copy

def score(val1,val2,bloss62):
    for k in bloss62.keys():
        if val1 == k : 
            for v in bloss62[k]:
                if val2 == v[0] :
                    score=v[1]
    return int(score)


def middle_edge(v,w,bloss62):
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
    # print(mid)
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

        s=[[0,-5]]
        for i in range(0,len(v)):
            s.append([-5*(i+1)])
        for j in range(0,len(w)):
            if j!=0:
                for i in range(0,len(v)+1):
                    s[i][0]=s[i][1]
                    s[i].pop()
                s[0].append(s[0][0]-5)
            for i in range(1,len(v)+1):
                match=score(v[i-1],w[j],bloss62)
                s[i].append(0)
                s[i][1]=max(s[i-1][1]-5,s[i][0]-5,s[i-1][0]+match)
         
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
    v=data[0]
    w=data[1]

with open("Blossum_62.txt","r") as g :
    data=g.readlines()
    g.close()
    bloss62=dict()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    alpha=data[0].split(" ")
    for i in range(1,len(data)):
        alphas=data[i].split(" ")
        bloss62[alphas[0]]=[]
        for j in range(1,len(alphas)):
            tpl=(alpha[j-1],alphas[j])
            bloss62[alphas[0]].append(tpl)

ans=middle_edge(v,w,bloss62)
for a in ans :
    print(a)