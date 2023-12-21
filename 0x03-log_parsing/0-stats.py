#!/usr/bin/python3
'''
     script that reads stdin line by line and computes metrics
'''

import re
import sys


def process_line(line):
    """
    Process a line and extract information.
    """
    # Define the regex pattern for the input format
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

    match = pattern.match(line)
    if match:
        ip_address, date, status_code, file_size = match.groups()
        return int(status_code), int(file_size)
    else:
        return None


def print_statistics(total_size, status_counts):
    """
    Print the computed statistics.
    """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            data = process_line(line.strip())
            if data:
                status_code, file_size = data
                total_size += file_size

                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

            # Print statistics after every 10 lines
            if i % 10 == 0:
                print_statistics(total_size, status_counts)
                print("-----")

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
