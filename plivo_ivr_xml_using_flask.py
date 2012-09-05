from flask import Flask, Response, request, make_response
import plivo
import os

app = Flask(__name__)

@app.route('/getdigits/', methods=['GET', 'POST'])
def getdigits():
    if request.method == 'GET':
        digits = request.args.get('Digits', '')
    elif request.method == 'POST':
        digits = request.args.get('Digits', '')
    
    resp = plivo.Response()
    if digits:
        if digits == '1':
            resp.addSpeak("Hello, welcome to Plivo's demo app")
        else:
            resp.addSpeak('Hola, bienvenido a la aplicaci&#65533;n de demostraci&#65533;n Plivo', language='es-ES')
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
    response.add(getdigits)
    response.addSpeak(body="Input not received. Thank you.")
    ret_response = make_response(response.to_xml())
    ret_response.headers["Content-type"] = "text/xml"
    return ret_response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
