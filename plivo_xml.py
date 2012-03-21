import plivo


r = plivo.Response()


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


r = plivo.Response()
url = 'http://example.com/redirect'
params = {'method':'POST'}
r.addRedirect(url, **params)

"""
Output:
    <Response>
    <Redirect method="POST">http://example.com/redirect</Redirect>
    </Response>
"""
