x1 = float(input())
y1 = float(input())
r1 = float(input())
x2 = float(input())
y2 = float(input())
r2 = float(input())

d = ((x1-x2)**2 + (y1-y2)**2)**0.5

if d==(r1+r2) or d==abs(r1-r2):
    print('TIEPXUC')
elif d>(r1+r2):
    print('NGOAINHAU')
elif (d<(r1+r2) and d==abs(r1-r2)) or (d<=abs(r2-r1)):
    print('TRONGNHAU')
else:
    print('GIAONHAU')
