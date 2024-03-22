import math
x = float(input())
#Gán f1, f2 = 0
f1 = 0
f2 = 0
#Tính f1
if x>0:
    f1 = 3*x + math.sqrt(x)
else:
    f1 = (math.e)**x + 4
#Tính f2    
if (x>-1) and (x<1):
    f2 = (3*x) + 5    
elif x>=1:
    f2 = math.sqrt(x**2 + 1)
elif x<=1:
    f2 = x**2 + 2*x - 1
#In ra kết quả
print(f"{f1:.3f}")
print(f"{f2:.3f}")
