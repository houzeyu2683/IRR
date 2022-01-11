
##  Standard packages.
import numpy
import json
import os
import io
from dotenv import dotenv_values
from flask import Flask, request
from flask.json import jsonify
from flask import render_template


##  Customized packages.

application = Flask(__name__, template_folder='./statics/templates')

@application.route("/")
def root():

    message = 'the server is running so please check the features are working or not'
    print(message)
    if(message): response = render_template("home.html")
    return(response)

@application.route("/api/search/", methods=['POST'])
def api_search():

    if(request.method=='POST'):

        message = 'call [/api/search/] function with method [post]'
        print(message)
        if(message): 

            ##  query = 'I find my skin have rash, should I go to the hospital.'
            query = request.form['query']
            print(query)
            pass

        response = 'return a json object and con'
    return(response)


import json
with open("statics/json/litcovid2BioCJSON.json", 'r') as paper:

    tmp = json.load(paper)
    pass


# 展示之前就設定一個情境，
# ex: skin vs covid-19
# 說故事，關聯性。

# @application.route("/api/v1/Upload/", methods=["POST"])
# def upload():

#     message = 'call [/api/v1/Upload/] api'
#     data = request.get_json()
#     print(message)    
#     print(data)
#     pass

#     if(message):

#         ##  Access image.
#         client = boto3.client(
#             's3', 
#             aws_access_key_id=constant['AWS_ACCESS_KEY_ID'], 
#             aws_secret_access_key=constant['AWS_SECRET_ACCESS_KEY']
#         )
#         key = data['image'].split('?')[0].replace("https://aibots.s3.amazonaws.com/", "")
#         url  = client.generate_presigned_url('get_object', Params={'Bucket': constant['AWS_STORAGE_BUCKET_NAME'], 'Key': key}, ExpiresIn=3600)
#         response = requests.get(url)
#         image = PIL.Image.open(io.BytesIO(response.content))
        
#         ##  Locate the mole center point.
#         intX, intY = yoloCroper.detect_image(image)  ##  e.g (312, 453) center point

#         ##  Detect image quality good or not.
#         x  = numpy.expand_dims(numpy.array(image.resize((224, 224))) / 255, axis=0)
#         graph = tensorflow.compat.v1.get_default_graph()
#         floatCheckImageHaveSkinScore = kerasSkinOrNotClassifier.predict(x)[:,1].item()
#         logiReject = False if(floatCheckImageHaveSkinScore>0.5) else True
#         print("logiReject", 'good')
#         ##  Response
#         response = {
#             "Reject":logiReject, 
#             "Message": "", 
#             "X": intX, 
#             "Y": intY, 
#             "CheckImageHaveSkinScore": floatCheckImageHaveSkinScore,
#             "ImageSizeScore":0
#         }
#         pass
    
#     print("response data")
#     print(response)
#     json_response = jsonify(response)
#     return(json_response)

# @application.route("/api/v1/GetRisk/", methods=["POST"])
# def risk():

#     message = 'call [/api/v1/GetRisk/] api'
#     print(message)
#     data = request.get_json()
#     print('request data')
#     print(data)
#     pass

#     if(message):

#         ##  Access image.
#         client = boto3.client(
#             's3', 
#             aws_access_key_id=constant['AWS_ACCESS_KEY_ID'], 
#             aws_secret_access_key=constant['AWS_SECRET_ACCESS_KEY']
#         )
#         key = data['image_crop'].split('?')[0].replace("https://aibots.s3.amazonaws.com/", "")
#         url  = client.generate_presigned_url('get_object', Params={'Bucket': constant['AWS_STORAGE_BUCKET_NAME'], 'Key': key}, ExpiresIn=3600)
#         response = requests.get(url)
#         image_crop = PIL.Image.open(io.BytesIO(response.content)).convert("RGB").resize((224, 224))

#         ##  Classification the risk level.
#         arrayImage = numpy.expand_dims(numpy.array(image_crop), axis=0) / 255
#         arrayVariable = process.ProcessVariable(json=data)
#         floatRiskScore = kerasRiskClassifier.predict([arrayImage, arrayVariable])[:,1].item()
#         strRiskLevel = "Higher" if(floatRiskScore>0.85) else "Lower"

#         ##  Response.
#         response = {
#             "Reject" : False,
#             "Message": "",
#             "CheckImageHaveMoleScore":0.0,
#             "RiskLevel" : strRiskLevel,
#             "RiskScore": floatRiskScore,
#             "CheckBlurScore":0.0
#         }
#         pass

#     print("response data")
#     print(response)     
#     json_response = jsonify(response)  
#     return(json_response)

if __name__ == "__main__":

    constant = dotenv_values(".environment")
    application.run(host='0.0.0.0', port=8001, debug=False, threaded=False)
    pass

