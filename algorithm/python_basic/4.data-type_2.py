# 문자열, 문자열 연산, 슬라이싱
str1 = "I am Boy"
str2 = "NiceMan"
str3 = ''
str4 = str('')

print(len(str1), len(str2), len(str3))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = f"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
"""
문자열

멀티라인

테스트
"""
print(multi)


# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
# print(str_o3 + 3)   # type error
print('a' in str_o4)  # 할당된 문자열은 수정이 불가 (=> 순회 가능)
print('f' in str_o4)
print('z' not in str_o4)