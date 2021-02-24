def solution(n):
    answer = 0
    rest = n
    while rest!=0:
        answer+=rest%10
        rest=rest//10
    return answer
