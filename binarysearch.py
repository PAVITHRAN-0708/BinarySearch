def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


if __name__ == "__main__":
    data = [8, 12, 23, 45, 56, 99]
    target_value = 56
    
    print("Sorted Array:", data)
    print(f"Searching for: {target_value}")
    
    result = binary_search(data, target_value)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")