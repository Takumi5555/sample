n = list(input())
if n[0] < n[1] or n[0] == n[1] and n[1] < n[2]:
  ans = int(n[0]*3)+111
else:
  ans = int(n[0]*3)

print(ans)