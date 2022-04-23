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

def two_break_distance(p,q):
    distance=0
    # find the number of cycles:
     #create the simetrique of p using q 
    q_colored_edges=Colored_Edges(q)
    p_colored_edges=Colored_Edges(p)
    print(q_colored_edges)
    print(p_colored_edges)
     #create the superimposing graph 
     #calculate teh number of cycles in q 
     
    # find the number fo blocks in p and q 
      # they have teh same number fo blocks which is teh number of their colored edges 
    # find the difference between block - cycles
    return distance


with open ("dataset.txt","r") as f : 
    data = f.readlines()
    for i in range(len(data)):
        data[i]=data[i].rstrip("\n")
    p=data[0].split(")(")
    q=data[1].split(")(")
    genomes=[p,q]
    for j in range(len(genomes)) :
        for i in range(len(genomes[j])):
            genomes[j][i]=genomes[j][i].rstrip(")")
            genomes[j][i]=genomes[j][i].lstrip("(")
            genomes[j][i]=genomes[j][i].split(" ")
            for y in range(len(genomes[j][i])):
                genomes[j][i][y]=int(genomes[j][i][y])
print(p,q)
ans=two_break_distance(p,q)
print(ans)