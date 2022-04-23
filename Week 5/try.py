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
            for edge in edges :
                if strnode in edge :
                    if edge.index(strnode)==1:
                        lst1=[strnode,nextnode]
                    elif edge.index(strnode)==0:
                        lst1=[nextnode,strnode]
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
        print(finalnode)
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
        print(cycle) 
        print(pcomp)
        print(qcomp)
        cycles.append(cycle)    

    return cycles

q=[[1, -3, -6, -5],[2, -4]]
p=[[1, 2, 3, 4, 5, 6]]

pedges=Colored_Edges(p)
qedges=Colored_Edges(q)
print(pedges)
print(qedges)

totaledges=pedges+qedges


# pcycles=cycle_finder(pedges)
# qcycles=cycle_finder(qedges)

# print(pcycles)
# print(qcycles)

print(colored_cycle(pedges,qedges))