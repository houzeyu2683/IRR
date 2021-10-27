

import pandas
from flask import Flask, request
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


if __name__ == "__main__":

    application.run(port=8080, debug=True)
    pass
