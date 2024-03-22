weigh = int(input())
height = float(input())
# Tính BMI
BMI = weigh/(height)**2
# In ra kết quả
if BMI<18.5:
    print("Loai 1: Gay")
elif BMI<=22.9:
    print("Loai 2: Binh thuong")
elif BMI<=24.9:
    print("Loai 3: Tien beo phi")
elif BMI<=30:
    print("Loai 4: Beo phi do 1")
else:
    print("Loai 5: Beo phi do 2")
