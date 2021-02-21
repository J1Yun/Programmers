def solution(arr):
    answer = arr
    min=answer[0]
    for i in answer:
        if i<min:
            min=i
    answer.remove(min)
    if not answer:
        answer.append(-1)
    return answer
