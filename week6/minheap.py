import math

class MinHeap:
    def __init__(self, A):
        n = len(A)
        for i in range(n // 2 - 1, -1, -1):
          self.heapify(A, n, i)
        self.A=A
        self.n = len(A)
    

    
    def heapify(self,arr, n, i, ch = True):
      if i < 0 : return
      # Initialize smallest as root
      smallest = i 
      
      #  left index = 2*i + 1
      l = 2 * i + 1 
      
      # right index = 2*i + 2
      r = 2 * i + 2  

      # If left child is larger than root
      if l < n and arr[l] < arr[smallest]:
          smallest = l

      # If right child is larger than smallest so far
      if r < n and arr[r] < arr[smallest]:
          smallest = r

      # If smallest is not root
      if smallest != i:
          arr[i], arr[smallest] = arr[smallest], arr[i]  # Swap
          if not ch:
             self.heapify(arr, n, (i-1)//2, False)

          # Recursively heapify the affected sub-tree
          self.heapify(arr, n, smallest)


    def print(self):
        # def printCurrentLevel(pos_node, level):
        #     if pos_node >= self.n:
        #         return
        #     if level == 1:
        #         # print(pos_node, end=' ')
        #         print(self.A[pos_node], end=" ")
        #     elif level > 1:
        #         printCurrentLevel(2*pos_node+1, level - 1)
        #         printCurrentLevel(2*pos_node+2, level - 1)

        # for i in range(self.n):
        #     printCurrentLevel(0, i)
        # print()

        if self.n==0: return

        for i in range(self.n):
            print(self.A[i], end = ' ')
        print()

    def height(self, pos):
      if pos == 0:
        return -1  # Empty tree
      return math.ceil(math.log2(pos))
    
    def push(self, key):
       self.A.append(key)
       self.n+=1

       self.heapify(self.A, self.n, (self.n-2)//2, False)

    def pop(self):
       if self.n ==0:
          return -1
       self.A[0], self.A[self.n-1] = self.A[self.n-1], self.A[0]
       self.n-=1
       element = self.A.pop()
       self.heapify(self.A, self.n, 0)
       return element



if __name__ == "__main__":

  heap = MinHeap([])
  # heap.print()
# 
  for num in (9, 6, 4, 12, 7, 1, 3):
      heap.push(num)

  # heap.push(1)
  heap.pop()
  heap.pop()

  heap.print()