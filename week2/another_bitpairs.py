def pairs(s):

    sum =0
    sum_i=0
    count_i =0
    n = len(s)
    for i in range(n):
      if  s[i] == '1':
        sum+= i*count_i - sum_i
        count_i+=1
        sum_i+=i
          
    return sum

if __name__ == "__main__":
    print(pairs("100101"))
    print(pairs("0101"))
    print(pairs("101"))
    print(pairs("100100111001"))