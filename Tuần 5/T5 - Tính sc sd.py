import math
n = int(input())                #Nhập vào n

#Tính sc
sc = 0
for i in range(1, n+1):
    sc = math.sqrt(3 + sc)

#Tính sd
sd = 1                          #Đặt sd = 1 để for chạy từ 2
temp_sd = 1                     #Đặt phép nhân tạm thời là 1 để bắt đầu for chạy từ 2
for i in range(2,n+1):          #For từ 2 đến n+1
    temp_sd = temp_sd*i         #Nhân vào temp giá trị i khi đó temp sẽ trở thành giá trị phép tính tại n
    sd += temp_sd               #Cộng vào giá trị sd giá trị tại n=i

#Thông báo kết quả
print(f"{sc:.3f}")
print(f"{sd:.3f}")