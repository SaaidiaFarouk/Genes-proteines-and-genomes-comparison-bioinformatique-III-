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
        while cyclecheck(cycle,edges) == False  :
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

def Graph_To_Genome(edges):
    p=list()
    cycles=cycle_finder(edges)
    for cycle in cycles :
        nodes = compositions(cycle)
        chromosome =  Cycle_To_Chromosome(nodes)
        p.append(chromosome)

    return p 


with open("dataset.txt","r") as f : 
    data=f.readline()
    data=data.rstrip("\n")
    data=data.lstrip("(")
    data=data.rstrip(")")
    data_edges=data.split("), (")
    edges=list()
    for data_edge in data_edges : 
        edge=data_edge.split(", ")
        edge=[int(edge[i]) for i in range(len(edge))]
        edges.append(edge)
  
ans=Graph_To_Genome(edges)

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
        
            
