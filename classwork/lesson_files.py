from pprint import pprint
import string

book = open('hhgttg.txt', 'r')
content = book.read().lower()
book.close()

not_wanted_words = open('stop2.txt', 'r')
skip_words = not_wanted_words.read()
not_wanted_words.close()

skip_words = skip_words.split('\n')

words = {}
for word in content.split():
    word = word.strip(string.punctuation)
    if word not in skip_words:

        if word in words:
            words[word] += 1
        else:
            words[word] = 1

pprint(words)
