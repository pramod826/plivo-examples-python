import os
from flask import Flask, make_response
import plivo

app = Flask(__name__)

@app.route('/transcription/xml/')
def hello():
    response = plivo.Response()
    recording_parameters = {'action': 'http://server/url1',
                            'method': 'GET',
                            'maxLength': '30',
                            'finishOnKey': '*',
                            'transcriptionType': 'auto',
                            'transcriptionUrl': 'http://server/url2',
                            'transcriptionMethod': 'GET',
                           }
    response.addRecord(**recording_parameters)
    return_response = make_response(response.to_xml())
    return_response.headers["Content-Type"] = "text/xml"
    return return_response

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)