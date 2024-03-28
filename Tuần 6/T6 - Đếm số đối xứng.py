def kiemtra(n,m):
    if n>100 and m<100000 and n<m:
        return True
    else:
        return False

def doixung(a):
    lenn=len(str(a))        #Đếm số ký tự trong chuỗi a len(chuỗi str) str(num)
    kt_doixung=True
    for i in range(1,(lenn//2)+1,1):    #For từ 1 đến a/2
        sodau = int(str(a)[i-1])        #str(a)[i-1] lấy giá trị ở vị trí đầu tiên (giá trị đầu tiên là 0)
        socuoi = int(str(a)[lenn-i])    #str(a)[lenn-i] lấy giá trị ở vị trí cuối cùng (vì start từ 0 nên vị trí cuối là độ dài - 1)
        if sodau != socuoi:
            kt_doixung = False
            break
    return kt_doixung

#Chương trình chính
n = int(input())
m = int(input())
if kiemtra(n,m):    #Kiểm tra n và m có thuộc khoảng đề bài hay không?
    dem=0
    for j in range(n,m+1):
        if doixung(j):
            dem+=1
    print(dem)
else:
    print("N/A")