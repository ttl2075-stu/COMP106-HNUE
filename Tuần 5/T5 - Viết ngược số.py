n = int(input())
nn = 0
while n!=0:
    nn = (nn*10)+(n%10)
    n = n//10
print(nn)