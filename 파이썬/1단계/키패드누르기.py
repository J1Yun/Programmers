def solution(numbers, hand):
    answer = ''
    keypad = {1: (1, 1), 2: (1, 2), 3: (1, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3), 7: (3, 1), 8: (3, 2), 9: (3, 3), 0: (4, 2)}
    hands = {'right': 'R', 'left': 'L'}
    finger = {'R': (4, 3), 'L': (4, 1)}
    for num in numbers:
        if num in (1, 4, 7):
            fing = 'L'
        elif num in (3, 6, 9):
            fing = 'R'
        else:
            l_dist = abs(finger['L'][0] - keypad[num][0]) + abs(finger['L'][1] - keypad[num][1])
            r_dist = abs(finger['R'][0] - keypad[num][0]) + abs(finger['R'][1] - keypad[num][1])
            if l_dist < r_dist:
                fing = 'L'
            elif l_dist > r_dist:
                fing = 'R'
            else:
                fing = hands[hand]
        
        answer += fing
        finger[fing] = keypad[num]
    return answer