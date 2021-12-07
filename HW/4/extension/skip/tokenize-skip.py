

import nltk 
import re
import string
from nltk import ngrams


'''
參數 'sentence' 是一個 list 物件，每個元素是一篇文章，
參數 'stemming' 預設 'True' ，
參數 'stopword' 預設是 'remove' 。
'''
def tokenize(sentence = 'hello word!'):

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
    word = []
    for w in sentence:

        if(w not in stopword):

            word += [w]
            pass

        pass
    
    '''
    2-gram process.
    '''
    n      = 2
    bigram = []
    for g in ngrams(word, n):

        w = '_'.join(g)
        bigram += [w]
        pass

    '''
    3-gram process.
    '''
    n      = 3
    thigram = []
    for g in ngrams(word, n):

        w = '_'.join(g)
        thigram += [w]
        pass    

    return(word, bigram, thigram)
    # sentence = 'this is a foo bar sentences and i want to ngramize it'
    # n = 2
    # sixgrams = ngrams(sentence.split(), n)
    # for grams in sixgrams:
    #     x = '_'.join(grams)    
    #     print(x)

    # x = grams
    # '_'.join(x)



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

