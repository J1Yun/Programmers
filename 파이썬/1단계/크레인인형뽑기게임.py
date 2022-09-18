def makePop(array):
    if len(array) >= 2:
        if array[-1] == array[-2]:
            array.pop()
            array.pop()
            return 2
    return 0

def solution(board, moves):
    answer = 0
    bocket = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]:
                bocket.append(board[i][m-1])
                answer += makePop(bocket)
                board[i][m-1] = 0
                break
    return answer
