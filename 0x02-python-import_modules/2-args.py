#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv_list = sys.argv

    if len(argv_list) == 1:
        print(f"0 arguments")
    if len(argv_list) == 2:
        print(f"1 argument:")
    if len(argv_list) > 2:
        print(f"{len(argv_list)-1} arguments:")

    for argu in range(0, len(argv_list)):
        if argu == 0:
            continue
        print(f"{argu}: {argv_list[argu]}")
