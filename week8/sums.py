
def sums(items):
  possible_sum = {0}  # all possible sums
  for item in items:
     new_sums = {item+s for s in possible_sum}
     possible_sum |= new_sums

  return len(possible_sum)-1

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  
    print(sums([2, 2, 3]))                  
    print(sums([1, 3, 5, 1, 3, 5]))         
    print(sums([1, 15, 5, 23, 100, 55, 2])) 