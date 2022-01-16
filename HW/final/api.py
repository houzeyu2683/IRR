
import pandas
import math
import text

'''
根據給定的關鍵字（Subject-X）來計算文本的分數，
用來排序呈現檢索結果。
'''

class detail:

    def __init__(self, score=None, content=None, sentence=None, similar=None):

        self.score = score
        self.content = content
        self.sentence = sentence
        self.similar = similar
        return
        
    pass

def search_with_subject(search='rash', top=5):

    vocabulary = text.vocabulary()
    embedding = text.embedding()
    pass

    information = pandas.read_csv("./information.csv")
    vocabulary.load(what='frequency matrix', path='./frequency matrix.csv')
    embedding.load(path='./vector.model')
    search = vocabulary.tokenize(content=search, to='word')[0]
    pass

    # search = 'rash'
    # top = 5
    # pass

    weight = vocabulary.get('ntf-idf')
    rank = information.copy()
    similar_list = embedding.model.wv.similar_by_word(search,top)
    similar_word = [k for k, _ in similar_list]
    for k in [(search, 1)] + similar_list:

        w,s = k
        weight[vocabulary.term.index(w),:] = weight[vocabulary.term.index(w),:] * (math.exp(5)*s)
        pass

    rank['score'] = weight.sum(0)
    rank = rank.sort_values(['score'], ascending=False).head(top).copy()

    '''
    對於每篇文章，去找出訊息量較多的句子，多少句子是參數。
    '''

    output = []
    for index, item in rank.iterrows():

        d = detail(
            score=item["score"], 
            content=item['abstract'], 
            sentence={},
            similar = set()
            )
        for s in vocabulary.tokenize(d.content, 'sentence'):
            
            r = [vocabulary.term.index(i) for i in vocabulary.tokenize(s, 'word')]
            d.sentence.update({s:weight[r,index].sum()})
            d.similar.update(set.intersection(set([vocabulary.term[i] for i in r]), set(similar_word)))
            pass
        
        output.append({item['title_e']:d})
        pass    
    
    return(output, rank)

rank_detail, _ = search_with_subject(search='organization', top=5)

for i in rank_detail:
    for k, v in i.items():
        # print(i[k].content)
        print(i[k].score)
        print(i[k].sentence)
        print(i[k].similar)
        pass
    pass