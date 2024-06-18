#!/usr/bin/python3
""" Log parsing """

import sys
import re
from collections import defaultdict


def main():
    """
    Get the metrics to be printed out from the stdin
    """
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    log_pattern = re.compile(
        r'(\S+) - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )

    try:
        for line in sys.stdin:
            match = log_pattern.match(line)
            if match:
                status_code = match.group(2)
                file_size = int(match.group(3))

                total_size += file_size
                status_counts[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    computer_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        computer_metrics(total_size, status_counts)
        raise

    computer_metrics(total_size, status_counts)


def computer_metrics(total_size, status_counts):
    """ prints out the computer metrics """
    print("File size: {}".format(total_size))

    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


if __name__ == '__main__':
    main()
