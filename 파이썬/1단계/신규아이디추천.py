import re

def toLower(string):
    return string.lower()

def filtering(string):
    return re.sub('[=+$%&,#/\?:^@*~!\{\}\<\>\\\(\)\[\]]', '', string)

def reduceDot(string):
    length = 0
    while length != len(string):
        length = len(string)
        string = string.replace('..', '.')
    return string

def removeDot(string):
    if len(string) >= 1 and string[0] == '.':
        string = string[1:]
    if len(string) >= 1 and string[-1] == '.':
        string = string[:-1]
    return string

def fillEmptyString(string):
    if len(string) == 0:
        string = 'a'
    return string

def processStringLength(string):
    if len(string) >= 16:
        string = string[:15]
        string = removeDot(string)
    elif len(string) <= 2:
        string += string[-1] * (3 - len(string))
    return string

def solution(new_id):
    new_id = toLower(new_id)
    new_id = filtering(new_id)
    new_id = reduceDot(new_id)
    new_id = removeDot(new_id)
    new_id = fillEmptyString(new_id)
    new_id = processStringLength(new_id)
    return new_id