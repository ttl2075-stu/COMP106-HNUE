a = int(input())
b = int(input())
c = int(input())
d = int(input())
# Đặt max giả sử
max1 = a
max2 = a
# Tìm max và max thứ 2
if b>max1:
    max2=max1
    max1=b
if c>max1:
    max2=max1
    max1=c
if d>max1:
    max2=max1
    max1=d
#In ra kết quả
print(max2)
