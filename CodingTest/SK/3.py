def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return (n * factorial(n - 1))

def solution(width, height, diagonals):
    answer = 0
    for i in diagonals:
        answer += ((factorial(i[0] + i[1] - 1) // (factorial(i[0] - 1) * factorial(i[1])))*
        (factorial(width + height - i[0] - i[1] + 1) // (factorial(width - i[0]) * factorial(height - i[1] + 1)))) % 10000019
        answer += ((factorial(i[0] + i[1] - 1) // (factorial(i[0]) * factorial(i[1] - 1)))*
        (factorial(width + height - i[0] - i[1] + 1) // (factorial(width - i[0] + 1) * factorial(height - i[1])))) % 10000019
    return answer % 10000019