#Hàm tìm ước chung lớn nhất
def ucln(a,b):
    while (a*b !=0):        #Áp dụng thuật toán tìm ước chung bằng phép tính chia lấy dư cho đến khi 1 trong 2 số = 0
        if a>b:             #Nếu a>b thì 
            a=a%b
        else:
            b=b%a
    uc=a+b                  #Trả kết quả ước chung là a+b (vì 1 trong 2 số = 0)
    return uc

#Chương trình chính    
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())

uc=ucln(x1,x2)              #Tính ước chung của cặp số đầu
for i in [x3,x4,x5]:        #Sử dụng vòng lặp for để tìm ước chung của lần lượt các cặp số
    uc = ucln(uc,i)
print(uc)