def insertAtPosition(arr: list[int], X: int, P: int) -> list[int]:
    arr.insert(P, X)
    arr.pop()
    return arr
