# 다음과 같이 import를 사용할 수 있습니다.
# import math
from collections import deque

# probably broken BFS
def solution(n, garden):
    queue = deque()
    for i in range(n):
        for j in range(n):
            if garden[i][j] == 1:
                queue.append((i, j))

    answer = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and garden[nx][ny] == 0:
                    garden[nx][ny] = 1
                    queue.append((nx, ny))
        if len(queue) == 0:
            break
        answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
