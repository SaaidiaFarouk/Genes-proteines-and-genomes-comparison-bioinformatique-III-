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

def compositions(nodes):
    composition=list()
    for node in nodes : 
        for n in node : 
            composition.append(n)
    return composition

def colored_cycle(pedges,qedges):
    cycles=list()
    pcomp=compositions(pedges)
    qcomp=compositions(qedges)
    while len(pcomp)!=0:
        cycle=list()
        strnode=min(pcomp)
        for edge in pedges:
            if strnode in edge:
                m=edge.index(strnode)
                if m==0:
                    tpl1=edge[::-1]
                else:
                    tpl1=edge
                cycle.append(tpl1)
        if pcomp.index(strnode)%2==0:
            finalnode=pcomp[pcomp.index(strnode)+1]
        else:
            finalnode=pcomp[pcomp.index(strnode)-1]
        pcomp.pop(pcomp.index(strnode))
        qcomp.pop(qcomp.index(strnode))
        nextnode=0
        while nextnode!=finalnode:
            for edge in qedges:
                if strnode in edge : 
                    m=edge.index(strnode)
                    n=1-m
                    nextnode=edge[n]
                    if m==1:
                        tpl1=edge[::-1]
                    else:
                        tpl1=edge
                    cycle.append(tpl1)
                    qcomp.pop(qcomp.index(nextnode))
                    pcomp.pop(pcomp.index(nextnode))
                    break
            for edge in pedges : 
                if nextnode in edge: 
                    m=edge.index(nextnode)
                    n=1-m
                    strnode=edge[n]
                    if m==1:
                        tpl1=edge[::-1]
                    else:
                        tpl1=edge
                    cycle.append(tpl1)
                    if strnode in pcomp:
                        pcomp.pop(pcomp.index(strnode))
                        qcomp.pop(qcomp.index(strnode))
                    break
            
        cycle.pop()   
        cycles.append(cycle)    

    return cycles

def two_break_distance(p,q):
    distance=0
     
    qedges=Colored_Edges(q)
    pedges=Colored_Edges(p)
    cycles=colored_cycle(pedges,qedges)
    number_of_cycles=len(cycles)
    number_of_blocks=len(pedges)
     
    distance=number_of_blocks-number_of_cycles
    
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

ans=two_break_distance(p,q)
print(ans)