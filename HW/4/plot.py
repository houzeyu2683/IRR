
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


