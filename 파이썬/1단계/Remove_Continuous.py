def solution(arr):
    answer = []
    l=len(arr)
    for i in range(l-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    answer.append(arr[l-1])
    return answer
