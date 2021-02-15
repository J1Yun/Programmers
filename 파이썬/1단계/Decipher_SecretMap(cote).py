#2018 KAKAO BLIND RECRUITMENT

def solution(n, arr1, arr2):
    answer = []
    bin1 = []  
    bin2 = []
    for i in range(n):
        z1=''
        z2=''
        t = format(arr1[i],'b')
        if len(t)<n:
            for a in range(n-len(t)):
                z1+='0'
        z1 += t
        bin1.append(z1)
        t = format(arr2[i],'b')
        if len(t)<n:
            for a in range(n-len(t)):
                z2+='0'
        z2 += t
        bin2.append(z2)

    for i in range(n):
        s = ''
        for j in range(n):
            p = str(int(bin1[i][j]) or int(bin2[i][j]))
            if p =='1':
                s+='#'
            else:
                s+=' '
        answer.append(s)
    return answer
