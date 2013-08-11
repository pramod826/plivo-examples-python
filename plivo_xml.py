import plivo

r = plivo.XML.Response()


# Add speak
body = 'Calling from Plivo'
params = {'loop':2}

r.addSpeak(body, **params)

# Add play
r.addPlay('http://examples.com/playTrumpet.mp3', **params)

# Add Wait
params = {'length':3}
r.addWait(**params)

""" 
Output:
    <Response>
    <Speak loop="2">Calling from Plivo</Speak>
    <Play loop="2">http://examples.com/playTrumpet.mp3</Play>
    <Wait length="3" />
    </Response>
"""


r = plivo.XML.Response()
url = 'http://example.com/redirect'
params = {'method':'POST'}
r.addRedirect(url, **params)

"""
Output:
    <Response>
    <Redirect method="POST">http://example.com/redirect</Redirect>
    </Response>
"""
d=r.addDial(callerId=_from, callerName=cname)
d.addNumber(to)
'''
to return these response as xml
'''
from flask import Response
response=Response(r.to_xml(),mimetype='text/xml')
return response

