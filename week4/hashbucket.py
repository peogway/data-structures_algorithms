class HashBucket:
    def __init__(self, M, B):
        self.M = M
        self.B = B
        self.T = [[None for _ in range(M//B)] for _ in range(B)]

        self.overflow =[]

    def hash(self,data):
        sum =0
        for c in data:
            sum+= ord(c)    
        return sum%self.M

    def print(self):
        for bucket in self.T:
            for d in bucket:
                if (d is None) : print('F ', end ='')
                elif (d is True) : print('T ', end ='')
                else: print(d, end =' ')
        for d in self.overflow:
          print(d,end=' ')
        print()
    
    def insert(self, data):
      index = self.hash(data)


      bucket_num = self.M//self.B

      bucket_pos = index%(self.B)
      bucket_i = 0
      original_i = bucket_i
      

      if self.T[bucket_pos][bucket_i] == data: return


      while self.T[bucket_pos][bucket_i] is not None and self.T[bucket_pos][bucket_i] is not True:
          bucket_i = (bucket_i+1)%bucket_num
          if bucket_i== original_i:
              if (len(self.overflow)<self.M) and (data not in self.overflow): self.overflow.append(data)
              return


      self.T[bucket_pos][bucket_i] = data

    def delete(self, data):
      index = self.hash(data)
      bucket_num = self.M//self.B

      bucket_pos = index%(self.B)
      bucket_i = 0


      while self.T[bucket_pos][bucket_i] is not None:

        if self.T[bucket_pos][bucket_i] == data:
            self.T[bucket_pos][bucket_i] = True
            return
        bucket_i = (bucket_i+1)%bucket_num
        if bucket_i== 0:
            self.overflow.remove(data)
            return
      



if __name__ == "__main__":
    table = HashBucket(8, 4)
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


