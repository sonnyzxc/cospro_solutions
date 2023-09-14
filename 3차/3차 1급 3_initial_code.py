#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    #여기에 코드를 작성해주세요.
    MAX_PLACES = 64
    visited = []

    for pos in [[ord(x) - ord('A') + 1, int(y)] for x, y in bishops]:
        attack_range = [
            f"{chr(x + ord('A') - 1)}{y}"
            for x in range(1, 9)
            for y in range(1, 9)
            if abs(pos[0] - x) == abs(pos[1] - y)
        ]
        visited.extend(attack_range)
    return MAX_PLACES - len(set(visited))

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")