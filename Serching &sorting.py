arr = [10, 20, 30, 40, 50]
key = 30

for i in range(len(arr)):
    if arr[i] == key:
        print(i)
        break
else:
    print(-1)