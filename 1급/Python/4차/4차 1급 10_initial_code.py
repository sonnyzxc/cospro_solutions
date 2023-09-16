#다음과 같이 import를 사용할 수 있습니다.
#import math
def get_prime(n): # very very special
    primes = [2]
    for i in range (3, n + 1, 2) :
        is_prime = True
        for j in range(2, i) :
            if i % j == 0 :
                is_prime = False
                break
        if is_prime :
            primes.append(i)
    return primes

def solution(a, b):
    # 여기에 코드를 작성해주세요.
    answer = 0
    # squared

    primes = get_prime(b)

    #제곱
    for i in primes:
        now = pow(i, 2)
        if a < now < b:
            answer += 1
    #세제곱
    for i in primes:
        now = pow(i, 3)
        if a < now < b:
            answer += 1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")