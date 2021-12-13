# Using numpy arrays
import numpy as np

price = []
cuts = int(input("Enter number of cuts:"))
print("Enter Price of Cuts:")
for i in range(0, cuts):
    num = int(input())
    price.append(num)
print(price)

# Make an initial grid of all zeros
arr = np.zeros((len(price),cuts+1))

for i in range(0,len(price)):
    for j in range(0,cuts+1):

        # First column => 0 length of rod => 0 profit
        if j == 0:
            continue

        # First row => arr[i-1,j] doesn't exist so just pick the second value
        elif i == 0:
            arr[i,j] = price[i] + arr[i, j-i-1]

        # where j <= i => arr[i, j-i-1] doesn't exist so just pick the first value
        elif (j-i-1) < 0:
            arr[i,j] = arr[i-1,j]
        
        # using the whole expression
        else:
            arr[i,j] = max(arr[i-1,j], (price[i] + arr[i, j-i-1]))
        
# Answer in the extreme bottom right cell
print(arr)
print("Maximum profit is", arr[len(price)-1,cuts])