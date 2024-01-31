import math
a = int(input())
b = int(input())
c = int(input())
# Nếu a = 0, tính phương trình bậc nhất
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh co vo so nghiem!")
        else:
            print("Phuong trinh vo nghiem!")
    else:
        x = -c/b
        print("Phuong trinh co mot nghiem: x =", f"{x:.3f}")
# Với a!=0 thì tính nghiệm phương trình bậc 2
else:
    denta = b**2 - 4*a*c
    if denta < 0:
        print("Phuong trinh vo nghiem!")
    elif denta == 0:
        print("Phuong trinh co nghiem kep: x1 = x2 =",f"{-b/(2*a):.3f}")
    else:
        x2 = (-b - math.sqrt(denta))/(2*a)
        x1 = (-b + math.sqrt(denta))/(2*a)
        print("Phuong trinh co 2 nghiem: x1 =", f"{x1:.3f}", "va x2 =", f"{x2:.3f}")
