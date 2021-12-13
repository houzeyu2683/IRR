
import data

tabulation = data.tabulation(path='resource/csv/pubmed.csv')
tabulation.read()
tabulation.table.head()

vocabulary = data.vocabulary()
vocabulary.build(content=tabulation.table['abstract'], document=tabulation.table['title'])
vocabulary.compute(mode='tf-idf')

data.



