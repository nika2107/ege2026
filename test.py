from re import finditer
s = 'BADOCA'
print(r'([BCD][AO])+', s)
print(finditer(r'(?:[BCD][AO])+', s))

pattern = r'([BCD][AO])+'

matches = [match.group() for match in finditer(pattern, s)]

print(matches)
