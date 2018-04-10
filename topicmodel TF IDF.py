import jieba, os
from gensim import corpora, models, similarities

train_set = []

walk = os.walk('output1')
for root, dirs, files in walk:
    for name in files:
        f = open(os.path.join(root, name), 'r',encoding='UTF-8')
    raw = f.read()
    word_list = list(jieba.cut(raw, cut_all = False))
    train_set.append(word_list)


dic = corpora.Dictionary(train_set)
corpus = [dic.doc2bow(text) for text in train_set]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lda = models.LdaModel(corpus_tfidf, id2word = dic, num_topics = 10)
corpus_lda = lda[corpus_tfidf]

for topic in lda.print_topics(num_words = 5):
    termNumber = topic[0]
    print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    for term in listOfTerms:
        listItems = term.split('*')
        print('  ', listItems[1], '(', listItems[0], ')', sep='')