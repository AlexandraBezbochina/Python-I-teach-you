n=3;
def distance(n):
    dist1=0
    dist2=0
    for i in range(1,n+1):
        dist1=dist1+1/i
        dist2=dist2+((-1)**(i+1))/i
    return (print("пройденное расстояние",dist1,"расстрояние до дома",dist2))

distance(1)
distance(2)
distance(3)
distance(4)
distance(5)