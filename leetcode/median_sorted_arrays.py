# Python Program to find the median of merged sorted
# array using Binary Search

# Function to find median of merged sorted array
def getMedianSameLen(a, b):
    n = len(a)
    low = 0
    high = n - 1

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = n - mid1
        r1 = float('inf') if mid1 == n else a[mid1]
        l1 = float('-inf') if mid1 == 0 else a[mid1-1]

        r2 = float('inf') if mid2 == n else b[mid2]
        l2 = float('-inf') if mid2 == 0 else b[mid2-1]

        if r1 >= l2 and l1 <= r2:
            return (max(l1, l2) + min(r1, r2)) / 2.0
        if l1 > r2:
            high = mid1 - 1
        else:  # l2 < r1
            low = mid1 + 1
    return 0


def get_median(a, b):
    total = len(a) + len(b)
    half = total // 2

    if len(a) > len(b):
        a, b = b, a

    low, high = 0, len(a) - 1

    while True:
        mid1 = (low + high) // 2
        mid2 = half - (mid1 + 1) - 1

        r1 = a[mid1+1] if (mid1+1) < len(a) else float('inf')
        l1 = a[mid1] if mid1 >= 0 else float('-inf')

        r2 = b[mid2+1] if (mid2+1) < len(b) else float('inf')
        l2 = b[mid2] if mid2 >= 0 else float('-inf')

        if r1 >= l2 and l1 <= r2:
            if total % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                return min(r1, r2)
        if l1 > r2:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return 0




a_ = [1, 2]
b_ = [3, 4]

print(get_median(a_, b_))