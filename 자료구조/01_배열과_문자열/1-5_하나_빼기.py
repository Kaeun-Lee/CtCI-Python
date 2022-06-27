"""
    문제 : 문자열 두 개가 주어졌을 때, 문자열을 같게 만들기 위한 편집 횟수가 1회 이내인지 확인하는 함수
    조건 : 문자열 편집하는 방법은 1. 문자 삽입, 2. 문자 삭제, 3. 문자 교체 이다
"""

# Solution
def modify_string(str1, str2):
    cnt = 0
    if len(str1) == len(str2):      # 길이가 같으면
        for i in range(len(str1)):  # 각 단어 확인
            if str1[i] != str2[i]:
                cnt += 1 
    else:
        min_len = min(len(str1), len(str2))
        if len(str1) < len(str2):
            for i in range(min_len):
                if str1[i] not in str2:
                    cnt += 1
        else:
            for i in range(min_len):
                if str2[i] not in str1:
                    cnt += 1
    if cnt > 1:
        return False
    else:
        return  True

print(modify_string('pale', 'ple'))   # True
print(modify_string('pales', 'ple'))  # True
print(modify_string('pale', 'bale'))  # True
print(modify_string('pale', 'bake'))  # False