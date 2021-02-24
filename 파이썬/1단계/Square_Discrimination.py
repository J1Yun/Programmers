def solution(n):
    answer = 0
    i = 1
    while i*i<=n:
        if i*i==n:
            answer=i
        i=i+1
    if answer==0:
        return -1
    else:
        return (answer+1)*(answer+1)
 
