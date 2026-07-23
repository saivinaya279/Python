def build_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)   

    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix


def range_sum(prefix, left, right):
    
    return prefix[right + 1] - prefix[left]



arr = [2, 4, 1, 5, 3]
prefix = build_prefix_sum(arr)
print(range_sum(prefix, 1, 3))   