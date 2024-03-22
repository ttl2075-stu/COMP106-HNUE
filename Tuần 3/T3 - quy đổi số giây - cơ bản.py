inp = int(input("Nhap vao so giay can tinh: "))
day = inp//86400
hh = (inp-day*86400)//3600
mm = (inp-day*86400-hh*3600)//60
ss = inp - day*86400 - hh*3600 - mm*60
print(inp, "=",day," ngày ",hh," giờ ",mm," phút ",ss," giây")
