if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        a = input().split()
        if len(a) == 3:
            eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
        elif len(a) == 2:
            eval("list." + a[0] + "(" + a[1] + ")")
        elif a[0] == "print":
            print(list)
        else:
            eval("list." + a[0] + "()")