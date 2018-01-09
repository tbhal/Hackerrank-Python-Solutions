import sys
if sys.version_info[0]>=3: input=input

s= input().strip()
t= input().strip()
a=[i for i in range(len(s)-len(t)+1) if s[i:i+len(t)]==t]
if a:
	for e in a: print((e,e+len(t)-1))
else:
    print((-1,-1))