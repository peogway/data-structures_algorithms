def isort(A):
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if (A[i] >=A[j]):
        A[i],A[j] = A[j],A[i]


if __name__ == "__main__": 
    A = [4, 3, 6, 2, 9, 7, 1, 8, 5]
    isort(A)
    print(A)
