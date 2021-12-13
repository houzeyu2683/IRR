
import pandas

class extraction:

    def __init__(self, table=None, vocabulary=None):

        self.table = table
        self.vocabulary = vocabulary
        pass
    
    def rank(self, what='title', top=10):

        if(what=='title'):

            pair = [engine(vocabulary=self.vocabulary).document(item) for _, item in self.table.iterrows()]
            summary = pandas.DataFrame(pair, columns=['title', "score"])
            summary = summary.sort_values(by='score', ascending=False).reset_index(drop=True).head(top)
            return(summary)

        if(what=='sentence'):

            summary = []
            group = [engine(vocabulary=self.vocabulary).sentence(item) for _, item in self.table.iterrows()]
            for g in group:

                summary += [pandas.DataFrame(g).sort_values(by='score', ascending=False).reset_index(drop=True).head(top)]

            return(summary)

        pass

    pass
#     def rank(self, what='')

#     def document(self, content='a skin skin man', title='the first artile title'):

#         token = self.vocabulary.tokenize(x=content)
#         weight = self.vocabulary.matrix[:,self.vocabulary.document.index(title)]
#         score = sum([weight[self.vocabulary.term.index(t)] for t in token])
#         return(score, title)


# x = [extraction.document(content=item['abstract'], title=item['title']) for _, item in tabulation.table.iterrows()]
# import pandas
# y = pandas.DataFrame(x, columns=['score', 'title'])
# y = y.sort_values(by='score', ascending=False).reset_index(drop=True)

class engine:

    def __init__(self, vocabulary=None):

        self.vocabulary = vocabulary
        pass

    def document(self, item):

        content = item['abstract']
        title   = item['title']
        token = self.vocabulary.tokenize(x=content)
        weight = self.vocabulary.matrix[:,self.vocabulary.document.index(title)]
        score = sum([weight[self.vocabulary.term.index(t)] for t in token])
        return(title, score)

    def sentence(self, item):

        group = {item['title']:[], 'score':[]}
        for s in item['abstract'].split("."):

            if(s==''): continue

            token = self.vocabulary.tokenize(s)
            weight = self.vocabulary.matrix[:,self.vocabulary.document.index(item['title'])]
            # score = sum([weight[self.vocabulary.term.index(t)] for t in token])
            w = []
            for t in token:

                try:

                    w += [weight[self.vocabulary.term.index(t)]]
                    pass

                except:

                    continue

                pass

            score = sum(w)
            group[item['title']] += [s]
            group['score'] += [score]
            pass
        
        return(group)

    pass

    # def evaluate(self, content=[['hello', 'world'], ['good', 'morning']], document=['book A', 'Book B']):

    #     '''針對給定的文章，進行斷句，將每個句子透過 tf-idf 計算對應的分數。'''
    #     group = []
    #     for c, d in zip(content, document):

    #         sentence = self.split(x=c)
    #         score = []
    #         for s in sentence:

    #             row = [self.vocabulary.term.index(k) for k in self.vocabulary.tokenize(x=s)]
    #             column = self.vocabulary.document.index(d)
    #             collection = self.vocabulary.matrix[row, column]
    #             score += [collection.sum()]
    #             pass
            
    #         item = pandas.DataFrame({'sentence':sentence, d:score})
    #         item.sort_values(d, ascending=True)
    #         group += [item]
    #         pass
        
    #     return(group)

    # pass

