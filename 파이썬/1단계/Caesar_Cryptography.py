def solution(s, n):
    answer = ''
    for i in s:
        check=ord(i)+n
        if i==' ':
            answer+=i
        elif (i<='Z' and chr(check)>'Z') or chr(check)>'z':
            answer+=chr(check-26)
        else:
            answer+=chr(check)
    return answer
