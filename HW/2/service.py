

import extension


import pandas
import numpy
from flask import Flask, request
from plotly.io import to_html
from plotly import express as plotly
from plotly.subplots import make_subplots


application = Flask(__name__)


@application.route("/", methods=['GET'])
def root():

    message = '這是資訊檢索作業的首頁。'
    return(message)


@application.route("/table", methods=['GET'])
def table():
    
    if(request.method=='GET'):

        table = pandas.read_csv('resource/csv/group.csv')
        pass
    
    table = table.to_html()
    return(table)


@application.route("/plot", methods=['GET'])
def plot():

    if(request.method=='GET'):

        tubulation = extension.tubulation(path="resource/csv/data.csv")
        tubulation.read()
        tubulation.table.dropna(subset=['abstract'], inplace=True)
        pass

        size = request.values.get('size')
        if(size):

            print("找到 size 值，將會使用 {} 篇文本資料。".format(size))
            selection = tubulation.table.sample(int(size), random_state=0)
            pass

        else:

            print("找不到 size 值，將使用全部的文本。")
            size = len(tubulation.table)
            selection = tubulation.table
            pass

        top = request.values.get('top')
        if(top):

            print("找到 top 值，會將頻率最高的 {} 個單字進行畫圖。".format(top))
            top = int(top)
            pass

        else:

            print("找不到 top 值，使用預設值，會將頻率最高的 100 個單字進行畫圖。")
            top = 100
            pass

        content = " ".join(selection['abstract'].tolist())
        article = extension.article(content=content)
        pass

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
        pass

        picture = {
            "default":plotly.bar(table['default'].head(top), x='word', y='frequency', labels=dict(word="")),
            "porter":plotly.bar(table['porter'].head(top), x='word', y='frequency', labels=dict(word="")),
            "log default":plotly.bar(table['default'].head(top), x='word', y='log frequency', labels=dict(word="")),
            "log porter":plotly.bar(table['porter'].head(top), x='word', y='log frequency', labels=dict(word=""))
        }
        figure = make_subplots(rows=1, cols=4, subplot_titles=("計算 word 頻率", "計算 word 頻率 by porter 演算法", "log( 計算 word 頻率 )", "log( 計算 word 頻率 by porter 演算法 )"))
        figure.add_trace(picture["default"]['data'][0], row=1, col=1)
        figure.add_trace(picture["porter"]['data'][0], row=1, col=2)
        figure.add_trace(picture["log default"]['data'][0], row=1, col=3)
        figure.add_trace(picture["log porter"]['data'][0], row=1, col=4)
        figure.update_layout(height=500, width=1500, title_text="用 {} 篇的摘要，挑選頻率最高的 {} 個 word 來畫圖。".format(size, top))
        response = to_html(figure)
        return(response)

    pass


if __name__ == "__main__":

    application.run(port=8080, debug=True)
    pass
