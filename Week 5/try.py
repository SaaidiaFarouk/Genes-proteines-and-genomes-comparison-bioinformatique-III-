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
        while cyclecheck(cycle,edges) == False  and len(edges_compo)!=0:
            print(edges_compo)
            strnode=min(edges_compo)
            for edge in edges :
                if strnode in edge :
                    if edge.index(strnode)==1:
                        lst1=[strnode,strnode+1]
                    elif edge.index(strnode)==0:
                        lst1=[strnode+1,strnode]
                    edges_compo.pop(edges_compo.index(min(edges_compo)))
                    edges_compo.pop(edges_compo.index(min(edges_compo)))
            cycle.append(lst1)
        cycles.append(cycle)
    return cycles




q=[[1, -3, -6, -5],[2, -4]]


edges=Colored_Edges(q)
print(edges)
cycles=cycle_finder(edges)
print(len(cycles))
print(cycles)