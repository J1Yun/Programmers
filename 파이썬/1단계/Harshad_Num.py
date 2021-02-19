def solution(x):
    strx = str(x)
    length = len(str(x))
    sum = 0
    for i in range(length):
        sum+=int(strx[i])
    if x%sum==0:
        return True
    else:
        return False
   
