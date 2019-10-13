import random
class Voin:
    name=""
    health=""
    damage=""
    security=""
    def __init__(self,name):
        self.name=name
        self.army1=[]
        self.army2=[]

    def h(self):
        return self.health

    def d(self):
        return self.damage

    def uron(self,damage):
        a=self.health-damage
        if a >0:
            print (self.name + "получил" + str(damage)+"урона." + "Осталость"+str(a)+"здоровья")
        else:
            print (self.name + "получил" + str(damage)+"урона и погиб")


    def uron1(self,damage):
        a=self.health-damage
        return a


class VoinWithhield(Voin):
    def s(self):
        return self.security
    def uron(self,damage):
        a=self.health+self.security-damage
        if a >0:
            print (self.name + "получил" + str(damage)+"урона." + "Остальность"+str(a)+"здоровья")
        else:
            print (self.name + "получил" + str(damage)+"урона и погиб")


class VoinExpert(Voin):
    def d(self):
        return self.damage

#Задача 1. Создаем воинов, выводи значения здоровья, атаки и защиты
#создаем воина первого класса и смотрим его параметры
voin1=Voin("vova")
voin1.health=int(random.uniform(100,150))
voin1.damage=int(random.uniform(20,30))
print(voin1.health)
print (voin1.h())
print(voin1.damage)
print(voin1.d())
#создаем воина второго класса и смотрим его параметры
voin2=VoinWithhield("petya")
voin2.health=int(random.uniform(100,150))
voin2.damage=int(random.uniform(20,30))
voin2.security=int(random.uniform(5,10))
print(voin2.health)
print (voin2.h())
print(voin2.damage)
print(voin2.d())
print(voin2.security)
print(voin2.s())
#создаем воина третьего класса и смотрим его параметры
voin3=VoinExpert("vitya")
voin3.health=int(random.uniform(100,150))
voin3.damage=int(random.uniform(30,40))
print(voin3.health)
print(voin3.h())
print(voin3.damage)
print(voin3.d())
# функции, которые определеяют урон и показывают, сколько осталось у воина после атаки( дальше используется другая функция, результатом которой будет не print, а return)
voin1.uron(voin3.damage)
voin2.uron(voin3.damage)
voin1.uron(voin2.damage)

# Задача 2. Бой между первым и вторым классом (первый класс нападает первым)
while voin2.health>0 and voin1.health>0:
    voin2.health=voin2.health-voin1.damage
    if voin2.health>0:
        voin1.health=voin1.health-voin2.damage
if voin1.health<0:
    print("первый умер")
if voin2.health<0:
    print("второй умер")
print("здоровье первого воина"+str(voin1.health))
print("здоровье второго воина"+str(voin2.health))

# Бой между первым и третьим классом (первый класс нападает первым)
while voin3.health>0 and voin1.health>0:
    voin3.health=voin3.health-voin1.damage
    if voin3.health>0:
        voin1.health=voin1.health-voin3.damage
if voin1.health<0:
    print("первый умер")
if voin3.health<0:
    print("третий умер")
print("здоровье первого воина"+str(voin1.health))
print("здоровье третьего воина"+str(voin3.health))


# Бой между вторым и третьим классом (второй класс нападает первым)
while voin3.health>0 and voin2.health>0:
    voin3.health=voin3.health-voin2.damage
    if voin3.health>0:
        voin2.health=voin2.health-voin3.damage
if voin2.health<0:
    print("второй умер")
if voin3.health<0:
    print("третий умер")
print("здоровье второго воина"+str(voin2.health))
print("здоровье третьего воина"+str(voin3.health))


# создаем еще воинов для первой армии
voin11=Voin("vova1")
voin12=Voin("vova2")
voin13=Voin("vova3")
voin21=VoinWithhield("petya1")
voin22=VoinWithhield("petya2")
voin23=VoinWithhield("petya3")
voin31=VoinExpert("vitya1")
voin32=VoinExpert("vitya1")
voin33=VoinExpert("vitya1")

# сделать армию с помощью ассоциации не получалось очень долго, поэтому так
army1=[voin1,voin11,voin12,voin13,voin2,voin21,voin22,voin23,voin3,voin31,voin32,voin33]
print(army1)

# создаем еще воинов для второй армии
voin111=Voin("vova1")
voin112=Voin("vova2")
voin113=Voin("vova3")
voin221=VoinWithhield("petya1")
voin222=VoinWithhield("petya2")
voin223=VoinWithhield("petya3")
voin331=VoinExpert("vitya1")
voin332=VoinExpert("vitya1")
voin333=VoinExpert("vitya1")

army2=[voin1,voin111,voin112,voin113,voin2,voin221,voin222,voin223,voin3,voin331,voin332,voin333]

#бой двух армий
i = 1
while len(army1) > 0 and len(army2) > 0:
    n1 = ranom.randint(0, len(army1) - 1)
    n2 = random.randint(0, len(army2) - 1)
    if i % 2 == 1:
        if type(army1[n1]) == VoinExpert:
            army2[n2].uron1(army1[n1].d())

        else:
            army2[n2].uron1(army1[n1].d())

        if army2[n2].health < 0:
            del army2[n2]
    else:
        if type(army2[n2]) == VoinExpert:
            army1[n1].d(army2[n2].d())

        else:
            army1[n1].uron1(army2[n2].d())

        if army1[n1].health < 0:
            del army1[n1]
    i = i + 1
if len(army1) == 0:
    print('вторая армия победила')
else:
    print('вторая армия победила')
