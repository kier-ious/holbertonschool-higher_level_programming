#!/usr/bin/python3
for i in range(0, 10):
    for t in range(1, 10):
        if i != t and i < t:
            if i == 8 and t == 9:
                break
            print("{}{}, ".format(i, t), end="")
print("89")
