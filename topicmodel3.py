import codecs

from gensim import corpora
from gensim.models import LdaModel
from gensim.corpora import Dictionary

train = []
# stopwords = codecs.open('stopWords/1893（utf8）.txt','r',encoding='utf8').readlines()
# stopwords = [ w.strip() for w in stopwords ]
fp = codecs.open('output2/a3.txt','r',encoding='utf8')
for line in fp:
    line = line.split()
    train.append([ w for w in line  ])

dictionary = corpora.Dictionary(train)
corpus = [ dictionary.doc2bow(text) for text in train ]
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5,passes=20)

for topic in lda.print_topics(num_words = 2):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')