n, d = input().split(' ')
a = [int(i) for i in input().split()]
for j in range(int(n)):
    print(a[(j + int(d)) % int(n)], end=' ' )
