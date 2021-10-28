

import nltk
import pandas
import string
import re
from collections import Counter, defaultdict
from nltk.stem import PorterStemmer
 

keyword = "COVID-19"
table = pandas.read_csv("resource/csv/{}/{}.csv".format(keyword, keyword))


'''
為了實現功能中的元件，需要用一些例子來進行開發。
'''
abstract = table['abstract'][0]


'''
兩個英文單字或是字母中間如果有 '-' ，那定義為一個單字，在清除標點符號的過程要放過，其餘標點符號刪掉。 
'''
word = {}
word['origin'] = re.sub(
    "[" + re.sub("[-]", "", string.punctuation) + ']', 
    "", 
    abstract
).split()


'''
一個句子的結尾如果是 '.' 則定義為一個句子，將 '.' 以外的標點符號進行刪除，
接著使用句號來分割句子。其中最後一個句子如果包含 '.' 則會被保留下來，所以多一個程式來將其刪除。
'''
sentence = re.sub(
    "[^" + re.sub("[^.]", "", string.punctuation) + string.ascii_letters + string.whitespace + ']', 
    "", 
    abstract
).split(". ")
sentence[-1] = re.sub('[.]', '', sentence[-1])


'''
針對文字部份使用 Porter 演算法來精簡文字。
'''
porter = PorterStemmer()
word['porter'] = [porter.stem(w) for w in word['origin']]


'''
假設有兩篇文章，其中內容一模一樣，如何去統計這些文章的 word 並且進行排序，有無使用 porter 演算法要分開來計算。
'''
def convert(x, what='word list', to='dataframe'):

    if(what=='word list'):

        if(to=='dataframe'):

            table = pandas.DataFrame.from_dict(dict(Counter(x)), orient='index').reset_index()
            table.columns = ['word', 'frequency']
            pass

        pass
    
    output = table
    return(output)


count = {
    "origin" : convert(x=word['origin']),
    "porter" : convert(x=word['porter'])
}


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
print(stopwords.words('english'))
pandas.DataFrame(count['origin'])
stopword = [
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 
    'ourselves', 'you', "you're", "you've", "you'll", 
    "you'd", 'your', 'yours', 'yourself', 'yourselves', 
    'he', 'him', 'his', 'himself', 'she', 
    "she's", 'her', 'hers', 'herself', 
    'it', "it's", 'its', 'itself', 'they', 'them', 
    'their', 'theirs', 'themselves', 'what', 
    'which', 'who', 'whom', 'this', 'that', 
    "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 
    'were', 'be', 'been', 'being', 'have', 'has', 
    'had', 'having', 'do', 'does', 'did', 'doing', 
    'a', 'an', 'the', 'and', 'but', 'if', 'or', 
    'because', 'as', 'until', 'while', 'of', 'at', 
    'by', 'for', 'with', 'about', 'against', 
    'between', 'into', 'through', 'during', 'before', 
    'after', 'above', 'below', 'to', 'from', 'up', 
    'down', 'in', 'out', 'on', 'off', 'over', 'under', 
    'again', 'further', 'then', 'once', 'here', 'there', 'when', 
    'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
    'only', 'own', 'same', 'so', 'than', 'too', 'very', 
    's', 't', 'can', 'will', 'just', 'don', "don't", 'should', 
    "should've", 'now', 'd', 'll', 'm', 'o', 're', 
    've', 'y', 'ain', 'aren', "aren't", 'couldn', 
    "couldn't", 'didn', "didn't", 'doesn', "doesn't", 
    'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 
    'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', 
    "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', 
    "shouldn't", 'wasn', "wasn't", 'weren', 
    "weren't", 'won', "won't", 'wouldn', "wouldn't"
]

pandas.DataFrame()

count['origin']


word['total'] = word['porter'] + word['porter']

word['count'] = Counter(word['total'])




abstract.split()

re.sub("[^.]", "", string.ascii_letters)

# https://drive.google.com/drive/folders/167L7dQvW7Z7ox6mB_JXA8R42ng06CaxA
