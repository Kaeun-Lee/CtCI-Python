"""
    문제 : 반복되는 문자의 개수를 세는 방식의 문자열 압축 메서드 ex) 'aabcccaaa' -> 'a2b1c5a3'
    조건 : '압축된' 문자열의 길이가 기존 문자열의 길이보다 길면, 기존 문자열을 반환
           문자열은 대소문자 알파벳(a~z)로만 이루어져 있음
"""

# Solution
def compress_string(input):
    temp = input[0]
    cnt = 1
    result = ''

    for i in range(1, len(input)):
        if input[i] == temp:
            cnt += 1
        else:
            result += temp + str(cnt)
            temp = input[i]
            cnt = 1
    result += temp + str(cnt)  # 가장 마지막에 남은 문자와 개수

    if len(result) > len(input):
        return input
    else:
        return result


print(compress_string('aabccccaaa'))
print(compress_string('abacacacac'))