def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
      pivot = arr.pop()
    items_greater = []
    items_lower = []
    for item in arr:
      if item > pivot:
        items_greater.append(item)
      else:
        items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([2,3,19,14,5,6,7,8,9,]))