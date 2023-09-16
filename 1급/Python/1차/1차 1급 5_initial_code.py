#You may use import as below.
#import math

def solution(n):
    # Write code here.
    answer = 0
    c = 0
    for x in range(1, n*n + 1, n):
        temp = [y for y in range(x, x + n)]
        if c % 2 == 1:
            answer += temp[len(temp) - 1 - c]
        else:
            answer += temp[c]
        c += 1
    return answer
#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")