
import data

tabulation = data.tabulation(path='resource/csv/pubmed.csv')
tabulation.read()
tabulation.table.head()

vocabulary = data.vocabulary()
vocabulary.build(content=tabulation.table['abstract'], document=tabulation.table['title'])
vocabulary.transform(mode='tf-idf')

extraction = data.extraction(table=tabulation.table, vocabulary=vocabulary)
extraction.rank(what='title', top=10)

sentence = extraction.rank(what='sentence', top=5)
]




sentence[3]

