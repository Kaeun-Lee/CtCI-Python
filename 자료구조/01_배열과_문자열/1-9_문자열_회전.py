# 한 단어가 다른 문자열에 포함되어 있는지 판멸하는 메서드

# 우리가 해결할 것 : 문자열이 있을 때 s2는 s1을 회전시킨 결과인지 판별
# 메서드를 한 번만 호출해서 판별


# 해결할 것부터
# 회전시킨 걸 어떻게 알지?
# 얼만큼 회전될 걸 어떻게 알까? 
s1 = 'waterbottle'
s2 = 'erbottlewat'

for i in range(len(s1)):
    if s1[i] in s2:
        print(s2.index(s1[i]))

