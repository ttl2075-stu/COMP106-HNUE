#Tính F(x,y)
def calcfxy(x,y):
    print(f"{x**2+x*y+y**2-2*x-y:.2f}")

#Tính F(x,y,z)
def calcfxyz(x,y,z):
    if y==0:
        print("N/A")
    else:    
        print(f"{x*y*z+(x/y**z):.2f}")

#Chương trình chính
x=float(input())
y=float(input())
z=float(input())
calcfxy(x,y)
calcfxyz(x,y,z)