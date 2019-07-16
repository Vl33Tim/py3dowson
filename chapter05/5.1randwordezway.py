# printing word in random sequenses

import random

WORDS = ["PYTHON","PROGRAMMING","LINUX","LISTS","DICTIONARY","TURPLES"]
print(*WORDS)
random.shuffle(WORDS)
print(*WORDS)
random.shuffle(WORDS)