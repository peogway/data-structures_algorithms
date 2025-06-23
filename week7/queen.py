def queen(n,m):
    # i=0
    def solve(row, queens_placed, cols, diags1, diags2):
        # nonlocal i
        if queens_placed == m:
            return 1
        if row >= n:
            return 0
        if n-row+1 < (m-queens_placed):
            return 0
        count = 0
        available_columns = ~cols & ((1 << n) - 1)
        while available_columns:

            # i+=1
            # print(i)

            col = available_columns & -available_columns
            pos = col.bit_length() - 1
            available_columns-= col
            diag1_mask = 1 << (row - pos + n - 1)
            diag2_mask = 1 << (row + pos)
            if (cols & col) == 0 and (diags1 & diag1_mask) == 0 and (diags2 & diag2_mask) == 0:
                count += solve(
                    row + 1,
                    queens_placed + 1,
                    cols | col,
                    diags1 | diag1_mask,
                    diags2 | diag2_mask
                )
        count += solve(row + 1, queens_placed, cols, diags1, diags2)
        return count
    return solve(0, 0, 0, 0, 0)

if __name__ == "__main__":
    print('#############')
    print(queen(4, 4))  # 2
    # print(queen(4, 2))  # 44
    # print(queen(6,4))   #982
    # print(queen(7,2))   #700
    # print(queen(8,8))   #92
    # print(queen(11,11))
    # print(queen(12,12))
    # print(queen(13,12))
    print('###############')