def scoringdnas(dnas):
    v=dnas[0]
    w=dnas[1]
    u=dnas[2]
    scorex=list()
    for i in v : 
        scorex.append([])
        for j in w : 
            scorex[i].append([])  
            for k in u : 
                scorex[i][j].append(0)


with open("dataset.txt","r") as f : 
    data = f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    dnas=list()
    for line in data : 
        dnas.append(line)
print(dnas)