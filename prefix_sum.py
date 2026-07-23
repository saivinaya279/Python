def build_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * (n + 1)   # prefix[0] = 0 (sum of zero elements)

    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix


def range_sum(prefix, left, right):
    # sum of arr[left..right] inclusive
    return prefix[right + 1] - prefix[left]


# usage
arr = [2, 4, 1, 5, 3]
prefix = build_prefix_sum(arr)
print(range_sum(prefix, 1, 3))   # 10