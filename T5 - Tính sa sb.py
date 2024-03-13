n = int(input())
sa = 0
sb = 1
for i in range(1,n+1):
    sa += i**2
    sb += 1/(i*(i+1))
print(f"{sa:.3f}")
print(f"{sb:.3f}")