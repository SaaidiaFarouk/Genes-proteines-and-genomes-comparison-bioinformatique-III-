a=[-3, 4, 1, 5, -2]
# print("here",a[2:3])


def checksort(k,p):
    val=True
    for i in range(0,k):
        if abs(p[i])!=i+1:
            val=False
    return val

print(checksort(1,a))