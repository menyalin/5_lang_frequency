from operator import itemgetter
from pprint import pprint


def load_data(filepath):
    import os
    if os.path.isfile(filepath):
        print("файл найден")
        f = open(filepath, 'r', encoding='utf_8')
        text = f.read()
        f.close()
        if text:
            return text
        else:
            print("Файл " + filepath + " не содержит текст")
            return False
    else:
        print("файл не найден")
        return False



def get_most_frequent_words(text, num_of_words):
    import re
    from collections import Counter
    text = text.lower()
    words = re.findall(r'\w+', text)
    counts = Counter(words)
    print('------------------------------------------------------------------------')
    print('Самые популярные слова в указанном файле и их количество:')
    pprint(counts.most_common(num_of_words))


