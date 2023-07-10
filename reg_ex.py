import re

pattren=re.compile(r'very bad|horrible|worst')

print(re.findall(pattren,"this is shit and horrible"))