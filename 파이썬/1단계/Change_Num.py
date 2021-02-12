def solution(n):
    answer = 0
    strnum=list(str(n))
    for i in range(len(strnum)):
        for j in range(i,len(strnum)):
            if int(strnum[i])<int(strnum[j]):
                temp=strnum[i]
                strnum[i]=strnum[j]
                strnum[j]=temp
    answer=int(''.join(strnum))
    return answer
