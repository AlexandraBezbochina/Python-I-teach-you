str="жыли"
print(str)
print(len(str))
print(str[0])
print(len(str))
for i in range(0,len(str)-1):
    if str[i]=="Ж" or str[i]=="ж" or str[i]=="Ш" or str[i]=="ш":
        if str[i+1]=="Ы" or str[i+1]=="ы":
            a1="Неправильно написано жи/ши"
            print(a1)
            break
    elif str[i]=="Ч" or str[i]=="ч" or str[i]=="Щ" or str[i]=="щ":
        if str[i+1]=="Я" or str[i+1]=="я":
            a2 = "Неправильно написано ча/ща"
            print(a2)
            break