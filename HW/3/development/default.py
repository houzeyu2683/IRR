
import extension

tabulation = extension.tabulation(path='resource/csv/data.csv')
tabulation.read()
tabulation.load(tokenize=extension.tokenize)
tabulation.split()
tabulation.build(what='dictionary')

example = [
    "The ongoing outbreak of coronavirus disease COVID-19 is significantly implicated by global heterogeneity in the genome organization of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2)."
]
tabulation.search(sentence=example[0])

machine = extension.machine(sentence=tabulation.word)
machine.build(by='CBOW')


title = [
    'covid-19', 'influenza', 
    'asthma', 'myocardial',
    'stroke', 'chest'
]
machine.model.wv.similar_by_word('my')
##  用主題去找相似字詞，找出對應字詞的向量。
##  用 tsne 降為度來畫圖  用 plotly 來畫圖。

machine.model.wv['covid-19']



tabulation.table['keyword'].unique()




from gensim.models import TfidfModel
from gensim.corpora import Dictionary
dataset = tabulation.word
dct = Dictionary(dataset)  # fit dictionary
corpus = [dct.doc2bow(line) for line in dataset]  # convert corpus to BoW format
model = TfidfModel(corpus)  # fit model
vector = model[corpus[0]]  # apply model to the first corpus document
vector[0][0]
model.id2word
dct[0]

import numpy as np
for doc in model[corpus]:

    print([[dct[id], np.around(freq, decimals=2)] for id, freq in doc])

corpus[2]

##  克漏字填充。
sentence = 'The causative [] of global in the whole.'
tabulation.search(sentence)


extension.tokenize("")




tabulation.search()
sentence = 'The [] agents of global.'
"causative"
head, tail = sentence.split('[]')

head, _, _ = extension.tokenize(head)
tail, _, _= extension.tokenize(tail)

head = head[-1]
tail = tail[0]

from collections import Counter
Counter(tabulation.bigram[0])



"heterogeneity"




'covid-19'


machine.model.predict_output_word(['It'], 2)


tabulation.bigram[0]




machine.model.wv['rich']





sentence = "The ongoing outbreak of coronavirus"

"COVID-19 is significantly implicated by global heterogeneity in the genome organization of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2)." 

answer = 'disease'
tokenize = extension.tokenize
word, bigram = tokenize(sentence)
bigram

machine.model.wv.similar_by_word(bigram[-1])



"The causative agents of global heterogeneity in the whole genome of SARS-CoV-2 are not well characterized due to the lack of comparative study of a large enough sample size from around the globe to reduce the standard deviation to the acceptable margin of error. "
"To better understand the SARS-CoV-2 genome architecture, we have performed a comprehensive analysis of codon usage bias of sixty (60) strains to get a snapshot of its global heterogeneity."
"Our study shows a relatively low codon usage bias in the SARS-CoV-2 viral genome globally, with nearly all the over-preferred codons' A.U. ended."
"We concluded that the SARS-CoV-2 genome is primarily shaped by mutation pressure; however, marginal selection pressure cannot be overlooked."
"Within the A/U rich virus genomes of SARS-CoV-2, the standard deviation in G.C. (42.91% ± 5.84%) and the GC3 value (30.14% ± 6.93%) points towards global heterogeneity of the virus."
"Several SARS-CoV-2 viral strains were originated from different viral lineages at the exact geographic location also supports this fact."
"Taking all together, these findings suggest that the general root ancestry of the global genomes are different with different genome's level adaptation to host."
"This research may provide new insights into the codon patterns, host adaptation, and global heterogeneity of SARS-CoV-2."


'''
單一克漏字填充，輸入 'sentence' 中用 '[]' 來代表想要填充的單字。
作法是根據 '[]' 前後各一個單字向量，計算最相近的單字向量集合，根據集合交集找出最有可能的單字。
'''
sentence = 'This research may provide new insights into the codon patterns, host adaptation, and global heterogeneity of SARS-CoV-2.'
answer = "insights"




head, tail = sentence.split("[]")
head = tokenize(head)[-1]
tail = tokenize(tail)[0]
if((head!=[] or tail!=[])):

    selection = {}

    selection['head'] = set([w for w, _ in machine.model.wv.most_similar(head, topn=100)])
    selection['tail'] = set([w for w, _ in machine.model.wv.most_similar(tail, topn=100)])
    set.intersection(selection['head'],selection['tail'])

head = 'publi'

tokenize(head)[-1]!=[]
tokenize(tail)


tokenize('be acer') == []
type(head)


def predict(sentence, tokenzie):

    head, tail = sentence.split("[]")
    head, tail = [head], [tail]
    tokenize(head)

tokenize = extension.tokenize

##  舉個例子來做填字情境。
head = [str(head[0])]
head = head[0]
type(head)
# import gensim
# model = gensim.models.Word2Vec(min_count=5, window=5, sg=0, vector_size=50, epochs=20, seed=0)
# model.build_vocab(tabulation.sentence)
# model.train(tabulation.sentence, total_examples=model.corpus_count, epochs=model.epochs)



# tabulation.sentence

# sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
# model = Word2Vec(min_count=1)
# model.build_vocab(sentences)  # prepare the model vocabulary
# model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)  # train word vectors
# (1, 30)


