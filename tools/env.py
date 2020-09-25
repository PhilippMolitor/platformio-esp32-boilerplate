#!/usr/local/bin/python3

# thanks to:
#   h0tw1r3 @ StackOverflow
#   https://stackoverflow.com/a/50456924/13954640

import sys
import os
import re

matcher = re.compile(r'''^([^\s=]+)=(?:[\s"']*)(.+?)(?:[\s"']*)$''')
result = []
path = os.path.join(os.getcwd(), '.env')

try:
    with open(path) as f:
        for line in f:
            pair = matcher.match(line)
            if pair is not None:
                result.append((pair.group(1), '\\"' + pair.group(2) + '\\"'))
except:
    exit(1)

Import("env")
env.Append(CPPDEFINES=result)
