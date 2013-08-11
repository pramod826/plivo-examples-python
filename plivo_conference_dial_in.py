from flask import Flask, request,Response
import plivo
import os

SERVER_NAME = 'my.server.domain'
CONF_CODE = '1234'

app = Flask(__name__)

@app.route('/conf-get-input/', methods=['GET', 'POST'])
def conf_get_input():
    response = plivo.XML.Response()
    repsonse.addSpeak('If you know your conference pin, please enter')
    getdigits = response.addGetDigits(
        action='http://' + SERVER_NAME + '/getdigits/',
        timeout='15',
        finishOnKey='#'
    )
    response.addSpeak(body="Input not received. Thank you.")
    xml_response=Response(response.to_xml(),mimetype='text/xml')
    return xml_response

@app.route('/conf-verify-input/', methods=['GET', 'POST'])
def conf_verify_input():
    if request.method == 'GET':
        user_input = request.args.get('Digits', '')
    elif request.method == 'POST':
        user_input = request.form.get('Digits', '')
        
    response = plivo.XML.Response()
    if CONF_CODE != 'Digits':
        response.addSpeak('There is no conference running with the given code.')
        response.addHangup()
    else:
        response.addConference(
            body='myconference',
            action='http://' + SERVER_NAME + '/conf-action/',
            callbackUrl='http://' + SERVER_NAME + '/conf-callback/'
        )

    xml_response = Response(response.to_xml(),mimetype='text/xml')
    return xml_response

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
