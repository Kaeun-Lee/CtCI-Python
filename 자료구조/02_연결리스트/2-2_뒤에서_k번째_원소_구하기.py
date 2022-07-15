test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)

def solution(list, k):
    return list[-k]

print(solution((10, 20, 30, 40, 50), 1))  # 50
print(solution((10, 20, 30, 40, 50), 5))  # 10