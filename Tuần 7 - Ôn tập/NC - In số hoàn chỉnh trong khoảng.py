#Hàm kiểm tra giá trị nhập vào có thuộc trong khoảng điều kiện hay không
def kiemtra(n):
    if n>1 and n<100000:
        return True
    else:
        return False
#Hàm kiểm tra số đưa vào có phải là số hoàn chỉnh hay không, nếu có thì in ra màn hình
def shc(a):
    tempp=1                         #Đặt giá trị tổng các ước của số đó (tempp) = 1 vì 1 luôn là ước của tất cả các số và for sẽ không bắt dầu từ 1
    for i in range(2,(a//2)+1,1):   #For từ 2 cho đến a/2 (vì một số không bao giờ chia hết cho (chính nó)/2)
        if a%i==0:                  #Nếu a chia hết cho i
            tempp+=i                #thì cộng i vào tổng ước
    if tempp==a:                    #Nếu tổng các ước bằng chính số a 
        print(a, end=" ")           #thì a là số hoàn chỉnh và in ra màn hình (end=' ' là để không xuống dòng và cách ra 1 dấu cách)

#Chương trình chính
n=int(input())
if kiemtra(n):                  #Kiểm tra n có thuộc khoảng đề bài yêu cầu hay không?
    for j in range(2,n+1,1):    #nếu có thì chạy vòng lặp j từ 2 cho đến n (không chạy từ 1 vì 1 là trường hợp đặc biệt)
        shc(j)                  #sử dụng hàm số hoàn chỉnh đã cài đặt
else:
    print("N/A")                #nếu n không thuộc khoảng đề bài yêu cầu thì in ra "N/A"