## 
n = int(input())
sum = 0
flag = 1
for i in range(1,n+1):
    sum += flag * ( 1 / i)
    flag *= -1 
print("{:.4f}".format(sum))    