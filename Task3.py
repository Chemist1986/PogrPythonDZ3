# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

import re
from collections import Counter

def count_most_frequent_words(text, n):
   
    text = re.sub(r'[^\w\s]', '', text.lower())

   
    words = text.split()

    
    word_counts = Counter(words)

    
    most_common_words = word_counts.most_common(n)

    return most_common_words


input_text = """
Your large text string here...
"""

most_frequent_words = count_most_frequent_words(input_text, 10)
print("10 самых часто встречаемых слов:")
for word, count in most_frequent_words:
    print(word, "-", count)