weight = 60
height = 1.7

imt = weight / (height * height)

print(imt)

if imt < 19:
    print("У вас недовес")
elif imt > 25:
    print("У вас перевес")
else:
    print("Ваш вес в норме")

def get_imt(weight, height):
    imt = weight / (height * height)

    if imt < 19:
        print("У вас недовес")
    elif imt > 25:
        print("У вас перевес")
    else:
        print("Ваш вес в норме")

get_imt(140,1.2)

get_imt(90,1.7)

get_imt(95,1.6
