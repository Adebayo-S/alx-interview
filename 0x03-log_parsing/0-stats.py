#!/usr/bin/python3
import sys
import re

count = 0
file_size = 0
status = {}


def printlog(status, file_size) -> None:
    print(f"File size: {file_size}")
    for k, v in sorted(status.items(), key=lambda item: int(item[0])):
        print(f"{k}: {v}")


try:
    for line in sys.stdin:
        match = re.match(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*)\] "(.*)" (\d+) (\d+)', line)
        if match:
            count += 1
            file_size += int(match.group(5))
            status_code = match.group(4)
            if status_code and type(eval(status_code)) == int:
                status[status_code] = status[status_code] + \
                    1 if status_code in status else 1
            if count % 10 == 0:
                printlog(status, file_size)
except KeyboardInterrupt:
    printlog(status, file_size)
