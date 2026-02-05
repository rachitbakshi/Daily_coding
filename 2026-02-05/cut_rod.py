def cut_rod(p,n):
  if n == 0:
    return 0
  q = float('-inf')
  for i in range(1,n+1):
    r = p[i-1] + cut_rod(p,n-i)
    if r>q:
      q = r
  return q
p = [1, 5, 8, 9, 10, 1, 17, 20]
x = int(input("enter length of rod \n(less than 8, because i have put prices of lengths up to 8 only) \n"))
print(cut_rod(p,x))
