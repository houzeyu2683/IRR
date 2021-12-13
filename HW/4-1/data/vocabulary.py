
import nltk 
import re
import string
import itertools
import tqdm
import pandas
import functools
import numpy
from collections import Counter

class vocabulary:

    def __init__(self):
        
        return

    def build(self, content=[['hello', 'world'], ['good', 'morning']], document=['book A', 'Book B']):

        '''Build term document matrix.'''
        total  = len(content)
        matrix = []
        word   = []
        for s, d in tqdm.tqdm(zip(content, document), total=total):

            w = self.tokenize(x=s)
            c = Counter(w)
            m = pandas.DataFrame.from_dict(c, orient='index').reset_index().rename(columns={'index':'term', 0:d})
            word   += [w]
            matrix += [m]
            pass
        
        matrix = functools.reduce(lambda x, y: pandas.merge(x, y, how='outer'), matrix).fillna(0)
        self.term      = matrix.term.tolist()
        self.document  = matrix.columns.tolist()[1:]
        frequency = matrix.iloc[:,1:].to_numpy()
        if(True): frequency = (frequency / frequency.sum(axis=0))
        self.frequency = frequency
        return

    def tokenize(self, x='hello word!'):

        pattern  = "[" + re.sub("[-]", "", string.punctuation) + ']'
        word = re.sub(pattern, "", x).split()
        pass

        ##  Stemming with porter method.
        stemming = True
        if(stemming):

            porter = nltk.stem.PorterStemmer()
            word = [porter.stem(w) for w in word]
            pass

        ##  Remove stopword.
        if(True):

            collection = []
            for w in word:

                if(w not in stopword):

                    collection += [w]
                    pass

                pass
            
            word = collection
            pass

        return(word)

    def transform(self, mode='tf-idf'):

        if(mode=='tf-idf'):

            matrix = numpy.dot(
                self.frequency.transpose(), 
                numpy.diag(numpy.log(self.frequency.shape[1] / (self.frequency > 0).sum(axis=1)))
            )
            matrix = matrix.transpose()
            self.matrix = matrix.round(2)
            pass
        
        print('use [self.matrix] to call the weight matrix')
        return

    pass

stopword = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself",
    "she", "her", "hers", "herself", "it", "its", "itself", "they", 
    "them", "their", "theirs", "themselves", "what",
    "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", 
    "being", "have", "has", "had", "having", "do", "does", "did", "doing", 
    "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", 
    "into", "through", "during", "before", "after", "above", "below", "to", 
    "from", "up", "down", "in", "out", "on", "off", "over", "under", 
    "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
    "any","both","each","few","more","most","other","some","such",
    "no","nor","not","only","own","same","so","than", "too", 
    "very", "s", "t", "can", "will", "just", "don", "should", "now"
}





