

import pandas
from flask import Flask, request
from plotnine.geoms import geom_bar
application = Flask(__name__)


@application.route("/", methods=['GET'])
def root():

    message = '作業演示界面'
    return(message)


@application.route("/table", methods=['GET'])
def table():
    
    if(request.method=='GET'):

        keyword = request.values.get('keyword')
        table = pandas.read_csv('resource/csv/{}/{}.csv'.format(keyword, keyword))
        pass
    
    table = table.to_html()
    return(table)


@application.route("/distribution", methods=['GET'])
def distribution():

    if(request.method=='GET'):

        keyword = request.values.get('keyword')
        table = pandas.read_csv('resource/csv/{}/{}.csv'.format(keyword, keyword))
        
        pass

    return


import io
import base64
from plotnine import ggplot, aes
@application.route('/plot')
def build_plot():

    img = io.BytesIO()

    y = [1,2,3,4,5]
    x = [0,2,1,3,4]
    plot = ggplot(aes(x,y)) + geom_bar()
    return(plot)


if __name__ == "__main__":

    application.run(port=8080, debug=True)
    pass
