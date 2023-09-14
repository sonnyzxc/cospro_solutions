#You may use import as below.
#import math

def solution(pos):
    moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
    x, y = ord(pos[0]) - ord('A') + 1, int(pos[1])
    answer = 0
    for move in moves:
        if 1 <= move[0] + x <= 8 and 1 <= move[1] + y <= 8:
            answer += 1
    
    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")