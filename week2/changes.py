def changes(A):
    stack = []
    c =0
    for x in A:
      if len(stack)>0:
          if x==stack[-1]: 
            c+=1
            stack.pop()
          else:
            stack.pop()
            stack.append(x)
      else:
         stack.append(x)
    return c


if __name__ == "__main__":
  print(changes([1, 1, 1, 1, 1]))
  print(changes([1, 3, 2, 2, 3, 3, 4, 1, 4, 1]))
  print(changes([3, 3, 5, 1, 4, 2, 1, 2, 1]))
  print(changes([4, 2, 4, 5, 1, 5, 2]))
  print(changes([3, 2, 3, 2, 2, 1, 3, 2, 1, 3]))
  print(changes([1, 2, 5, 5, 4, 2]))
  print(changes([4, 4, 2, 3, 3, 1, 3, 3, 4, 4]))
  print(changes([1, 1, 2, 2, 2, 2]))
  print(changes([3, 2, 5, 2, 2, 2, 4]))
  print(changes([1, 1, 1, 4, 2, 3, 3, 2, 2, 3]))
  print(changes([3, 1, 4, 4, 1, 4, 3, 3, 3, 3]))