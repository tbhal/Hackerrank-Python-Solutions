# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 00:38:39 2018

@author: tushar
"""

import re

for _ in range(int(input())):
    m = re.findall(r'(?<!^)#[0-9a-f]{3,6}', input().strip(), flags = re.I)
    if m:
        print('\n'.join(m))