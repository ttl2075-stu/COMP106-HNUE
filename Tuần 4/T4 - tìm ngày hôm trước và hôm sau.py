dd = int(input())
mm = int(input())
yy = int(input())

#Tinh ngay hom qua
if dd==1: #Neu la ngay 1 dau thang
    if mm==1: ##Neu la thang 1 thi lui ve ngay cuoi cung nam sau
        print(f"31/12/{yy-1}")
    elif mm==3: ##Neu la thang 3 thi lui ve thang 2, kiem tra nam nhuan
        if yy%4==0 and ( yy%100>0 or yy%400==0 ):
            print(f"29/02/{yy}")
        else:
            print(f"28/02/{yy}")
    else:
        if mm-1 in [1,3,5,7,8,10,12]: 
            print(f"31/{mm-1:02d}/{yy}")
        elif mm-1 in [4,6,9,11]:
            print(f"30/{mm-1:02d}/{yy}")
else:
    print(f"{dd-1:02d}/{mm:02d}/{yy}")

#Tinh ngay hom sau
if mm!=2:
    if (dd==31 and mm in [1,3,5,7,8,10,12]) or (dd==30 and mm in [4,6,9,11]): 
        print(f"01/{mm+1:02d}/{yy}")
    else:
        print(f"{dd+1:02d}/{mm:02d}/{yy}")
else:
    if dd==29 and ((yy%4==0) and (yy%100>0 or yy%400==0)):
        print(f"01/03/{yy}")
    elif dd==28 and ((yy%4!=0) and (yy%100==0 or yy%400!=0)):
        print(f"01/03/{yy}")
    else:
        print(f"{dd+1:02d}/{mm:02d}/{yy}")
