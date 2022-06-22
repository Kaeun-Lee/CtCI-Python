"""
    문제 : 문자열에 들어있는 모든 공백을 '%20'으로 바꿔주는 메서드
"""

# Solution
def change_url(str):
    result = str.replace(" ", "%20")
    return result

print(change_url("Mr John Smith"))