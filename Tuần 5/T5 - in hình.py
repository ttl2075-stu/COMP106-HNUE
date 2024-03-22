n = int(input())
#In hình tam giác
for i in range(1, n + 1):
    print(" " * (n - i + 1), end="")
    print("*" * (2 * i - 1))
print("")

# In hình vuông
for i in range(n):
    print("*" * 5)
print(" ")

# In hình hình tháp
for i in range(1,n+1):
    print("*" * ((i*2)-1))
for i in range(n-1,0,-1):
    print("*" * ((i*2)-1))