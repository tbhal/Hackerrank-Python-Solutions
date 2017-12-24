import re
Mix = filter(None, re.split(r'[\,\.]*', input().strip()))
print("\n".join(Mix))