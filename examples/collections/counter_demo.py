from collections import Counter

cnt = Counter(red=10, blue = 20)
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)

cnt2 = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(cnt2)

# Count tokens
st = """Python is a fascinating language. It is a general purpose language used for all purposes.
A language is to be flexible and powerful. Python is popular. Python is awesome 
Python 3.9 is latest
"""

import re
words = re.findall(r'\w+', st)
word_count = Counter(words)
print(word_count)
print(word_count.most_common(5))