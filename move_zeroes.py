arr = list(map(int, input().split()))
non_zero = [x for x in arr if x != 0]
zeros = [0] * (len(arr) - len(non_zero))
print("After moving zeros:", non_zero + zeros)
