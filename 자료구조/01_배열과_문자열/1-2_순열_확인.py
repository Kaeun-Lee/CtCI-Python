"""
    문제 : 주어진 두 개의 문자열이 서로 순열 관계에 있는지 확인하는 메서드
    *순열 관계 : 
                다른 문자열을 정렬했을 때 동일한 문자가 되는 관계
                두 문자열에서 사용된 문자는 같은데 문자의 순서만 다른 형태
"""

def check_permutation(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
         return False


print(check_permutation('hi', 'ih'))          # True
print(check_permutation('orange', 'orenge'))  # False
        
# 한 문자열에서 같은문자가 중복되어 있는 경우 고려하기