from collections import Counter


def word_counter(str:str):
    word_count = len(str.split())
    return word_count 

def char_counter(str:str):
    str_lower = str.lower()
    return Counter(str_lower)

def sorter(items):
    return items["num"]

def dict_sorter(dict):
    items = []
    for key in dict:
        if key.isalpha():
            items.append({"char":key,"num":dict[key]})
    items.sort(reverse=True,key=sorter)
    return items