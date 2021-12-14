
import data

tabulation = data.tabulation(path='resource/csv/pubmed.csv')
tabulation.read()
tabulation.table.head()

vocabulary = data.vocabulary(content=tabulation.table['abstract'], title=tabulation.table['title'])
vocabulary.build()
vocabulary.transform(mode='tf-idf')

importance = data.importance(vocabulary=vocabulary)
document = importance.document(top=5)

for _, item in document.iterrows():
    
    title   = item['title']
    content = tabulation.table.loc[tabulation.table['title']==title]['abstract'].item()
    sentence, _ = importance.sentence(title=title, content=content, top=3)
    data.mark(title, content, sentence)
    pass


# k = 2
# title    = document['title'][k]
# content  = tabulation.table.loc[tabulation.table['title']==title]['abstract'].item()
# sentence, _ = importance.sentence(title=title, content=content, top=5)
# mark(title, content, sentence)




# vocabulary.tokenize.sentence(tabulation.table['abstract'][1])


# extraction = data.extraction(table=tabulation.table, vocabulary=vocabulary)
# extraction.rank(what='title', top=10)

# sentence = extraction.rank(what='sentence', top=5)
# ]
# import nltk
# nltk.load('english')

# sentence[3]

