

import extension
from plotly.subplots import make_subplots


tabulation = extension.tabulation(path='resource/csv/data.csv')
tabulation.read()
tabulation.load(tokenize=extension.tokenize)
tabulation.split()
tabulation.build(what='dictionary')
tabulation.table['keyword'].value_counts()
machine = extension.machine(sentence=tabulation.word)
picture = {}
picture['window']    = []
picture['dimension'] = []
picture['epoch']     = []
picture['close']     = []


##  觀察 window 。
'CBOW'
machine.build(by='CBOW', window=1, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['window'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=5, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['window'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=10, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['window'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=15, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['window'] += [machine.plot(skip='color')]
"SG"
machine.build(by='SG', window=1, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['window'] += [machine.plot(skip='color')]
machine.build(by='SG', window=5, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['window'] += [machine.plot(skip='color')]
machine.build(by='SG', window=10, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['window'] += [machine.plot(skip='color')]
machine.build(by='SG', window=15, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['window'] += [machine.plot(skip='color')]
'Plot'
figure = make_subplots(rows=4, cols=2, subplot_titles=("w:1, d:50, e:5", "w:1, d:50, e:5", "w:5, d:50, e:5", "w:5, d:50, e:5", "w:10, d:50, e:5", "w:10, d:50, e:5", "w:15, d:50, e:5", "w:15, d:50, e:5"))
figure.update_layout(height=1500, width=1000, title_text="觀察 window 的影響 (左:CBOW, 右:SG)")
figure.add_trace(picture['window'][0]['data'][0], row=1, col=1)
figure.add_trace(picture['window'][1]['data'][0], row=2, col=1)
figure.add_trace(picture['window'][2]['data'][0], row=3, col=1)
figure.add_trace(picture['window'][3]['data'][0], row=4, col=1)
figure.add_trace(picture['window'][4]['data'][0], row=1, col=2)
figure.add_trace(picture['window'][5]['data'][0], row=2, col=2)
figure.add_trace(picture['window'][6]['data'][0], row=3, col=2)
figure.add_trace(picture['window'][7]['data'][0], row=4, col=2)
figure.show()


##  觀察 dimension 。
'CBOW'
machine.build(by='CBOW', window=15, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['dimension'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=15, dimension=100, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['dimension'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=15, dimension=150, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['dimension'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=15, dimension=200, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['dimension'] += [machine.plot(skip='color')]
"SG"
machine.build(by='SG', window=15, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['dimension'] += [machine.plot(skip='color')]
machine.build(by='SG', window=15, dimension=100, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['dimension'] += [machine.plot(skip='color')]
machine.build(by='SG', window=15, dimension=150, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['dimension'] += [machine.plot(skip='color')]
machine.build(by='SG', window=15, dimension=200, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['dimension'] += [machine.plot(skip='color')]
'Plot'
figure = make_subplots(rows=4, cols=2, subplot_titles=("w:15, d:50, e:5", "w:15, d:50, e:5", "w:15, d:100, e:5", "w:15, d:100, e:5", "w:15, d:150, e:5", "w:15, d:150, e:5", "w:15, d:200, e:5", "w:15, d:200, e:5"))
figure.update_layout(height=1500, width=1000, title_text="觀察 dimension 的影響 (左:CBOW, 右:SG)")
figure.add_trace(picture['dimension'][0]['data'][0], row=1, col=1)
figure.add_trace(picture['dimension'][1]['data'][0], row=2, col=1)
figure.add_trace(picture['dimension'][2]['data'][0], row=3, col=1)
figure.add_trace(picture['dimension'][3]['data'][0], row=4, col=1)
figure.add_trace(picture['dimension'][4]['data'][0], row=1, col=2)
figure.add_trace(picture['dimension'][5]['data'][0], row=2, col=2)
figure.add_trace(picture['dimension'][6]['data'][0], row=3, col=2)
figure.add_trace(picture['dimension'][7]['data'][0], row=4, col=2)
figure.show()


##  觀察 epoch 。
'CBOW'
machine.build(by='CBOW', window=15, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['epoch'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=15, dimension=50, epoch=10)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['epoch'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=15, dimension=50, epoch=15)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['epoch'] += [machine.plot(skip='color')]
machine.build(by='CBOW', window=15, dimension=50, epoch=20)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['epoch'] += [machine.plot(skip='color')]
picture['close'] += [machine.plot(skip='')]
"SG"
machine.build(by='SG', window=15, dimension=50, epoch=5)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['epoch'] += [machine.plot(skip='color')]
machine.build(by='SG', window=15, dimension=50, epoch=10)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['epoch'] += [machine.plot(skip='color')]
machine.build(by='SG', window=15, dimension=50, epoch=15)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['epoch'] += [machine.plot(skip='color')]
machine.build(by='SG', window=15, dimension=50, epoch=20)
machine.load(tokenize=extension.tokenize)
machine.collect(title=["covid-19", "diabetes", "melanoma", "hypertension", 'chest'], top=30)
machine.reduce(method="MDS", dimension=2)
picture['epoch'] += [machine.plot(skip='color')]
picture['close'] += [machine.plot(skip='')]
'Plot'
figure = make_subplots(rows=4, cols=2, subplot_titles=("w:15, d:50, e:5", "w:15, d:50, e:5", "w:15, d:50, e:10", "w:15, d:50, e:10", "w:15, d:50, e:15", "w:15, d:50, e:15", "w:15, d:50, e:20", "w:15, d:50, e:20"))
figure.update_layout(height=1500, width=1000, title_text="觀察 epoch 的影響 (左:CBOW, 右:SG)")
figure.add_trace(picture['epoch'][0]['data'][0], row=1, col=1)
figure.add_trace(picture['epoch'][1]['data'][0], row=2, col=1)
figure.add_trace(picture['epoch'][2]['data'][0], row=3, col=1)
figure.add_trace(picture['epoch'][3]['data'][0], row=4, col=1)
figure.add_trace(picture['epoch'][4]['data'][0], row=1, col=2)
figure.add_trace(picture['epoch'][5]['data'][0], row=2, col=2)
figure.add_trace(picture['epoch'][6]['data'][0], row=3, col=2)
figure.add_trace(picture['epoch'][7]['data'][0], row=4, col=2)
figure.show()


##  根據上述結論在分別從 'CBOW' 與 'SG' 挑一張比較微觀的來看。
picture['close'][0].update_layout(title_text='CBOW (w:15, d:50, e:20)').show()
picture['close'][1].update_layout(title_text='SG (w:15, d:50, e:20)').show()


##  存圖片
picture['close'][0].write_html("CBOW.html")
picture['close'][1].write_html("SG.html")



