n = int(input())

kt="Co"                 #Đặt biến kiểm tra là có
if n<2:                 #Số nguyên tố là các số lớn hơn 1, các số nhỏ hơn 1 in kết quả là không
    print("Khong")
else:                   #Nếu n>2 thì kiểm tra
    for i in range(2,(n//2)+1):     #Vùng kiểm tra từ 2 cho đến n/2
        if n%i==0:                  #Nếu giá trị n chia hết cho i thì kết thúc và in ra là Không
            kt="Khong"
            break
    print(kt)