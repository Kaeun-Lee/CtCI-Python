"""
    문제 : 주어진 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘
    조건 : 자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘
"""

# Solution_1
def check_duplication(str):
    dict = {}

    for i in str:
        if i not in dict:
            dict[i] = 0
        else:
            return True
    return False


print(check_duplication('44'))   # True
print(check_duplication('117'))  # True
print(check_duplication('132'))  # False