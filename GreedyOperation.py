arr = [1, 3, 4, 2]

arr = sorted(arr)

sum = 0
operation = 0

sum = arr[0]+arr[1]
operation += sum

for j in range(2,len(arr)):
    sum += arr[j]
    operation += sum

print(sum)
print(operation) 