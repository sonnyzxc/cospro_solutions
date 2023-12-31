# 다음과 같이 import를 사용할 수 있습니다.
# import math
import itertools

def solution(card, n):
	answer = -1

	card = list(map(str, card))
	nums = list(map(''.join, itertools.permutations(card)))
	nums = sorted(list(set(map(int, nums))))

	for i in range(len(nums)):
		if n == nums[i]:
			answer = i+1

	return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 2, 1, 3]
n1 = 1312
ret1 = solution(card1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card2 = [1, 1, 1, 2]
n2 = 1122
ret2 = solution(card2, n2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")