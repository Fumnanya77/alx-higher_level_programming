#!/usr/bin/python3
def multiple_returns(sentence):
    lent = len(sentence)
    firs = sentence[0]
    if sentence == "":
        lent = 0
        firs = None
    return (lent, firs)
