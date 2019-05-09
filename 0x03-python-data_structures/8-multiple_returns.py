#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), None if sentence is None else sentence[0])
