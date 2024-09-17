def primes(N):
  def is_prime(n):
    if n<2: return False
    if n==2 : return True
    for i in range(2, int(n**1/2+1)):
      if n%i==0: return False
    return True
  c=0
  for i in range(2,N+1):
    if is_prime(i): 
      c+=1
  return c
if __name__ == "__main__":
  print(primes(7))
  print(primes(15))
  print(primes(50))