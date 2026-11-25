def duplicateZeros(arr: List[int]) -> List[int]:
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i = i + 2
        else:
            i = i + 1
    return arr
