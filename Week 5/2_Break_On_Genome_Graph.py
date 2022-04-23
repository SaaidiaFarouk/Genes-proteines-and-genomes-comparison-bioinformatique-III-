def two_breakongenomegraph(edges,coordinates):
    for edge in edges :
        if coordinates[0] in edge and coordinates[1] in edge :
            edges.pop(edges.index(edge))
        elif coordinates[2] in edge and coordinates[3] in edge :
            edges.pop(edges.index(edge))
    
    edges.append([coordinates[0],coordinates[2]])
    edges.append([coordinates[1],coordinates[3]])
    return edges

with open("dataset.txt","r") as f : 
    data=f.readline()
    data1=f.readline()
    data=data.rstrip("\n")
    data=data.lstrip("(")
    data=data.rstrip(")")
    data_edges=data.split("), (")
    edges=list()
    for data_edge in data_edges : 
        edge=data_edge.split(", ")
        edge=[int(edge[i]) for i in range(len(edge))]
        edges.append(edge)
    coordinates=data1.split(", ")
    coordinates=[int(coordinates[i]) for i in range(len(coordinates))]
    print(coordinates)


ans= two_breakongenomegraph(edges,coordinates)
print(ans)

with open("answear.txt","w") as d :
    for a in ans : 
        tpl="("+str(a[0])+", "+str(a[1])+")"
        d.write(tpl)
        if ans.index(a)!=len(ans)-1:
            d.write(", ")
    d.close()
        
