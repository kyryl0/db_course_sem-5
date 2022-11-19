import pymorphy2
from collections import defaultdict
import string
words = defaultdict(list)

morph = pymorphy2.MorphAnalyzer(lang='uk')

with open('kaydasheva-simia.txt', 'r', encoding= 'utf-8') as f:
    text = f.read()

for i in text:
    if i in string.punctuation:
        text = text.replace(i, '')

for w in text.lower().split():
    words[morph.parse(w)[0].normal_form] = (morph.parse(w)[0].tag.POS, [inf[0] for inf in morph.parse(w)[0].lexeme])


