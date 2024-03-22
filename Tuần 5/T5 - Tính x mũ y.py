x = float(input())
y = int(input())
kq = x
for i in range(2,y+1):
    kq = kq*x
print(f"{kq:.3f}")