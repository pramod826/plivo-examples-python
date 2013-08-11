#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, make_response
import plivo

app = Flask(__name__)

@app.route('/recordmessage/', methods=['GET', 'POST'])
def record_message():
    response = plivo.XML.Response()
    response.addSpeak(body='Record your message after the beep. Press asterisk when done')
    #xml_response.addPlay(body='http://server/sound/file/url/')
    response.addRecord(action='http://' + request.environ['SERVER_NAME'] + '/getrecording/', method='GET', maxLength=60, finishOnKey='*')
    response.addSpeak(body='Recording not received')
    xml_response = Response(response.to_xml(),mimetype='text/xml')
    return xml_response

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
