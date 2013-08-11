from flask import Flask, request,make_response,Response
import plivo
import os
app = Flask(__name__)

@app.route('/getdigits',methods=['GET','POST'])
def getdigits():
    if request.method == 'GET':
        digits=request.args.get('Digits','')

    elif request.method == 'POST':
        if 'Digits' in request.form:
            digits=request.args.get('Digits','')

    xml=plivo.XML.Response()
    if digits:
        xml.addSpeak('You have Pressed '+ str(digits))
    else:
        xml.addSpeak('You have not pressd any digit')

    return Response(xml.to_xml(),mimetype='text/xml')
 

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5079))
    app.run(host='0.0.0.0' , port=port)
