#Hàm tính sinx
def sinx(x,m):
    kq=0                        #Đặt kết quả của phép tính là kq=0
    for i in range(1,m+1,1):    #For từ 1 đến m
        #Tính giai thừa
        giaithua=1                  #Đặt lại giá trị giai thừa ban đầu = 1
        for k in range(1,(2*i),1):  #Chạy từ 1 đến i để tính giai thừa
            giaithua = giaithua*k   
        kq+=( (-1)**(i-1) )*((x**((2*i)-1))/giaithua) #Tính kq theo biểu thức sin
    return kq   #Trả kết quả của hàm 

#Chương trình chính   
x=float(input())
m=int(input())

print(f"{sinx(x,m):.3f}")