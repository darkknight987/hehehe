import numpy as np

price = []
cuts = int(input("Enter number of cuts:"))
print("Enter Price of Cuts:")
for i in range(0, cuts):
    num = int(input())
    price.append(num)
print(price)

arr = np.zeros((len(price),cuts+1))

for i in range(0,len(price)):
    for j in range(0,cuts+1):
        if j == 0:
            continue
        elif i == 0:
            arr[i,j] = price[i] + arr[i, j-i-1]
        elif (j-i-1) < 0:
            arr[i,j] = arr[i-1,j]
        else:
            arr[i,j] = max(arr[i-1,j], (price[i] + arr[i, j-i-1]))
        
print(arr)
print("Maximum profit is", arr[len(price)-1,cuts])
