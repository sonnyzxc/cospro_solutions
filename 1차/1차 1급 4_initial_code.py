#You may use import as below.
#import math

def solution(num):
    return int(str(num+1).replace('0','1'))


#The following is code to output testcase.
num = 9949999
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")