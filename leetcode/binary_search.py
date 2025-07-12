def binary_search(arr: list, target: float) -> int:
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return low


ind = binary_search([1,4,5,6,7], target=5.5)
print(ind)
