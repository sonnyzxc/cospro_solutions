#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(number, target):
    # DP (2xN tiling problem?)
    # gave up on this question
    dp = [-1]*(2*target+1)

    for i in range(1, number+1):
        dp[i] = number - i
        dp[i*2] = dp[i] + 1

    dp[number+1] = 1

    for i in range(number+2, target+1):
        min_num = min(dp[i-1]+1, dp[i//2]+1) if (i % 2 == 0) and (i//2 >= number) else dp[i-1]+1

        if dp[i+1] != -1:
            min_num = min(min_num, dp[i+1]+1)

        if dp[i] != -1:
            min_num = min(min_num, dp[i])

        dp[i] = min_num
        dp[i*2] = min_num+1

    return dp[target]

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 5
target1 = 9
ret1 = solution(number1, target1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")