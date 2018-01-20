# 载入停用词表
#
# 主要思想是分词过后，遍历一下停用词表，去掉停用词。
import jieba


# jieba.load_userdict('userdict.txt')
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('stopWords/1893（utf8）.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


#inputs = open('input/个人聊天记录.txt', 'r', encoding='utf-8')
inputs = open('input/QQ群聊天记录.txt', 'r', encoding='utf-8')
#inputs = open('input/环境监测与环境影响评价（摘要utf8).txt', 'r', encoding='utf-8')

outputs = open('output1/a2.txt', 'w',encoding='utf-8')
for line in inputs:
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg + '\n')
outputs.close()
inputs.close()