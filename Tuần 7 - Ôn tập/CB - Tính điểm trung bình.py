#Nhập điểm toán văn anh
t=float(input())
v=float(input())
a=float(input())

if t<=10 and v<=10 and a<=10 and t>=0 and v>=0 and a>=0:    #Điều kiện điểm t, v, a trong khoảng từ [0,10]
    avg=(t+v+a)/3               #Tính trung bình
    #So sánh điểm trung bình với điều kiện
    if avg>=8 and avg<=10:
        print("Giỏi")
    elif avg>=6:
        print("Khá")
    elif avg>=4:
        print("Trung bình")
    else:
        print("Yếu")
else:                           #Nhập điểm t, v, a không trong khoảng [0,10]
    print("Lỗi nhập điểm")