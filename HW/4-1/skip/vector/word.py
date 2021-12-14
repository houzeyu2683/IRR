import pandas
data = pandas.read_csv('resource/csv/pubmed.csv')
data = data.sample(200)
data.to_csv('./resource/pubmed-sample.csv', index=False)
