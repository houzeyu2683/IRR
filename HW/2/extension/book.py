

import re
import string
import pandas
from collections import Counter
from nltk.stem import PorterStemmer


class tubulation:

    def __init__(self, path):
        
        self.path = path
        pass
    
    def read(self):

        self.table = pandas.read_csv(self.path)
        return

    pass


class article:

    def __init__(self, content):

        self.content = content
        return

    def get(self, what='word', normalization='default'):

        cache = {}
        pass

        if(what=='word'):

            '''
            兩個英文單字或是字母中間如果有 '-' ，那定義為一個單字，在清除標點符號的過程要放過，其餘標點符號刪掉。 
            '''
            pattern = "[" + re.sub("[-]", "", string.punctuation) + ']'
            cache['word'] = re.sub(pattern, "", self.content).split()
            pass

            if(normalization=='default'):

                word = cache['word']
                pass

            if(normalization=='porter'):

                porter = PorterStemmer()
                cache['word'] = [porter.stem(w) for w in cache['word']]
                word = cache['word']
                pass
            
            return(word)

        if(what=='sentence'):

            '''
            一個句子的結尾如果是 '.' 則定義為一個句子，將 '.' 以外的標點符號進行刪除，
            接著使用句號來分割句子。其中最後一個句子如果包含 '.' 則會被保留下來，所以多一個程式來將其刪除。
            '''
            pattern = "[^" + re.sub("[^.]", "", string.punctuation) + string.ascii_letters + string.whitespace + ']'
            cache['sentence'] = re.sub(pattern, "", self.content).split(". ")
            cache['sentence'][-1] = re.sub('[.]', '', cache['sentence'][-1])
            sentence = cache['sentence']
            return(sentence)

        pass

    pass


'''
假設有兩篇文章，其中內容一模一樣，如何去統計這些文章的 word 並且進行排序，有無使用 porter 演算法要分開來計算。
'''
class dictionary:

    def __init__(self, word):

        self.word = word
        return

    def convert(self, what='word', to='table'):

        if(what=='word'):

            if(to=='table'):

                table = pandas.DataFrame.from_dict(dict(Counter(self.word)), orient='index').reset_index()
                table.columns = ['word', 'frequency']
                return(table)

            pass
        
        pass

    pass
