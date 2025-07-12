def mergesort(l: list):
    half = len(l) // 2
    a = l[:half]
    b = l[half:]
    if len(a) > 1:
        a = mergesort(a)
    if len(b) > 1:
        b = mergesort(b)
    return merge(a, b)


def merge(a, b):
    merged = []
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            merged.append(a[a_idx])
            a_idx += 1
        else:
            merged.append(b[b_idx])
            b_idx += 1
    if a_idx < len(a) or b_idx < len(b):
        if a_idx < len(a):
            idx = a_idx
            arr = a
        else:
            idx = b_idx
            arr = b
        while idx < len(arr):
            merged.append(arr[idx])
            idx += 1

    return merged

m = mergesort([5,6,78,4,6])
print(m)
