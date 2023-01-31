from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    score = []
    recruit = defaultdict(set)
    for i in range(len(info)):
        data = info[i].split()
        recruit['-'].add((int(data[-1]), i))
        for j in range(4):
            recruit[data[j]].add((int(data[-1]), i))
    print(recruit)
    for q in query:
        data = q.split()
        count = 0

        applicant = recruit[data[i]]
        for i in range(2, 7, 2):
            applicant = applicant.intersection(recruit[data[i]])
        idx = bisect_left(list(applicant), (int(data[-1]), 0))
        count = len(applicant) - idx
        
        answer.append(count)
    print(recruit)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))