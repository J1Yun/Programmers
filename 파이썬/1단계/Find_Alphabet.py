def solution(s):
    countp=0
    county=0
    s= s.lower()
    for i in s:
        if i=='p':
            countp=countp+1
        if i=='y':
            county=county+1
    if countp==county:
        return True
    else:
        return False
    
