

import nltk 
import re
import string
import itertools
import tqdm
import pandas
import functools
from collections import Counter


class vocabulary:

    def __init__(self):
        
        return

    def build(self, sentence, title):

        '''Build term document matrix.'''
        total  = len(sentence)
        matrix = []
        word   = []
        for s, t in tqdm.tqdm(zip(sentence, title), total=total):

            w = self.tokenize(sentence=s)
            c = Counter(w)
            m = pandas.DataFrame.from_dict(c, orient='index').reset_index().rename(columns={'index':'term', 0:t})
            word   += [w]
            matrix += [m]
            pass
        
        self.word   = word
        self.matrix = functools.reduce(lambda x, y: pandas.merge(x, y, how='outer'), matrix).fillna(0)
        pass

        # self.count = Counter(list(itertools.chain(*w)))
        return

    def tokenize(self, sentence='hello word!'):

        '''
        兩個英文單字或是字母中間如果有 '-' ，那定義為一個單字，在清除標點符號的過程要忽略，其餘標點符號刪掉。 
        '''
        pattern  = "[" + re.sub("[-]", "", string.punctuation) + ']'
        sentence = re.sub(pattern, "", sentence).split()

        '''
        Stemming with porter method.
        '''
        stemming = True
        if(stemming):

            porter = nltk.stem.PorterStemmer()
            sentence = [porter.stem(w) for w in sentence]
            pass

        '''
        Remove stopword.
        '''
        if(True):

            word = []
            for w in sentence:

                if(w not in stopword):

                    word += [w]
                    pass

                pass
            
            pass

        return(word)

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





