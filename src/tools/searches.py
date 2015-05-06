

def binary_search(array, key, start, end):
    if end < start:
        return -1
    else:
        midpoint = start + (end - start) // 2

        if key < array[midpoint]:
            return binary_search(array, key, start, midpoint - 1)
        elif key > array[midpoint]:
            return binary_search(array, key, midpoint + 1, end)
        else:
            return midpoint

