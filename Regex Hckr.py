import re
T = int(input())
for i in range(T):
    k = input()
    print(bool(re.match(r"^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$", k)))