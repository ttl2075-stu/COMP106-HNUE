n = int(input())
shc = 0
for i in range(1,(n//2)+1):
    if n%i==0:
        shc=shc + i 
if n == shc:
    print("Co")
else:
    print("Khong")