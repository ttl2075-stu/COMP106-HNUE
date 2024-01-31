a = int(input())
b = int(input())
c = int(input())
d = int(input())
#Tim min
minn=a
if b<minn:
    minn=b
if c<minn:
    minn=c
if d<minn:
    minn=d
#Tim max
maxx=a
if b>maxx:
    maxx=b
if c>maxx:
    maxx=c
if d>maxx:
    maxx=d
#In ra ket qua
print(minn)
print(maxx)