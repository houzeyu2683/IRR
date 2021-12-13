
import pandas

class sentence:

    def __init__(self, vocabulary=None):

        self.vocabulary = vocabulary
        pass

    def split(self, x):

        # pattern  = "[" + re.sub("[-]", "", string.punctuation) + ']'
        # word = re.sub(pattern, "", x).split()
        y = x.split('.')[:-1]
        return(y)

    def evaluate(self, content=[['hello', 'world'], ['good', 'morning']], document=['book A', 'Book B']):

        '''針對給定的文章，進行斷句，將每個句子透過 tf-idf 計算對應的分數。'''
        group = []
        for c, d in zip(content, document):

            sentence = self.split(x=c)
            score = []
            for s in sentence:

                row = [self.vocabulary.term.index(k) for k in self.vocabulary.tokenize(x=s)]
                column = self.vocabulary.document.index(d)
                collection = self.vocabulary.matrix[row, column]
                score += [collection.sum()]
                pass
            
            item = pandas.DataFrame({'sentence':sentence, d:score})
            item.sort_values(d, ascending=True)
            group += [item]
            pass
        
        return(group)

    pass

