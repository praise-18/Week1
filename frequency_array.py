from collections import Counter
arr = list(map(int, input().split()))
freq = Counter(arr)
for k, v in freq.items():
    print(f"{k} -> {v} times")
