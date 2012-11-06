# -*- coding: utf-8 -*-
## Above line is to confirm that unicode Non-ASCII charcters would be included
## in this file
from flask import Flask, Response, request, make_response
import plivo
import os
import cgi
import sys

app = Flask(__name__)

@app.route('/getdigits/', methods=['GET', 'POST'])
def getdigits():
    ## import ipdb; import ipdb
    if request.method == 'GET':
        digits = request.args.get('Digits', '')
    elif request.method == 'POST':
        digits = request.form.get('Digits', '')
    
    resp = plivo.Response()
    if digits:
        if digits == '1':
            resp.addSpeak("Hello, welcome to Plivo's demo app")
        else:
            ## convert the accented characters to html entities
            text = cgi.escape(u'Hola, bienvenido a la aplicación de demostración Plivo').encode('ascii', 'xmlcharrefreplace')
            resp.addSpeak(body=text, language='es-ES', loop=0)
            ## text = cgi.escape(u'Wie heißt du? Sie weiß nicht? Ich heiße Plivo').encode('ascii', 'xmlcharrefreplace')
            ## resp.addSpeak(body=text, language='de-DE')

    else:
        resp.addSpeak('No input received')

    ret_response = make_response(resp.to_xml())
    ret_response.headers["Content-type"] = "text/xml"
    return ret_response

@app.route('/digits/', methods=['GET'])
def digits():
    action = request.args.get('action', 'http://domain.name/getdigits/')
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
    getdigits.addSpeak(body="Press 1 for English.")
    getdigits.addSpeak(body="Press 2 for Spanish.")
    ## getdigits.addSpeak(body="Press 2 for German.")
    response.add(getdigits)
    response.addSpeak(body="Input not received. Thank you.")
    ret_response = make_response(response.to_xml())
    ret_response.headers["Content-type"] = "text/xml"
    return ret_response

if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)
