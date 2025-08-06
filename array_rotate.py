arr = list(map(int, input().split()))
arr = [arr[-1]] + arr[:-1]
print("Rotated array:", arr)
