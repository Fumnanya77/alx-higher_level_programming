#!/usr/bin/python3
def multiple_returns(sentence):
    firs = sentence[0]
    if sentence == "":
        lent = 0
        firs = None
    else:
        lent = len(sentence)
        firs = firs
    return (lent, firs)
