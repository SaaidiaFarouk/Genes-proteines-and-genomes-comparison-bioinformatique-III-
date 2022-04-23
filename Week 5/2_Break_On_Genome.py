def two_breakongenomegraph(edges,coordinates):
    for edge in edges :
        if coordinates[0] in edge and coordinates[1] in edge :
            edges.pop(edges.index(edge))
        elif coordinates[2] in edge and coordinates[3] in edge :
            edges.pop(edges.index(edge))
    
    edges.append((coordinates[0],coordinates[2]))
    edges.append((coordinates[1],coordinates[3]))
    return edges

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

def Cycle_To_Chromosome(cycle):
    chromosome=list()
    for i in range(int(len(cycle)/2)):
        chromosome.append(9)
    for j in range(0,int(len(cycle)/2)):
        if cycle[2*j] < cycle[2*j+1]:
            chromosome[j]=int(cycle[(2*j+1)]/2)
        else : 
            chromosome[j]=int(-cycle[2*j]/2)
    
    return chromosome

def compositions(nodes):
    composition=list()
    for node in nodes : 
        for n in node : 
            composition.append(n)
    return composition

def cyclecheck(cycle,edges):
    if len(cycle)==0:
        return False
    val = True
    strnode=cycle[0][0]
    endnode=cycle[len(cycle)-1][1]
    for edge in edges :
        if strnode in edge :
            if endnode not in edge :
                val=False
    return val 

def cycle_finder(edges):
    cycles=list()
    edges_compo=compositions(edges)
    while len(edges_compo)!=0:
        cycle=list()
        strnode=min(edges_compo)
        lst1=[strnode,strnode+1]
        nextnode=strnode+1
        for edge in edges :
            if strnode in edge :
                if edge.index(strnode)==0:
                    lst1.reverse()
                    strnode=strnode+1
                    nextnode=strnode-1
        cycle.append(lst1)
        edges_compo.pop(edges_compo.index(lst1[0]))
        edges_compo.pop(edges_compo.index(lst1[1]))
        for edge in edges :
            if nextnode in edge :
                m=edge.index(nextnode)
                n=1-m
                strnode=edge[n]
                break

        while cyclecheck(cycle,edges) == False  :
            if strnode%2==0:
                nextnode=strnode-1
            else:
                nextnode=strnode+1
            lst1=[strnode,nextnode]
            edges_compo.pop(edges_compo.index(strnode))
            edges_compo.pop(edges_compo.index(nextnode))
            for edge in edges : 
                if nextnode in edge :
                    m=edge.index(nextnode)
                    n=1-m
                    strnode=edge[n]
            
            cycle.append(lst1)
        cycles.append(cycle)

    return cycles

def Graph_To_Genome(edges):
    p=list()
    cycles=cycle_finder(edges)
    for cycle in cycles :
        nodes = compositions(cycle)
        chromosome =  Cycle_To_Chromosome(nodes)
        # x=chromosome[len(chromosome)-1]
        # chromosome.pop()
        # chromosome.insert(0,x)
        p.append(chromosome)

    return p 



def two_breakongenome(chromosomes,coordinates):
    colored_edges=Colored_Edges(chromosomes)
    colored_edges=two_breakongenomegraph(colored_edges,coordinates)
    p=Graph_To_Genome(colored_edges)
    return p

with open ("dataset.txt","r") as f : 
    data = f.readline()
    data1=f.readline()
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
    coordinates=data1.split(", ")
    coordinates=[int(coordinates[i]) for i in range(len(coordinates))]
ans= two_breakongenome(chromosomes,coordinates)
for a in ans :
    print(a)
with open("answear.txt","w") as d : 
    anstor=""
    for a in ans :
        anstr="("
        for o in a : 
            if o > 0 :
                anstr+="+"
            anstr+=str(o)
            if a.index(o)!=len(a)-1:
                anstr+=" "
        anstr+=")"
        anstor+=anstr
    d.write(anstor)
    d.close()
        