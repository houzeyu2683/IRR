

import data
import extension


tabulation = data.tabulation(path='resource/csv/data.csv')
tabulation.read()
vocabulary = data.vocabulary()
vocabulary.build(sentence=tabulation.data['abstract'], title=tabulation.data['title'])


machine = extension.machine(vocabulary.word, vocabulary=vocabulary)
machine.build(what='model', by='SG', window=10, dimension=150, epoch=20)


machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
machine.plot(skip='').write_html("SG-plot.html")

'''
觀察二維分佈圖
相對靠近 chest 的是 tube 
相對靠近 normotens 的是 ambulatori 
相對靠近 borderlin 的是 obes 
相對靠近 pyothorax 的是 cereu 
'''

##  Term document matrix.
weight = extension.weight(matrix=vocabulary.matrix)
matrix = weight.transform(what='tfidf')


comparison = matrix.loc[(matrix.index=='chest')|(matrix.index=='tube')].sum(axis=0)
text = tabulation.data.loc[tabulation.data['title']==comparison.idxmax()]['abstract'].item()
text
vocabulary.tokenize(text)


comparison = matrix.loc[(matrix.index=='normotens')|(matrix.index=='ambulatori')].sum(axis=0)
text = tabulation.data.loc[tabulation.data['title']==comparison.idxmax()]['abstract'].item()
text
vocabulary.tokenize(text)


comparison = matrix.loc[(matrix.index=='borderlin')|(matrix.index=='obes')].sum(axis=0)
text = tabulation.data.loc[tabulation.data['title']==comparison.idxmax()]['abstract'].item()
text
vocabulary.tokenize(text)


comparison = matrix.loc[(matrix.index=='pyothorax')|(matrix.index=='cereu')].sum(axis=0)
text = tabulation.data.loc[tabulation.data['title']==comparison.idxmax()]['abstract'].item()
text
vocabulary.tokenize(text)
# numpy.dot(numpy.diag(numpy.log((vocabulary.matrix.shape[1]-1) / (vocabulary.matrix.iloc[:,1:] > 0).sum(axis=1))), vocabulary.matrix.iloc[:,1:])
# matrix = {
#     "text size" : vocabulary.matrix.shape[1],
#     'word' : vocabulary.matrix['term'],
#     'frequency' : vocabulary.matrix.iloc[:,1:]
# }
# cache = {}
# cache['tfidf'] = matrix['frequency'].copy()
# cache['idf'] = numpy.log(matrix['text size'] / (1*(cache['tfidf']>0)).sum(axis=1))









# document = data.document(title=tabulation.table['title'][0:2], sentence=tabulation.table['abstract'][0:2], vocabulary=vocabulary)
# document.build(what='matrix')
# document.matrix.shape

# document.matrix
# print('\033[2;31;43m CHEESY \033[0;0m')

# m[0]
# m[1]
# x = pandas.merge(m[0],m[1], how='outer')
# x.fillna(0)
# import pandas
# pandas.concat(m, axis=1, ).head()
# document.matrix
# from functools import reduce
# reduce(lambda x, y: pandas.merge(x, y, how='outer'), m)

# import pandas
# vocabulary.count.keys()
# term = pandas.DataFrame.from_dict(vocabulary.count, orient='index').reset_index()
# term.rename({'index':'word'})
# import pandas
# data = pandas.read_csv('resource/csv/data.csv')
# group = []
# for k in data['keyword'].unique():

#     group += [data.loc[data['keyword']==k].sample(500)]
#     print(k)
#     pass

# group = pandas.concat(group)
# group['keyword'].value_counts()
# group.to_csv('data.csv', index=False)
