n=int(input())  #Nhập số n
s=1             #Đặt s=1 (bỏ qua giá trị i là 1)          
gt=1            #Giai thừa là 1
for i in range(2,n+1,1):    #Chạy từ 2 đến n
    gt*=i                   #Tính giai thừa (phần mẫu số)
    s+=1/(gt)               #Tính s
print(f"{s:.5f}")           #In ra kết quả theo yc