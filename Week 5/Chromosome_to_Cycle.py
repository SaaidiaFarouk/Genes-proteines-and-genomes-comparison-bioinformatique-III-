def chromosome_to_cycle(chromosome):
    nodes=list()
    for chro in chromosome:
        nodes.append(9)
        nodes.append(9)
    for j in range(0,len(chromosome)):
        i = chromosome[j]
        if i > 0 :
            nodes[2*j]=2*i-1
            nodes[2*j+1]=2*i
        else : 
            nodes[2*j]=-2*i
            nodes[2*j+1]=-2*i-1
    return nodes


with open ("dataset.txt","r") as f : 
    data=f.readline()
    data=data.replace("\n","")
    data=data.replace("(","")
    data=data.replace(")","")
    chromosome=data.split(" ")
    chromosome=[int(chromosome[i]) for i in range(len(chromosome))]
ans=chromosome_to_cycle(chromosome)
print(ans)
with open("answear.txt","w") as d : 
    d.write("(")
    anstr=""
    for a in ans : 
        ao=str(a)
        anstr+=ao
        if ans.index(a)!=len(ans)-1:
            anstr+=" "
    d.write(anstr)
    d.write(")")
    d.close()
