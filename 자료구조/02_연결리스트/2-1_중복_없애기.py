# Solution_1
def solution(array):
    return list(set(array))


print(solution([]))
print(solution([1, 1, 1, 1, 1, 1]))
print(solution([1, 2, 3, 2]))
print(solution([1, 2, 2, 3]))
print(solution([1, 1, 2, 3]))
print(solution([1, 2, 3]))