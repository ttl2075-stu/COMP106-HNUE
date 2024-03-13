n = int(input())

#Kiểm tra dãy n có bao nhiêu số
i=0
nn = n
while nn>0:
    i+=1
    nn=nn//10

#Tính tổng luỹ thừa của các số
s=0
nn=n
while nn>0:
    s+= (nn%10)**i
    nn = nn//10

#Kiểm tra và in ra kết quả
if s==n:
    print("Co")
else:
    print("Khong")