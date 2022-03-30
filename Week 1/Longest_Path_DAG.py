def predecessors(node,graph):
    predecissors=list()
    for othernode in graph:
        if othernode[1] == node:
            predecissors.append(othernode)
    return predecissors

def graphcomposition(graph):
    composition=list()
    for node in graph :
        composition.append(node[0])
        composition.append(node[1])
    composition.sort()
    composition=list(dict.fromkeys(composition))
    return composition



def longestpath(graph,start,sink):
    lst=[]
    composition=graphcomposition(graph)
    s=dict()
    for node in composition :
        s[node]= float('-inf')
    s[start]=0
    for i in range(1,len(composition)) :
        node=composition[i]
        predecissors=predecessors(node,graph)
        maxi=0
        for pred in predecissors:
            m=s[pred[0]]+float(pred[2])
            if m >= maxi :
                maxi=m
        for pred in predecissors:
            m=s[pred[0]]+float(pred[2])
            if m == maxi :
                lst.append(pred)
        s[node]=maxi
    paths=list()

    for edge in lst :
        if edge[1] == sink :
            paths.append([edge])
    strpaths=list()
    for path in paths : 
        while path[len(path)-1][0] != start :
            finaledge=path[len(path)-1]
            for edge in lst :
                if edge[1]==finaledge[0] and s[edge[1]] + finaledge[2] == s[finaledge[1]]:
                    path.append(edge)
        pathstr=""
        path.reverse()
        for edge in path :
            pathstr=pathstr+str(edge[0])+" "
        pathstr+=str(sink)
        strpaths.append(pathstr)
    
    return(s[sink],strpaths)
        





with open("dataset.txt","r") as f : 
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    se=data[0].split(" ")
    s=int(se[0])
    e=int(se[1])
    graph=list()
    for i in range(1,len(data)):
        edge=data[i].split(" ")
        graph.append(edge)
    for edge in graph:
        for i in range(len(edge)):
            edge[i]=int(edge[i])

stri=''
ans=longestpath(graph,s,e)
print(ans)
with open ("answear.txt","w") as d :
    d.write(str(ans[0]))
    for an in ans[1]:
        stri=stri+str(an)+" -> "
    stro =stri[:len(stri)-4]
    d.write("\n")
    d.write(stro)

