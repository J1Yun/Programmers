def solution(num):
    answer = 0
    rest = num
    while rest!=1:
        if rest%2==0:
            rest=rest//2
        else:
            rest=rest*3+1
        answer=answer+1
        if answer==500:
            return -1
    return answer
