#!/usr/bin/env python3
"""
parse log from stdin
"""
import sys
import re

count = 0
file_size = 0
codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0,
         "500": 0}

pattern = r'^([\d\.]+)\s+-\s+\[(.*?)\]\s+"(.*?)"\s+(\d{3})\s+(\d+)$'
try:
    for line in sys.stdin:

        match = re.match(pattern, line)
        if match:
            file_size += int(line.split()[-1])
            count += 1
            code = line.split()[-2]
            codes[code] += 1
        if count == 10:
            print('File size: {}'.format(file_size))
            for code, c in codes.items():
                print('{}: {}'.format(code, c))
            count = 0
except KeyboardInterrupt:
    print('File size: {}'.format(file_size))
    for code, c in codes.items():
        print('{}: {}'.format(code, c))
    count = 0
    raise KeyboardInterrupt
