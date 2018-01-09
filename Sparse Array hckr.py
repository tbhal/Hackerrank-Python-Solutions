n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
m=int(input())
for i in range(m):
    query = input()
    count=0
    for i in range(n):
        if query==arr[i]:
            count+=1
    print(count)