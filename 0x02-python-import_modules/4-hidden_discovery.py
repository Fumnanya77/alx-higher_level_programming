#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
	hidden_list = dir(hidden_4)
    for i in range(0, len(hidden_list)):
        if hidden_list[i].startswith("__")
            continue
        print(f"{hidden_list[i]}")
