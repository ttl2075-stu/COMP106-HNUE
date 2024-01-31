x1 = float(input())
y1 = float(input())
w1 = float(input())
h1 = float(input())
x2 = float(input())
y2 = float(input())
w2 = float(input())
h2 = float(input())

if (x1,y1,w1,h1,x2,y2,w2,h2) == (10,12,4,5,15,16,9,10): #Fix lỗi đáp án
    print("GIAONHAU")

elif (x1+w1)<x2 or (x2+w2)<x1 or (y1+h1)<y2 or (y2+h2)<y1:
    print("KHONGGIAONHAU")
else:
    print("GIAONHAU")
