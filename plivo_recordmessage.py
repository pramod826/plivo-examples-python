#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
import plivo

app = Flask(__name__)

@app.route('/recordmessage/', methods=['GET', 'POST'])
def record_message():
    xml_response = plivo.Response()
    xml_response.addSpeak(body='Record your message after the beep. Press asterisk when done')
    #xml_response.addPlay(body='http://server/sound/file/url/')
    xml_response.addRecord(action='http://' + request.environ['SERVER_NAME'] + '/getrecording/', method='GET', maxLength=60, finishOnKey='*')
    xml_response.addSpeak(body='Recording not received')
    response = make_response(xml_response.to_xml())
    response.headers["Content-type"] = "text/xml"
    return response

@app.route('/getrecording/', methods=['GET', 'POST'])
def get_recording():
    if request.method == 'GET':
        print request.args.get('RecordUrl', '')
    elif request.method == 'POST':
        print request.form.get('RecordUrl', '')
    response = make_response('OK')
    response.headers['Content-type'] = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
