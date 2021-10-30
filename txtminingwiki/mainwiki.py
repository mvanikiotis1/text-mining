from mediawiki import MediaWiki
from collections import Counter
import string
import pprint
from nltk.corpus.reader.semcor import SemcorCorpusReader
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from requests.models import StreamConsumedError
from thefuzz import fuzz


wikipedia = MediaWiki()
poughkeepsie = wikipedia.page("Poughkeepsie, New York")

strippables = string.punctuation + string.whitespace
content = poughkeepsie.content.lower().strip(strippables)
content = content.split()
# print(content)
# print(poughkeepsie.title)
# print(poughkeepsie.content)


def word_counter(s):
    d = {}
    for word in s:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d

# print(content)
d = word_counter(content)
# print(d.values())
sum = sum(d.values())
c = Counter(d)


# This is to remove all the irrelevant words from the content
irrelavent_words = stopwords.words('english') 
irrelavent_symbols = '===' + '=='
relevant_words = []
for word in content:
    if word not in irrelavent_words:
        if word not in irrelavent_symbols:
            relevant_words.append(word)
# print(relevant_words)


di = word_counter(relevant_words)
# print(d1)
# val = di.values()
# sum1 = sum(di.values())
c1 = Counter(di)


# This 
str_content = " ".join(content)
# print(str_content)
sentence = str_content
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)


# I used this to find the word "Culinary" so that I can use it
split_poughkeepsie = poughkeepsie.content.split()
# i = 0
# for word in split_poughkeepsie:
#     # print(word)
#     i += 1
#     if word == "Culinary":
#         print(i - 1)
culinary_word = split_poughkeepsie[266]
# print(wordnet.synsets(culinary_word))
culinary_definition = wordnet.synset('culinary.a.01').definition()


# Here I am comparing the first half of the page with the last half
first_half = split_poughkeepsie[:2024]
# print(first2000)
last_half = split_poughkeepsie[2024:]
# print(last_half)
# fuzz.token_sort_ratio(first_half, last_half)

if __name__ == '__main__':
    print(f'\nThe total number of words on this page are: {sum}\n')
    print(f'The 10 most common words on this page are: {c.most_common(10)}\n')
    print(f'The 10 most common relevant words on this page are: {c1.most_common(10)}\n')
    print(f'The Sentiment Intensivity of this text is: {score}\n')
    print('Most of the Sentiment of this page is nuetral with a positive touch\n')
    print(f'For anyone who doesnt know, The Definition of the word Culinary is: "{culinary_definition}"\n')
    print(f'The silimarity between the first half of the page, and the second half is {fuzz.token_sort_ratio(first_half, last_half)}%')