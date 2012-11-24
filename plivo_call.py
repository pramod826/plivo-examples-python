import plivo


auth_id = ""
auth_token = ""

p = plivo.RestAPI(auth_id, auth_token)

# Make Calls
params = {
    'from': '1212121212', # Caller Id
    'to' : '232323232323', # User Number to Call
    'ring_url' : "http://example.herokuapp.com/ring_url",
    'answer_url' : "http://example.com/answer_url",
    'hangup_url' : "http://example.herokuapp.com/hangup_url",
}
response = p.make_call(params)

# Hangup Call
params = {
        'call_uuid' : 'XXXXXXXXXXXXXXX',
        }
response = p.hangup_call(params)

# Hangup All Calls
response = p.hangup_all_calls()


# Transfer Calls
params = {
        'call_uuid' : 'XXXXXXXXXXXXXXX',
        'transfer_url': 'http:example.com/transfer_url',
        }
response = p.transfer_call(params)


# Get CDR
params = {
        'record_id' : 'XXXXXXXXXXXXXXX',
        }
response = p.get_cdr(params)


# Record
params = {
        'call_uuid' : 'XXXXXXXXXXXXXXX',
        }
response = p.record(params)


# Stop Record
params = {
        'call_uuid' : 'XXXXXXXXXXXXXXX',
        }
response = p.stop_record(params)

