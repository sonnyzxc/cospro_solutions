#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(K, words):
	answer = 1
	rest_len = K
	is_first = True
	for word in words:
		if is_first:
			length = len(word)
		else:
			length = len(word) + 1

		if 0<= rest_len - length <= K:
			rest_len -= length
			is_first = False
		else:
			answer += 1
			rest_len = K-length
			is_first = True

	return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")