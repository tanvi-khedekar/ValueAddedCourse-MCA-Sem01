def shuffleArray(arr, n):
  result = []

  for i in range(n):
    result.append(arr[i])
    result.append(arr[i + n])

  return result