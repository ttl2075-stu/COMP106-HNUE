m = int(input())
y = int(input())
#Kiem tra xem co phai la nam nhuan hay khong
nhuan = 0
if y%4==0 or y%100==0 and y%400!=0:
    nhuan = 1
#Kiem tra so ngay cua thang va in ra ket qua
if m==2:
    if nhuan == 1:
        print("29")
    else:
        print("28")
elif m in [1,3,5,7,8,10,12]:
    print("31")
else:
    print("30")