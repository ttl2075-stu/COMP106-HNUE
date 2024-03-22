import math
#Tạo hàm tính fx
def calcfx(x):
    if x>=-1 and x<=1:
        print(f"{-2*(x-3):.2f}")
    elif x>1:
        print(f"{math.sqrt(x**2-1):.2f}")
    else:
        print("0.00")
#Tạo hàm tính gx
def calcgx(x):
    if x>2:
        print(f"{x**2 + 1:.2f}")
    elif x<-2:
        print(f"{6-5*x:.2f}")
    else:
        print(f"{2*x-1:.2f}")

#Chương trình chính
x = float(input())
calcfx(x)
calcgx(x)
