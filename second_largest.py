arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
print("Second largest:", arr[-2])
