#2018 KAKAO BLIND RECRUITMENT

def solution(dartResult):
    answer = 0
    split = []
    cal = []
    s = ''
    for i in range(len(dartResult)):
        s+=dartResult[i]
        if(not dartResult[i].isdigit() and (i==len(dartResult)-1 or dartResult[i+1].isdigit())):
            split.append(s)
            s = ''

    for i in range(3):
        s = ''
        for j in split[i]:
            if j.isdigit():
                s+=j
        cal.append(int(s))
        if 'D' in split[i]:
            cal[i]=pow(cal[i],2)
        elif 'T' in split[i]:
            cal[i]=pow(cal[i],3)
        if '*' in split[i]:
            if i==0:
                cal[i]=cal[i]*2
            else:
                for t in range(i-1,i+1):
                    cal[t]=cal[t]*2
        elif '#' in split[i]:
            cal[i]=cal[i]*(-1)

    answer = sum( i for i in cal)               
    return answer
