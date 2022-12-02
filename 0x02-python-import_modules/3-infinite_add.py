#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print(f"{sum(map(int, argv[1:]))}")
