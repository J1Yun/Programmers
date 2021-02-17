#2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    answer = []
    rate = []
    for i in range(1,N+1):
        countA = 0
        countS = 0
        for j in stages:
            if i<=j:
                countA+=1
            if i==j:
                countS+=1
        if countA == 0:
            rate.append(0)
        else:
            rate.append(countS/countA)
        
    answer=[i[0]+1 for i in sorted(enumerate(rate), key=lambda x:x[1], reverse=True)]

    return answer
