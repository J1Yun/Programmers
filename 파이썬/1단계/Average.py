def solution(arr):
    answer = 0
    sum = 0
    for i in arr:
        sum=sum+i
    answer=sum/len(arr)
    return answer
