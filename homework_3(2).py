s1=[1,2,3,4]
s2=[5,6,7,8]

a0=[]
def fun2(s1,s2):
    for i in range(0,len(s1)):
        a1=s1[i]+s2[i]
        k=list(str(a1))
        if len(k)>1:
            k=list(map(int, k))
            for i in range(0,len(k)):
                a0.append(k[i])
        else:
            a0.append(a1)
    return(print(a0))

fun2(s1,s2)



s3=[1,2,3,4,5]
s4=[5,6,7]
a0=[]
if len(s3)>len(s4):
    while len(s3)>len(s4):
        s4.insert(0,0)
elif len(s4)<len(s3):
    while len(s3)<len(s4):
        s3.insert(0,0)

fun2(s3,s4)