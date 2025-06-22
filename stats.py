from collections import Counter


def word_counter(str:str):
    word_count = len(str.split())
    return word_count 

def char_counter(str:str):
    str_lower = str.lower()
    return Counter(str_lower)