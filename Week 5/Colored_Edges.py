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

def Colored_Edges(chromosomes):
    edges=list()
    for chromosome in chromosomes : 
        nodes=chromosome_to_cycle(chromosome)
        for j in range(1,len(chromosome)):
            edges.append((nodes[2*j-1],nodes[2*j]))
        edges.append((nodes[2*len(chromosome)-1],nodes[0]))
    
    return edges


with open("dataset.txt","r") as f : 
    data = f.readline()
    data=data.replace("\n","")
    data=data.replace("(","")
    chromosome_parts=data.split(")")
    chromosome_parts.pop()
    chromosomes=list()
    j=0
    for chromosome_part in chromosome_parts :
        chromosomes.append(chromosome_part.split(" "))
        chromosomes[j]=[int(chromosomes[j][i]) for i in range(len(chromosomes[j]))]
        j+=1


ans = Colored_Edges(chromosomes)

with open("answear.txt","w") as d :
    for a in ans : 
        tpl="("+str(a[0])+", "+str(a[1])+")"
        d.write(tpl)
        if ans.index(a)!=len(ans)-1:
            d.write(", ")
    d.close()

