def greeting(name):
    print("xin chao " + name)
greeting("Phuong")

def introduce(name, cafe):
    print(name + " thich uong " + cafe)
introduce("Vinh", "tra vai")
introduce("Phuong", "bac xiu")

def area_rectangle(long, short):
    return long*short
a = area_rectangle(4,6)
b = area_rectangle(3,5)
sum = a + b
print("dien tich hinh chu nhat la: " + str(sum))

def chi_em(Phuong, Dat):
    if Phuong > Dat:
        return Phuong, Dat
    else:
        print("khong co ket qua.")
chi_em(22, 17)
 