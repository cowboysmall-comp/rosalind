

'''
    some other implementations:


    recursive:

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


    iterative:

    def binary_search(array, key, start, end):
        while start <= end:
            midpoint = start + (end - start) // 2

            if key < array[midpoint]:
                end   = midpoint - 1
            elif key > array[midpoint]:
                start = midpoint + 1
            else:
                return midpoint

        return -1

'''




def binary_search(array, key, start, end):
    while start < end:
        midpoint = start + (end - start) // 2

        if array[midpoint] < key:
            start = midpoint + 1
        else:
            end   = midpoint

    if start == end and array[start] == key:
        return start
    else:
        return -1

