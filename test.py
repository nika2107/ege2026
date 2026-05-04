import re
s = 'BADOCA'
print(re.findall(r'([BCD][AO])+', s))
print(re.findall(r'(?:[BCD][AO])+', s))
