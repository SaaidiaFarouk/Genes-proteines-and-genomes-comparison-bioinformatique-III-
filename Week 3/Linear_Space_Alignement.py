import copy
import sys
x=15
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
        if p == 0:
            backtrack=["→"]
            # print("Normal")
        elif p == 1 : 
            v=strings[0]
            w=strings[1]
        #     print("Reversed")
        # print("\nStrings:")
        # print(v)
        # print(w,"\n")
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

    for sum in sums :
        if sum[0] >= middlenode[0][0] :
            middlenode[0]=sum
            if sums.count(sum)!=1:
                sums.reverse()
                x=sums.index(sum)
                sums.reverse()
            else:
                x=sums.index(sum)
            
    if len(v)!=1 and x!=len(v):
        middlenode.append(sums[x+1])
    elif len(v) == 1 and x == 0:
        middlenode.append(sums[x+1])
    
    if middlenode[0][0]==middlenode[0][1]:
        middlenod=(x,mid)
        nextnode=(x,mid+1)
        edge="→"
    elif middlenode[0][0]==middlenode[1][0]:
        middlenod=(x,mid)
        nextnode=(x+1,mid)
        edge="↓"
    elif middlenode[0][0]==middlenode[1][1]:
        middlenod=(x,mid)
        nextnode=(x+1,mid+1)
        edge="↘"
    
    return middlenod ,nextnode ,edge



def linear_space_alignement(v,w,penalties,top,bot,left,right,):
    print("We are now working on : \n",w[left:right],v[top:bot])
    if left == right :
        print("Left == Right \n")
        print(top)
        print(bot)
        path=(bot-top)*"↓"
        print("Path = ",path)
        return path
    elif top == bot : 
        print("Top == Bot")
        print(left)
        print(right)
        path=(right-left)*"→"
        print("Path = ",path)
        return path
    else :
        mid= (right +left)/2
        if (right +left)% 2 == 0 : 
            mid=int(mid)
        elif (right +left) != 0 : 
            mid=int(mid)
        
        mid_results=middle_edge(v,w,penalties,top,bot,left,right)
        print(mid_results[0])
        print(mid_results[1])
        print(mid_results[2],"\n")
        mid_edge=mid_results[2]
        mid_node_coordinates=mid_results[0]
        mid_node=mid_node_coordinates[0]
        second_results=linear_space_alignement(v,w,penalties,top,mid_node,left,mid)
        if second_results == None :
            return mid_edge
        mid_edge=second_results
        print("Second Recursion of ",w[left:right],v[top:bot],"\n",mid_edge,"= Mid Edge\n") 
        
        if mid_edge == "→" or mid_edge == "↘" :
            mid +=1
        if mid_edge == "↓" or mid_edge == "↘" :
            mid_node += 1

        print("mid = ",mid)
        print("RIGHT =",right)
        print("Mid_Node = ",mid_node)
        print("BOT = ",bot)
        print("\n")

        linear_space_alignement(v,w,penalties,mid_node,bot,mid,right)
        



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

linear_space_alignement(v,w,penalties,top,bot,left,right)