import string

n = int(input())
a = string.ascii_lowercase
l = []
for i in range(n):
    s = '-'.join(a[i:n])
    l.append((s[::-1] + s[1:]).center(4*n-3, "-"))
print("\n".join(l[:0:-1] + l))