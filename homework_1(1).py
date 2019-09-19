print("homework from Bezbochina")
print("парковка")
def parkovka(day,hour):
    if day%2==0:
        print("четный день")
        if hour>21:
            print ("на правой стороне нельзя, паркуйся на левой")
        elif 19<hour<21:
            print("паркуйся, где хочешь")
        else:
            print("на левой стороне нельзя, паркуйся на правой")
    elif day%2>0:
        print("нечетный день")
        if hour > 21:
            print("на левой стороне нельзя, паркуйся на правой")
        elif 19 < hour < 21:
            print("паркуйся, где хочешь")
        else:
            print("на правой стороне нельзя, паркуйся на левой")

parkovka(3,17.45)
day=int(input("введите день"))
hour=float(input("введите время в формате час.минуты "))
parkovka(day,hour)
парковка (4,15.20)
