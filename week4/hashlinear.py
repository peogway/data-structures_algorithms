class HashLinear:
    def __init__ (self,M):
        self.M=M
        self.T = M*[None]
    
    def hash(self,data):
      sum =0
      # if (data=='peach' or data=='mango' or data=='grapes'):
      for x in data:
        sum+=ord(x)
      #   print('char:', x, ', ascii:', ord(x), ', sum:', sum)
      # print('remainder:', sum%self.M)
      # print('--------------------------------')
      return sum%self.M
    
    def print(self):
        for d in self.T:
          if d ==None: print('F ',end='')
          elif d==True: print('T ', end='')
          else: print(d,end=' ')
        print()

    def insert(self,data):
      # print('data:', data )

      index = self.hash(data)
      if self.T[index] ==data: return

      original_index = index
      while self.T[index] is not None and self.T[index] is not True:
          index = (index + 1) % self.M
          if index == original_index:
              return
      
      self.T[index] = data

    def delete(self, data):
      index = self.hash(data)
      original_index = index
      
      while self.T[index] is not None:
        if self.T[index] == data :
          self.T[index] = True
          return
        index = (index + 1) % self.M
        if index == original_index: return



if __name__ == "__main__":
    table = HashLinear(8)
    table.print()
    
    table.insert("apple")
    table.insert("orange")
    table.insert("banana")
    table.insert("grapes")
    table.insert("mango")
    table.insert("peach")
    table.insert("apple")
    table.print()

    table.delete("banana")
    table.delete("kiwi")
    table.delete("peach")
    table.print()
    