#!/usr/bin/python3
"""
parse log from stdin
"""
import sys
import re

# sample
# 78.99.227.220 - [2017-02-05 23:25:51.534767] "GET /projects/260 HTTP/1.1" 401 724
count = 0
file_size = 0
codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0,
         "500": 0}

pattern = r'^([\d\.]+)\s+-\s+\[(.*?)\]\s+"(.*?)"\s+(\d{3})\s+(\d+)$'

def print_stat():
    """print the stats"""
    print('File size: {}'.format(file_size))
    for code, c in sorted(codes.items()):
        if c > 0:
            print('{}: {}'.format(code, c))


if __name__ == "__main__":
    try:
        for line in sys.stdin:

            match = re.match(pattern, line)
            if match:
                file_size += int(line.split()[-1])
                count += 1
                code = line.split()[-2]
                codes[code] += 1
            if count == 10:
                print_stat()
                count = 0
    except KeyboardInterrupt:
        print_stat()
        count = 0
        raise KeyboardInterrupt
