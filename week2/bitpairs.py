def pairs(s):
    bit_pos_A= []
    for i in range(len(s)):
      if s[i] == '1': bit_pos_A.append(i)

    sum =0
    n = len(bit_pos_A)
    for i in range(0,n-1):
      sum+=(n-i-1)*(i+1)*(bit_pos_A[i+1]-bit_pos_A[i])
          
    return sum

if __name__ == "__main__":
    print(pairs("100101"))
    print(pairs("101"))
    print(pairs("100100111001"))