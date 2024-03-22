#Hàm kiểm tra có phải là số nhị phân hay không
def kiemtra(a):
    kt=True                     #Đặt giá trị kiểm tra là True
    while a>0 and kt==True:     #Vòng lặp while đến khi số a>0 (0001, nếu chỉ là số 0 thì cũng là số nhị phân) và chạy khi biến kt=True
        if a%10 in [0,1]:       #Lấy chữ số hàng đơn vị kiểm tra có phải là 0 hoặc 1 hay không
            a = a//10           #Nếu đúng thì a//10 (bỏ chữ số hàng đơn vị)
        else:
            kt=False            #Nếu sai thì đặt biến kt=False để dừng vòng lặp
    return kt                   #Trả kết quả có phải là số nhị phân hay không (True/False)

#Hàm chuyển số nhị phân thành thập phân
def chuyendoi(c):
    return int(str(c),2)
    #Chú thích:
    #int là hàm chuyển đổi một chuỗi string theo 1 định dạng nào đó về type int (số nguyên)
    #int(chuỗi ký tự, định dạng chuỗi)
    #str là hàm đổi số thành dạng string

#Chương trình chính
x = int(input())
y = int(input())

if kiemtra(x)==True and kiemtra(y)==True:   #Kiểm tra x và y có phải là số nhị phân hay không?
    tong = chuyendoi(x) + chuyendoi(y)      #Nếu đúng thì tính chuyển đổi x, y thành số thập phân và tính tổng
    print(tong)                             #In kết quả
else:
    print("N/A")                            #Nếu x, y không phải số nhị phân thì in ra "N/A"