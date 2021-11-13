

import pandas, tqdm
import itertools
from collections import Counter
import re


class tabulation:

    def __init__(self, path):

        self.path = path
        pass
    
    def read(self):

        self.table = pandas.read_csv(self.path).sample(200, random_state=0)
        pass

    def load(self, tokenize=None):

        self.tokenize = tokenize
        return

    def split(self):

        if(self.tokenize):

            total = len(self.table)
            word = []
            bigram = []
            thigram = []
            for s in tqdm.tqdm(self.table['abstract'], total=total, leave=False):

                w, b, t = self.tokenize(sentence=s)
                word += [w]
                bigram += [b]
                thigram += [t]
                pass

            self.word = word
            self.bigram = bigram
            self.thigram = thigram
            pass
        
        else:

            print("The tokenizer function not found.")
            pass

        pass

    def build(self, what='dictionary'):

        if(what=='dictionary'):

            count = Counter(list(itertools.chain(*self.word, *self.bigram, *self.thigram)))
            dictionary = pandas.DataFrame.from_dict(count, orient='index').reset_index()
            dictionary.columns = ['word', 'frequency']
            self.dictionary = dictionary
            pass

        return
    
    def search(self, sentence):
        # sentence = "in the whole genome of SARS-CoV-2 []"
        head, tail = sentence.split("[]")
        head, _, _ = self.tokenize(head)
        tail, _, _ = self.tokenize(tail)
        head = head[-1] + '_' if(head!=[]) else None
        tail = tail[0] + '_' if(tail!=[]) else None
        pass

        index = []
        for w in tqdm.tqdm(self.dictionary['word'], leave=False):

            if(head):

                if(head in w):

                    w = re.sub(head, "", w)
                    index += [w]
                    pass

                pass

            if(tail):

                if(tail in w):

                    w = re.sub(tail, "", w)
                    index += [w]
                    pass

                pass

            pass

        count = Counter(index)
        result = pandas.DataFrame.from_dict(count, orient='index').reset_index()
        result.columns = ['word', 'count']
        result = result.sort_values(by=['count'], ascending=False).head(10)
        return(result)

    pass



# head = 'how' + '_'
# tail = "_" + 'you'


# word = [['how', 'are', 'you'],['fine', 'and', "you"],['how_are', 'are_you']]
# bi = [['how', 'are', 'you'],['fine', 'and', "you"],['how_are', 'are_you']]
# count = Counter(list(itertools.chain(*word, *bi)))
# dictionary = pandas.DataFrame.from_dict(count, orient='index').reset_index()
# dictionary.columns = ['word', 'frequency']






# pandas.DataFrame()




