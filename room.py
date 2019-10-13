
# coding: utf-8

# In[142]:


class Room():
    dlina=""
    shirota=""
    high=""
    def __init__(self,d,sh,h):
        self.dlina=d
        self.shirota=sh
        self.high=h
    def square(self):
        return self.dlina*self.shirota
    def oboi(self,window,door):
        if door.secret==1:
            a=4*self.square()-window.square2()
            print ("площадь обоев"+str(a))
        elif door.secret==0:
            a=4*self.square()-window.square2()-door.square1()
            print ("площадь обоев" + str(a))
    def koefficient(self,window,door):
        k=window.square2()/self.square()
        return k
    def true_room(self,window,door):
        if (self.dlina + self.shirota)*2>window.shirota2+door.shirota1:
            if window.dlina2+window.high1<self.high:
                print ("такая комната существует")
                print("периметр комнаты" +str((self.dlina + self.shirota)*2), "необходимое пространствол для окна и двери" + str(window.shirota2+door.shirota1)) 
            else:
                print("комната не существует, т.к. недостаточно высоты потолка")
        else :
            print("такая комната не существует")
            print("периметр комнаты" +str((self.dlina + self.shirota)*2), "необходимое пространствол для окна и двери  " + str(window.shirota2+door.shirota1)  )


# In[143]:


class Door():
    dlina1=""
    shirota1=""
    secret=""
    def __init__(self,d,sh,s):
        self.dlina1=d
        self.shirota1=sh
        self.secret=s
    def square1(self):
        return self.dlina1*self.shirota1


# In[144]:


class Window():
    dlina2=""
    shirota2=""
    high1=""
    def __init__(self,d,sh,h):
        self.dlina2=d
        self.shirota2=sh
        self.high1=h
    def square2(self):
        return self.dlina2*self.shirota2


# In[145]:


room=Room(15,15,15)
door=Door(1,1,1)#1 в третьем аргументе означает, что дверь скрытая
window=Window(0.5,0.5,0.2)


# In[146]:


room.true_room(window,door)


# In[147]:


room.oboi(window,door)


# In[148]:


room.koefficient(window,door)

