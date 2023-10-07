'''Python Program for Find remainder of array multiplication divided by n'''

arr = [100, 10, 5, 25, 35, 14];lens = len(arr);n = 11
mul = 1
for i in range(lens):
    mul = (mul * (arr[i] % n)) % n
print(mul % n)