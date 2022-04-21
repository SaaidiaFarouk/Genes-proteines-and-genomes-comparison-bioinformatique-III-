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


with open ("dataset.txt","r") as f : 
    data=f.readline()
    data=data.replace("\n","")
    data=data.replace("(","")
    data=data.replace(")","")
    cycle=data.split(" ")
    cycle=[int(cycle[i]) for i in range(len(cycle))]

ans=Cycle_To_Chromosome(cycle)
print(ans)
with open("answear.txt","w") as d : 
    d.write("(")
    anstr=""
    for a in ans : 
        ao=str(a)
        if a > 0 :
            ao="+"+ao
        anstr+=ao
        if ans.index(a)!=len(ans)-1:
            anstr+=" "
    d.write(anstr)
    d.write(")")
    d.close()