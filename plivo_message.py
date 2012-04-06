import plivo


auth_id = ""
auth_token = ""

p = plivo.RestAPI(auth_id, auth_token)

# Send a SMS
params = {
    'src': '1202XXXXXX', # Caller Id
    'dst' : '12033XXXXX', # User Number to Call
    'text' : "Hi, message from Plivo",
    'type' : "sms",
}

response = p.send_message(params)

