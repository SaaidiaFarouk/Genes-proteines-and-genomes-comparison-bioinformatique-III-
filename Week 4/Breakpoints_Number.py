
def breakpoints_number(p):
    number=0
    if p[0]!=1:
        number+=1
    if p[len(p)-1]!=len(p):
        number+=1
    i=0
    while i!=len(p)-1:
        if p[i]!=p[i+1]-1 :
            number+=1
            i+=1
        else:
            i+=1
    
    
    return number
        



with open("dataset.txt","r") as f : 
    data=f.readline()
    data=data.replace("\n","")
    p=data.split(" ")
    for i in range(len(p)):
        p[i]=int(p[i])
print(breakpoints_number(p))