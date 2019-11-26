import re

pattern = r"spam"# raw string

if re.match(pattern, "pamspamspam"):# match: from the begining of the string
    print("match")
else:
    print("not match")

if re.search(pattern, "pamspamspam"):
    print("match")
else:
    print("not match")

print(re.findall(pattern, "pamspamspam"))

match = re.search(pattern, "pamspamspam")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

str1 = "my name is marco"
pattern = r"marco"
newstr1 = re.sub(pattern, "jim", str1)
print(newstr1)

str2 = r"^gr.y$"# ^ start, $ end, . any
if re.match(str2, "gray"):
    print("match")

str3 = r"[aeiou]"# any one in it
if re.match(str3, "usdfhc"):
    print("matched")

str4 = r"[a-z][0-9][A-Z]"
if re.match(str4, "y4T"):
    print("still matched")

str5 = r"[^A-Z]"# invert it
if re.search(str5, "123i89"):
    print("str5 matched")

str6 = r"abc(def)*"# 0 or more
if re.match(str6, "abcsd"):
    print("str6 matched")

str7 = r"abc(def)+"# 1 or more
str7 = r"abc(def)?"# 0 or 1
str7 = r"abc(def){1, 4}"# 1 to 4 times repeat
str8 = r"(ab)(cd)(ef)(g(t)h)"
match = re.search(str8, "abcdefgthis")
if match:
    print(match.group(0))# whole matched string
    print(match.group(1))
    print(match.groups())

str9 = r"(?P<first>abc)(?:def)(ghi)"# ?: not has the group index number
match = re.search(str9, "abcdefghijk")
if match:
    print(match.group("first"))
    print(match.group(2))
    print(match.groups())

str10 = r"gr(a|e)y"# each one can be use


str11 = r"(.+)\1"# \1: match group 1.

match = re.search(str11, "abab")
if match:
    print("str11 matched")

'''
\d: [0-9] \D: not [0-9]
\s: [ \t\n\r\f\v] \S: not [ \t\n\r\f\v]
\w: [a-zA-Z0-9_] \W: not [a-zA-Z0-9_]
'''

str12 = r"^\D+\d"

match = re.match(str12, "adc 9")
if match:
    print("str12 matched")

'''
\A: beagin of an string
\Z: end of an string
\b: boundary of an word
\B: empty string
'''

str13 = r"\b(abc)\b"
match = re.search(str13, " abc ")
if match:
    print("str13 matched")

str14 = r"[\w\.-]+@[\w\.-]+\.[\w\.]+"
str15 = "please contact nie11kun@icloud.com or marco@test.com for support"
match = re.findall(str14, str15)
if match:
    print(match)

