#Hàm tính đệ quy
def dequy(n):
    kq=0
    for i in range(1,n+1):
        kq+=i
    return kq

#Hàm kiểm tra n của thuộc khoản điều kiện hay không
def kiemtra(n):
    kt=False
    if n>1 and n<10000:
        kt=True
    return kt

#Chương trình chính
n = int(input())
if kiemtra(n):
    print(dequy(n))
else:
    print("N/A")