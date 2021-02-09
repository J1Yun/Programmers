def solution(a, b):
    answer = ''
    date=[31,29,31,30,31,30,31,31,30,31,30,31]
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    days=0
    for i in range(a-1):
        days=days+date[i]
    days=days+b
    result=days%7
    answer=day[result]
    return answer
