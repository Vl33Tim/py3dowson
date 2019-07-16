# printing word in random sequenses

import random

WORDS = ["PYTHON","PROGRAMMING","LINUX","LISTS","DICTIONARY","TURPLES"]
print(*WORDS)
jumbled = ""
while WORDS:
    tmp = random.choice(WORDS)
    jumbled += tmp + " "
    WORDS.remove(tmp)
print(jumbled)