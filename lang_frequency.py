from pprint import pprint
from collections import Counter
import re
from function import*


if __name__ == '__main__':
    NUM_POPULAR_WORDS = 10
    while True:
        print('Укажите текстовый файл для анализа, для выхода из программы введите "exit"')
        path = input()
        if path == 'exit':
            exit()
        text = load_data(path)
        if text:
            break
    get_most_frequent_words(text, NUM_POPULAR_WORDS)


