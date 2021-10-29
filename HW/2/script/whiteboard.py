

import extension
import numpy
from plotly.io import to_html
from plotly import express as plotly
from plotly.subplots import make_subplots


tubulation = extension.tubulation(path="resource/csv/data.csv")
tubulation.read()
tubulation.table.dropna(subset=['abstract'], inplace=True)


size = 1000
if(size):

    selection = tubulation.table.sample(size, random_state=0)
    pass

else:

    selection = tubulation.table
    pass


content = " ".join(selection['abstract'].tolist())
article = extension.article(content=content)


dictionary = {
    'default':extension.dictionary(word=article.get(what='word', normalization='default')),
    'porter':extension.dictionary(word=article.get(what='word', normalization='porter'))
}
table = {
    'default':dictionary['default'].convert(what='word', to='table'),
    'porter':dictionary['porter'].convert(what='word', to='table')
}
table['default']['log frequency'] = numpy.log(table['default']['frequency'])
table['porter']['log frequency'] = numpy.log(table['porter']['frequency'])


top = 200
picture = {
    "default":plotly.bar(table['default'].head(top), x='word', y='frequency', labels=dict(word="")),
    "porter":plotly.bar(table['porter'].head(top), x='word', y='frequency', labels=dict(word="")),
    "log default":plotly.bar(table['default'].head(top), x='word', y='log frequency', labels=dict(word="")),
    "log porter":plotly.bar(table['porter'].head(top), x='word', y='log frequency', labels=dict(word=""))
}
figure = make_subplots(rows=1, cols=4, subplot_titles=("計算 word 頻率", "使用 porter 演算法計算 word 頻率", "log( 計算 word 頻率 )", "log( 使用 porter 演算法計算 word 頻率 )"))
figure.add_trace(picture["default"]['data'][0], row=1, col=1)
figure.add_trace(picture["porter"]['data'][0], row=1, col=2)
figure.add_trace(picture["log default"]['data'][0], row=1, col=3)
figure.add_trace(picture["log porter"]['data'][0], row=1, col=4)
figure.update_layout(height=500, width=1500, title_text="用 {} 篇的摘要，挑選頻率最高的 {} 個 word 來畫圖。".format(size, top))
html = to_html(figure)
figure.show()

