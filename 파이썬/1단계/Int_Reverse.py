def solution(n):
    
    answer = []
    string = str(n)
    for i in string:
        answer.append(int(i))
    answer.reverse()
    return answer
