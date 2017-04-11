import os
import re
from collections import Counter
from pprint import pprint


def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file_handler:
            return file_handler.read()


def get_most_frequent_words(text, num_of_words):
    text_tmp = text.lower()
    words = re.findall(r'\w+', text_tmp)
    counts = Counter(words)
    return counts.most_common(num_of_words)


if __name__ == '__main__':
    NUM_POPULAR_WORDS = 10
    file_path = input("Select data file:")
    text = load_data(file_path)
    if not text:
        print('File not exists!')
        exit()
    print('The most popular words in the text and their count:')
    pprint(get_most_frequent_words(text, NUM_POPULAR_WORDS))
