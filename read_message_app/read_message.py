'''This is a heroku hostable Application
This app gets notification from Plivo ,when message is recieved at the Plivo endpoint via msg_url
and make call to a number specified in funtion 'call' and read out the message recieved at plivo end point.
The msg_url should be given as : <heroku server adress>/msg
'''
from flask import Flask, request,make_response,Response
import plivo
import os
import urllib
app = Flask(__name__)


def call(From,Message):
    print '--------------------------At call page'
    auth_id = "XXXXXXXXXXXXXXXXX"
    auth_token = "YYYYYYYYYYYYYYYYY"
    p = plivo.RestAPI(auth_id, auth_token)

    data={}
    data['from']=From
    data['msg']=Message
    url_values=urllib.urlencode(data)
    print url_values

    params = {
      'from': 'XXXXXXXXXXX', #Your Plivo  Caller Id
      'to' : 'YYYYYYYYYY', # The end number at which the recieved message is read out
       'answer_url' : '<herokuserver_adress>/ansurl?'+url_values,
    }
    response = p.make_call(params)
    print response

@app.route('/ansurl',methods=['GET','POST'])       
def ansurl_xml():#returns answer_url xml, containing recieved message to speak at end user
    print '-----------------------At /ansurl page-------------------------'
    msg=''
    frm=''
    if request.method == 'GET':
        msg=request.args.get('msg')
        frm=request.args.get('from')
    elif request.method == 'POST':
        msg=request.form['msg']
        frm = request.form['from']
    
    print "From :", frm ,"Message: ",msg
    text='Hello Mike. I have a got a message for you.The message is sent to you by '+ frm +'.'+'Here\'s the message.'+msg
    xml=plivo.XML.Response()
    xml.addSpeak(text)
    return Response(xml.to_xml(),mimetype='text/xml')    

@app.route('/',methods=['GET','POST'])
def index():
    print "------------------At index Page---------------------------------"
    xml=plivo.XML.Response()
    xml.addSpeak("Hello, You are welcome!!!!")
    return Response(xml.to_xml(),mimetype='text/xml')

#method to retrieve data sent from plivo as notification
@app.route('/msg',methods=['POST','GET'])
def get_msg():
    print "-----------------At /msg page -----------------------------------"
    Message=''
    From=''
    if request.method== 'GET':
        print 'GET'
        From=request.args.get('From')
        Message=request.args.get('Text')
    elif request.method == 'POST':                       
        From =request.form['From']
        Message=request.form['Text']
    print From,Message
    call(From,Message)



if __name__ == '__main__':
    port = int(os.environ.get('PORT',5089))
    app.run(host='0.0.0.0' , port=port)
