#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Above line is to confirm that unicode Non-ASCII charcters would be included
## in this file
#

from flask import Flask, request, make_response
import plivo
import os
import sys

app = Flask(__name__)

@app.route('/getdigits/', methods=['GET', 'POST'])
def getdigits():
    if request.method == 'GET':
        digits = request.args.get('Digits', '')
    elif request.method == 'POST':
        digits = request.form.get('Digits', '')
    
    resp = plivo.Response()
    if digits:
        if digits == '1':
            text = u'This is a demo app'
            resp.addSpeak(body=text, language='en-US')
        elif digits == '2':
            text = u'Dies ist eine Demo-Anwendung.'
            resp.addSpeak(body=text, language='de-DE')
        else:
            text = u'Άγνωστη εισόδου'
            resp.addSpeak(body=text, language='el-GR')
    else:
        resp.addSpeak('No input received')

    ret_response = make_response(resp.to_xml())
    ret_response.headers["Content-type"] = "text/xml"
    return ret_response

@app.route('/digits/', methods=['GET'])
def digits():
    #import ipdb; ipdb.set_trace()
    action = request.args.get('action', 'http://' + request.environ['SERVER_NAME'] + '/getdigits/')
    method = request.args.get('method', 'GET')
    timeout = request.args.get('timeout', '')
    retries = request.args.get('retries', '')
    finishonkey = request.args.get('finishOnKey', '')
    numdigits = request.args.get('numDigits', 0)
    validdigits = request.args.get('validDigits', '0123456789#*')
    params = {'action': action, 'method': method}
    if timeout:
        params['timeout'] = timeout
    if retries:
        params['retries'] = retries
    if finishonkey:
        params['finishOnKey'] = finishonkey
    if numdigits:
        params['numDigits'] = numdigits
    response = plivo.Response()
    getdigits = plivo.GetDigits(**params)
    getdigits.addSpeak(body="Press one for English.")
    getdigits.addSpeak(body="Press two for German.")
    response.add(getdigits)
    response.addSpeak(body="Input not received. Thank you.")
    ret_response = make_response(response.to_xml())
    ret_response.headers["Content-type"] = "text/xml"
    return ret_response

if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)
