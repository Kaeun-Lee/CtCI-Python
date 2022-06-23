"""
    문제 : 주어진 문자열이 회문(palindrome)의 순열인지 아닌지 확인하는 함수
    조건 : 회문이 꼭 사전에 등장하는 단어가 아니어도 됨
*회문 : 앞으로 읽으나 뒤로 읽으나 같은 단어 혹은 구절을 의미 -> 홀수번 반복되는 문자가 1개 or 0개
*순열 : 문자열을 재배치하는 것    
"""

# Solution
def check_palindrome_permutation(str):
    a = str.lower()  
    a = a.replace(' ', '')  # 공백 제거

    dict = {}
    cnt = 0

    for i in range(len(a)):
        if a[i] not in dict:
            dict[a[i]] = 1
        else:
            dict[a[i]] += 1

    for i in dict.values():
        if i % 2 != 0:
            cnt += 1

    if cnt > 1:
        return False
    else:
        return True
    

print(check_palindrome_permutation('Tact Coa'))