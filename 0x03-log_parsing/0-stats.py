#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
                code> <file size>
"""
import sys


count = 0
file_size = 0
status = {}


def printlog(status, file_size) -> None:
    """parse log and print formatted log"""
    print("File size: {}".format(file_size))
    for k, v in sorted(status.items(), key=lambda item: int(item[0])):
        print("{}: {}".format(k, v))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            parsed = line.split(' ')
            count += 1
            try:
                file_size += int(parsed[-1])
                status_code = parsed[-2]
                if status_code and type(eval(status_code)) == int:
                    status[status_code] = status[status_code] + \
                        1 if status_code in status else 1
            except (IndexError, ValueError):
                pass
            if count % 10 == 0:
                printlog(status, file_size)
    except KeyboardInterrupt:
        printlog(status, file_size)
        raise
    else:
        printlog(status, file_size)
