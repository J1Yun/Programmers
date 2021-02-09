def solution(s):
    answer = ''
    count = 0
    for i in s:
        if i.isalpha():
            if count%2==0:
                answer+=i.upper()
            else:
                answer+=i.lower()
            count+=1
        else:
            answer+=i 
            count=0
    return answer
