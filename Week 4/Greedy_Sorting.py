import copy
def checksort(k,p):
    val=True
    for i in range(0,k):
        if abs(p[i])!=i+1:
            val=False
    return val

def k_sorting(k,p):
    if k in p:
        g=p.index(k)
    elif -k in p :
        g=p.index(-k)
    
    px=p[k-1:g+1]
    px.reverse()
    j=0
    for i in range(k-1,g+1):
        p[i]=0-px[j]
        j+=1

    return p

def Greedy_Sorting(p):
    permutations=list()
    approxreversaldisatnce=0
    for k in range(1,len(p)+1):
        if checksort(k,p)==False:
            p=copy.deepcopy(k_sorting(k,p))
            px=copy.deepcopy(p)
            permutations.append(px)
            approxreversaldisatnce+=1
        if p[k-1] == -k :
            p[k-1]=0-p[k-1]
            px=copy.deepcopy(p)
            permutations.append(px)
            approxreversaldisatnce+=1
            

    return permutations


with open("dataset.txt","r") as f : 
    data=f.readline()
    data=data.replace("\n","")
    p=data.split(" ")
    for i in range(len(p)):
        p[i]=int(p[i])

ans=Greedy_Sorting(p)
with open ("answear.txt","w") as d:
    for a in ans :
        print(a)
        stri=""
        for num in a:
            if num >0:
                stri+="+"
            stri+=str(num)
            stri+=" "
        stri=stri.rstrip()
        d.write(stri+"\n")

        
