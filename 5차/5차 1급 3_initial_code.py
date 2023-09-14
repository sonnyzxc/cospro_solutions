def solution(numbers):
    numbers.sort()
    mid = (len(numbers) - 1) // 2
    numbers[mid], numbers[len(numbers)-1] = numbers[len(numbers)-1], numbers[mid]
    left, right = mid + 1, len(numbers) - 2
    print(numbers, numbers[left], numbers[right])
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
    return numbers


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
numbers = [7, 3, 4, 1, 2, 5, 6]
ret = solution(numbers)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
