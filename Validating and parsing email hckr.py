# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 00:43:38 2018

@author: tushar
"""

import re
for _ in range(int(input())):
    s=input()
    m=re.match(r'.*?\<([a-z]+[a-z0-9_\.\-]+)@([a-z]+)\.([a-z]{1,3})\>.*?',s)
    if m is not None and len(m.groups())==3:
        print(s)