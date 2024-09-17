def split(T):
    n= len(T)
    c=0
    if n<2:
        return 0
    max_left= [0]*n
    min_right= [0]*n

    max_left[0] = T[0]
    min_right[-1] = T[-1]
    for i in range(1, n):
        if max_left[i-1]<T[i]: max_left[i]=T[i]
        else: max_left[i]=max_left[i-1]
        
        if min_right[-i] >T[-i-1]: min_right[-i-1] = T[-i-1]
        else: min_right[-i-1] = min_right[-i]

    # print(max_left, min_right)
    
    for i in range(n-1):
        if max_left[i] <min_right[i+1]: c+=1

    return c

if __name__ == "__main__":
    
    print(split([1, 2, 3, 4, 5]))
    print(split([5, 4, 3, 2, 1]))
    print(split([2, 1, 2, 5, 7, 6, 9]))
    print(split([1, 2, 3, 1]))