"""
    문제 : 주어진 두 개의 문자열이 서로 순열 관계에 있는지 확인하는 메서드
    *순열 관계 : 
                다른 문자열을 정렬했을 때 동일한 문자가 되는 관계
                두 문자열에서 사용된 문자는 같은데 문자의 순서만 다른 형태
"""
import unittest
from collections import Counter

# Solution_1
def check_permutation(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
         return False

# Solution_2
def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


# Solution_3
def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for c in str1:
        counter[ord(c)] += 1
    for c in str2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1  # 문자열 길이는 같지만 한 문자만 많은 경우도 존재
    return True


# Solution_4
def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False
    
    return Counter(str1) == Counter(str2)  # Counter({'d': 1, 'o': 1, 'g': 1})

print(check_permutation('hi', 'ih'))          # True
print(check_permutation('orange', 'orenge'))  # False
        
# 한 문자열에서 같은문자가 중복되어 있는 경우 고려하기