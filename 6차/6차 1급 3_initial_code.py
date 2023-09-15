#다음과 같이 import를 사용할 수 있습니다.
#import math
import itertools

def solution(arr, K):
	answer = 10001
	list_a = list(itertools.combinations(arr, K))

	for nums in list_a:
		list_nums = list(set(nums))
		max_n, min_n = max(list_nums), min(list_nums)
		rtn = max_n - min_n
		if rtn < answer:
			answer = rtn
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")