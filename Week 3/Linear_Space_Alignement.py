import copy
import sys
x=1000
sys.setrecursionlimit(x)
def middle_edge(v,w,penalties,top,bot,left,right):
    vrev=""
    wrev=""
    p=-1
    w=w[left:right]
    v=v[top:bot]

    
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



def linear_space_alignement(v,w,penalties,top,bot,left,right,):
    if left == right :
        path=(bot-top)*"↓"
        return path
    elif top == bot : 
        path=(right-left)*"→"
        return path
    mid= (right +left)/2
    mid=int(mid)
    mid_results=middle_edge(v,w,penalties,top,bot,left,right)
    mid_edge=mid_results[2]
    mid_node_coordinates=mid_results[0]
    mid_node=mid_node_coordinates[0]
    mid_node+=top
    lp=linear_space_alignement(v,w,penalties,top,mid_node,left,mid)
    if mid_edge == "→" or mid_edge == "↘" :
        mid +=1
    if mid_edge == "↓" or mid_edge == "↘" :
        mid_node += 1
    rp=linear_space_alignement(v,w,penalties,mid_node,bot,mid,right)
    return lp+mid_edge+rp
    

def lsa_backtrack(v,w,path,penalties):
    vallin=""
    wallin=""
    scor=0
    i=0
    a=0
    b=0
    for i in range(len(path)):
        if path[i]=="→":
            vallin+="-"
            wallin+=w[b]
            scor-=penalties[2]
            b+=1
        elif path[i]=="↘":
            vallin+=v[a]
            wallin+=w[b]
            if v[a]==w[b]:
                scor+=penalties[0]
            elif v[a]!=w[b]:
                scor-=penalties[1]
            a+=1
            b+=1
        elif path[i]=="↓":
            vallin+=v[a]
            wallin+="-"
            scor-=penalties[2]
            a+=1
    return scor,wallin,vallin
    



with open ("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    penalties=data[0].split(" ")
    for i in range(len(penalties)):
        penalties[i]=int(penalties[i])
    w=data[1]
    v=data[2]

top=0
bot=len(v)
left=0
right=len(w)

path=linear_space_alignement(v,w,penalties,top,bot,left,right)
print(path)
alignement=lsa_backtrack(v,w,path,penalties)
with open("answear.txt","w") as d:
    for a in alignement : 
        print(a)
        d.write(str(a)+"\n")