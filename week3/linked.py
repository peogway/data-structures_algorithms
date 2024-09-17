class Node:
    def __init__(self, data, next):
        self.data= data
        self.next = next

    

class LinkedList:
    def __init__(self):
      self.tail = Node(None,None)
      self.head = Node(None, self.tail)
      self.len=0


    def print(self):
      head = self.head
      first = True
      while (head != None):
        data=head.data
        if first:
          print(data, end='')
        else: 
          if data!=None:
            print(' ->',data,end='')
        first =False
        if head.next==None: print()
        head = head.next
  
    def append(self, data):
      if self.len ==0: 
        self.head.data =data
        self.len +=1
      elif self.len==1:
        self.tail.data=data
        self.len+=1
      else:
        new_node = Node(data, None)
        self.tail.next = new_node
        self.tail = self.tail.next
        self.len+=1

    def insert(self, data, i):
      self.len+=1
      head = self.head
      prev = None
      index = 0
      while (i>0):
        prev=head
        head = head.next
        i-=1
      new_node = Node(data, head)
      if prev ==None: 
         self.head = new_node
         return
      prev.next = new_node

    def delete(self, i):
        if i >= self.len or i < 0: 
            return None

        head = self.head
        prev = None
        index = 0

        while head != None and index < i:
            prev = head
            head = head.next
            index += 1

        if head == None:
            return None

        deleted_value = head.data

        if prev == None:
            self.head = head.next
        else:
            prev.next = head.next

        if head.next == None:
            self.tail = prev

        self.len -= 1
        return deleted_value

    def index(self, data):
      index =0
      head=self.head
      while (head!=None):
        dt = head.data
        if data ==dt : return index
        index +=1
        head = head.next
      return -1
    def swap(self, i,j):
      object_at_i = None
      object_at_j = None
      index =0
      head = self.head
      while (index<=i or index<=j):
        if index ==i :
          # print(index)
          object_at_i= head
          # print(object_at_i.data)
        if index ==j :
          # print(index)
          object_at_j = head
        # print(head.data)
        head = head.next
        index+=1
      data = object_at_i.data
      object_at_i.data = object_at_j.data
      object_at_j.data = data

    def isort(self):
       n = self.len
       i=0
       head = self.head
       while (i <n -1):
          j=i+1
          after = head.next
          while (j <n):
             if (head.data> after.data):
              self.swap(i,j) 
             after= after.next
             j+=1
          head = head.next
          i+=1
        


if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()
    L.isort()
    L.print()