#Hàm
def calcsxn(x,n):
    ans=0
    for i in range(1,n+1):
        ans+=x**i
    return ans

#Chương trình chính
x=float(input())
n=int(input())
print(f"{calcsxn(x,n):.3f}")