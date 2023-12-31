#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(s1, s2, p, q):
    decimal_sum = int(s1, p) + int(s2, p)
    result = ""
    while decimal_sum > 0:
        remainder = decimal_sum % q
        result = str(remainder) + result
        decimal_sum //= q
    return result

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")