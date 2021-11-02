

import extension


import asyncio
import os
import Levenshtein
import datetime
import pandas
import numpy
import tqdm
from flask import Flask, request
from flask import send_from_directory
from plotly.io import to_html
from plotly import express as plotly
from plotly.subplots import make_subplots


application = Flask(__name__)


@application.route("/", methods=['GET'])
def root():

    message = '這是資訊檢索作業二的首頁。'
    return(message)


@application.route('/favicon.ico') 
def favicon():

    response = send_from_directory(
        os.path.join(application.root_path, 'static'), 
        'favicon.ico', 
        mimetype='image/vnd.microsoft.icon'
    ) 
    return(response)


@application.route("/table", methods=['GET'])
def table():
    
    if(request.method=='GET'):

        table = pandas.read_csv('resource/csv/data.csv')
        pass
    
    table = table.to_html()
    return(table)


@application.route("/plot", methods=['GET'])
def plot():

    if(request.method=='GET'):

        start = datetime.datetime.now()


        size = request.values.get('size')
        if(size):

            print("找到 size 值，將會使用 {} 篇文本資料。".format(size))
            size = int(size)
            if(size in [1000, 5000, 10000, 50000]):

                print("載入事前整理好的 word frequency 表。")
                table = {}
                table['default'] = pandas.read_csv("resource/csv/frequency/{}/default.csv".format(size))
                table['porter'] = pandas.read_csv("resource/csv/frequency/{}/porter.csv".format(size))
                pass
            
            else:

                if(size>=50000):

                    print('指定數量超過上限，使用 50000 篇文章。')
                    size = 50000
                    table = {}
                    table['default'] = pandas.read_csv("resource/csv/frequency/{}/default.csv".format(size))
                    table['porter'] = pandas.read_csv("resource/csv/frequency/{}/porter.csv".format(size))
                    pass
                
                else:

                    print('指定數量沒有超過上限。')
                    print("事前沒有整理，針對指定的 size 進行處理，生成 word frequency 表。")
                    tubulation = extension.tubulation(path="resource/csv/data.csv")
                    tubulation.read()
                    tubulation.table.dropna(subset=['abstract'], inplace=True)
                    selection = tubulation.table.sample(size, random_state=0)
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
                    pass

                pass

            pass

        else:

            print("找不到 size 值，使用 50000 篇文章。")
            size = 50000
            table = {}
            table['default'] = pandas.read_csv("resource/csv/frequency/{}/default.csv".format(size))
            table['porter'] = pandas.read_csv("resource/csv/frequency/{}/porter.csv".format(size))
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

        end = datetime.datetime.now()
        time = (end-start).seconds

        ##  畫圖。
        print("table['default'] word size: {}".format(len(table['default'])))
        print("table['porter'] word size: {}".format(len(table['porter'])))
        picture = {
            "default":plotly.bar(table['default'].head(top), y='frequency', x='word', labels=dict(word="")),
            "porter":plotly.bar(table['porter'].head(top), y='frequency', x='word', labels=dict(word="")),
            "log default":plotly.bar(table['default'].head(top), y='log frequency', x='word', labels=dict(word="")),
            "log porter":plotly.bar(table['porter'].head(top), y='log frequency', x='word', labels=dict(word=""))
        }
        title = (
            "計算 word 頻率", "計算 word 頻率 by porter 演算法", 
            "log( 計算 word 頻率 )", "log( 計算 word 頻率 by porter 演算法 )"
        )
        figure = make_subplots(rows=1, cols=4, subplot_titles=title)
        figure.add_trace(picture["default"]['data'][0], row=1, col=1)
        figure.add_trace(picture["porter"]['data'][0], row=1, col=2)
        figure.add_trace(picture["log default"]['data'][0], row=1, col=3)
        figure.add_trace(picture["log porter"]['data'][0], row=1, col=4)
        # figure.update_layout(height=500, width=1500, title_text="用 {} 篇的摘要，挑選頻率最高的 {} 個 word 來畫圖。（載入時間：{}秒）".format(size, top, time))
        figure.update_layout(height=500, width=1500, title_text="用 {} 篇的摘要，挑選頻率最高的 {} 個 word 來畫圖。".format(size, top))
        response = to_html(figure)
        return(response)

    pass


@application.route("/search", methods=['GET'])
def search():
    
    if(request.method=='GET'):

        word = request.values.get('word')
        if(word==None):

            response = "請輸入想要搜尋的字（英文）。"
            return(response)

        top = request.values.get('top')
        if(top==None):

            top = 100
            pass
        
        else:

            top = int(top)
            pass
        
        '''
        沒有平行執行，待修復。
        '''
        # @asyncio.coroutine
        # def thread(word, top, size):
        #     # size = 1000
        #     table = {
        #         'default':pandas.read_csv("resource/csv/frequency/{}/default.csv".format(size), na_filter = False),
        #         'porter':pandas.read_csv("resource/csv/frequency/{}/porter.csv".format(size), na_filter = False)
        #     }
        #     group = {
        #         'default word({}text)'.format(size):[],
        #         'score({}text)'.format(size):[]
        #     }    
        #     for _, item in table['default'].iterrows():

        #         group['default word({}text)'.format(size)] += [item['word']]
        #         group['score({}text)'.format(size)] += [Levenshtein.distance(word, item['word'])]
        #         pass

        #     group = pandas.DataFrame(group).sort_values('score({}text)'.format(size)).reset_index(drop=True)    
        #     group = group.head(top)
        #     return(group)

        # # loop = asyncio.get_event_loop()
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # task = thread(word, top, size=50000), thread(word, top, size=10000), thread(word, top, size=5000), thread(word, top, size=1000)
        # group = loop.run_until_complete(asyncio.gather(*task))
        # summary = [g for g in group]
        # # print("func_normal()={a}, func_infinite()={b}".format(**vars()))
        # loop.close()

        size = [1000, 5000, 10000, 50000]
        summary = []
        for s in size:

            table = {
                'default':pandas.read_csv("resource/csv/frequency/{}/default.csv".format(s), na_filter = False),
                'porter':pandas.read_csv("resource/csv/frequency/{}/porter.csv".format(s), na_filter = False)
            }
            group = {
                'default word({}text)'.format(s):[],
                'score({}text)'.format(s):[]
            }
            for _, item in tqdm.tqdm(table['default'].iterrows(), total=len(table['default'])):

                group['default word({}text)'.format(s)] += [item['word']]
                group['score({}text)'.format(s)] += [Levenshtein.distance(word, item['word'])]
                pass

            group = pandas.DataFrame(group).sort_values('score({}text)'.format(s)).reset_index(drop=True)
            summary += [group.head(top)]
        pass

        summary = pandas.concat(summary,axis=1)
        response = summary.to_html()
        return(response)
    
    pass


if __name__ == "__main__":

    application.run(port=8080, debug=True)
    pass
