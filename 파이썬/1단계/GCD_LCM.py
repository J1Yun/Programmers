def solution(n, m):
    answer = []
    if n <= m:
        for i in range(1,n+1):
            if n%i==0 and m%i==0:
                num=i
    else:
        for i in range(1,m+1):
            if n%i==0 and m%i==0:
                num=i
                
    answer.append(num)
    answer.append(num*(n//num)*(m//num))
    return answer
