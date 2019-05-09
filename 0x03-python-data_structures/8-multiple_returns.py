#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), None if len(sentence) is 0 else sentence[0])
