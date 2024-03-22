sd = int(input())
money = 0
if sd>400:
    money = 909000 + (sd-400)*2927
elif sd>300:
    money = 625600 + (sd-300)*2834
elif sd>200:
    money = 372000 + (sd-200)*2536
elif sd>100:
    money = 170600 + (sd-100)*2014
elif sd>50:
    money = 83900 + (sd-50)*1734
else:
    money = sd*1678
print(money)
