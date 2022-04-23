
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

def non_trivial_cycles(cycles):
    non_trivial=list()
    for cycle in cycles : 
        if len(cycle)!=2:
            non_trivial.append(cycle)
    return non_trivial

def two_breakongenomegraph(edges,coordinates):
    for edge in edges :
        if coordinates[0] in edge and coordinates[1] in edge :
            frst_to_pop=edge
            
        if coordinates[2] in edge and coordinates[3] in edge :
            second_to_pop=edge
            
    edges.pop(edges.index(frst_to_pop))
    edges.pop(edges.index(second_to_pop))
    edges.append((coordinates[0],coordinates[2]))
    edges.append((coordinates[1],coordinates[3]))
    return edges

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
    print("lol",colored_edges)
    p=Graph_To_Genome(colored_edges)
    return p

def shortest_rearangement(p,q):
    ps=list()
    ps.append(p)
    red_edges=Colored_Edges(p)
    blue_edges=Colored_Edges(q)
    cycles=colored_cycle(red_edges,blue_edges)
    nontrivial_cycles=non_trivial_cycles(cycles)
    while len(nontrivial_cycles)!=0:
        nontrivial_cycle=nontrivial_cycles[0]
        arbitrary_starting_blue_edge=nontrivial_cycle[0]
        next_blue_edge=nontrivial_cycle[len(nontrivial_cycle)-2]
        coordinates=[arbitrary_starting_blue_edge[0],arbitrary_starting_blue_edge[1],next_blue_edge[1],next_blue_edge[0]]
        red_edges=two_breakongenomegraph(red_edges,coordinates)
        cycles=colored_cycle(red_edges,blue_edges)
        p=two_breakongenome(p,coordinates)
        ps.append(p)
        red_edges=Colored_Edges(p)
        cycles=colored_cycle(red_edges,blue_edges)
        nontrivial_cycles=non_trivial_cycles(cycles)
        
    return ps

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

p=genomes[0]
q=genomes[1]
ans=shortest_rearangement(p,q)
for a in ans : 
    print(a)
with open("answear.txt","w") as d : 
    
    for x in ans :
        anstor=""
        for a in x :
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
        d.write("\n")
    d.close()