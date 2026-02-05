def bottom_up_cut_rod(p, n):
    # Create the table (notebook)
    r = [0] * (n + 1)
    
    # Fill the table from 1 to n
    for j in range(1, n + 1):
        q = float('-inf')
        # For each length j, find the best cut
        for i in range(1, j + 1):
            q = max(q, p[i-1] + r[j - i])
        
        # Save the result for length j
        r[j] = q
        
    return r[n]
p = [4,8,3,1,7,6,9,4,5]
x = int(input("enter length of rod\n less 9 due to price list constrain\n"))
print(bottom_up_cut_rod(p,x))
