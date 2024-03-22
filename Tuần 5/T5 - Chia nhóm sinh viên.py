a = int(input())
b = int(input())
c = int(input())
d = int(input())

m = max(a,b,c,d)
for i in range(m,(a*b*c*d)+1,m):
    if (i%a==0 and i%b==0 and i%c==0 and i%d==0):
        print(i)
        break