def solution(numbers):
    answer = [0] * len(numbers)
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if (j + 1) % (i + 1) == 0:
                answer[j] += numbers[i]
    return answer


# 숫자 배열 주어지고 해당 배열 번째 소수들번째 값들의 합 반환