inp = int(input())
fee = 150000
if inp>200:
    fee += 600*50 + 400*150 + 200*(inp-200)
elif inp>50:
    fee += 600*50 + 400*(inp-50)
else:
    fee += 600 * inp
print(fee)
