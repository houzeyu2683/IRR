

import itertools
import pandas
import tqdm
from functools import reduce
from collections import Counter


class document:

    def __init__(self, title, sentence, vocabulary):

        self.title = title
        self.sentence = sentence
        self.vocabulary = vocabulary
        return

    def build(self, what='matrix'):

        if(what=='matrix'):

            matrix = []
            total = len(self.sentence)
            for s, t in tqdm.tqdm(zip(self.sentence, self.title), total=total):

                w = self.vocabulary.tokenize(sentence=s)
                c = Counter(w)
                m = pandas.DataFrame.from_dict(c, orient='index').reset_index()
                m = m.rename(columns={'index':'word', 0:t})
                matrix += [m]
                pass
            
            self.matrix = reduce(lambda x, y: pandas.merge(x, y, how='outer'), matrix)
            self.matrix = self.matrix.fillna(0)
            pass

        return

    pass


# voc = {'word':3, "text":1, "hello":4}
# w = ['word', 'hello', 'text', 'text', 'word']
# [i for i in w]
