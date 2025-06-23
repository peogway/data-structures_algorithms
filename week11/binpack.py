# binpack.py

def binpack(items, S):
    items.sort(reverse=True)  # Sort items in descending order
    bins = []  # List to store bins
    
    for item in items:
        placed = False
        for bin in bins:
            if sum(bin) + item <= S:
                bin.append(item)
                placed = True
                break
        if not placed:
            bins.append([item])
    
    return bins

if __name__ == "__main__":
    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")
