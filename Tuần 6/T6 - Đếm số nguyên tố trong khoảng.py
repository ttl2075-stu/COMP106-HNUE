#Hàm kiểm tra điều kiện khoảng của đề bài
def kt_khoang(a,b):
    if a>500 and b<100000 and a<b:
        return True
    else:
        return False

#hàm kiểm tra số đưa vào có phải số nguyên tố hay không (Trả giá trị True/False)
def kt_snt(a):
    ktsnt=True
    for i in range(2,int(a**0.5)+2,1):  #Sử dụng thuật toán một số nguyên tố không bao giờ chia hết cho một số căn bậc 2 của nó
        if a%i==0:                      #Nếu a chia hết cho số i thì ktsnt = false và dừng vòng lặp (break)
            ktsnt=False
            break
    return ktsnt

m = int(input())
n = int(input())
if kt_khoang(m,n):
    dem=0
    for j in range(m,n+1,1):
        if kt_snt(j)==True:
            dem+=1
    print(dem)
else:
    print("N/A")