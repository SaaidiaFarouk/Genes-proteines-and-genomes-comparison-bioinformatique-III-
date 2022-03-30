import numpy as np

def dpchange(money,coins):
    minumcoins=[0]
    for m in range(1,money+1):
        minumcoins.append(np.inf)
        for i in range(len(coins)-1):
            if m >= coins[i]:
                if minumcoins[m-coins[i]]+1 < minumcoins[m]:
                    minumcoins[m] = minumcoins[m-coins[i]]+1
    print(minumcoins[money])
    return minumcoins[money]


with open("dataset.txt","r") as f:
    data=f.readlines()
    for i in range(len(data)):
        data[i]=data[i].replace("\n","")
    money=int(data[0])
    coins=data[1].split(" ")
    for i in range(len(coins)):
        coins[i]=int(coins[i])
dpchange(money,coins)