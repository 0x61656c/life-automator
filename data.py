import urllib.request
import json
import os
import wolframalpha


pa_api_key = 'key=' + str(os.environ['port_auth_api_key'])

pa_base_url = 'http://realtime.portauthority.org/bustime/api/v3/'

pa_commands = {
    'getTruetime' : 'getpredictions?'
}

pa_rt_id = {
    '61D' : '&rt=61D',
    '61C' : '&rt=61C'
}

pa_stp_id = {
    'home-inbound' : '&stpid=10919',
    'home-outbound' : '&stpid=10953',
    'school-outbound' : '&stpid=7117'
}

pa_bus_feed_id = '&rtpidatafeed=Port%20Authority%20Bus'

pa_formats = {
    'json' : '&format=json'
}

def truetime(base_url, api_key, rt_id, stp_id, feed_id, _format, command = pa_commands['getTruetime']):
    built_url = base_url + command + api_key + rt_id + stp_id + feed_id + _format 
    return json.loads(urllib.request.urlopen(built_url).read())

def get_truetime_home_inbound():
    _data = [(truetime(pa_base_url, 
        pa_api_key, 
        pa_rt_id['61D'], 
        pa_stp_id['home-inbound'], 
        pa_bus_feed_id, 
        pa_formats['json'])\
        ['bustime-response']['prd'][0]['prdctdn']),
        (truetime(pa_base_url, 
        pa_api_key, 
        pa_rt_id['61C'], 
        pa_stp_id['home-inbound'], 
        pa_bus_feed_id, 
        pa_formats['json'])\
        ['bustime-response']['prd'][0]['prdctdn'])]

    if str(_data[0]) == 'DUE' or str(_data[1]) == 'DUE':
        _response = 'DUE'

    _response = str(min(_data))
    
    return _response

def get_truetime_home_outbound():
    _response = str(truetime(pa_base_url, 
        pa_api_key, 
        pa_rt_id['61D'], 
        pa_stp_id['home-inbound'], 
        pa_bus_feed_id, 
        pa_formats['json'])\
        ['bustime-response']['prd'][0]['prdctdn'])
    
    return _response

def get_truetime_school_outbound():
    _data = [(truetime(pa_base_url, 
        pa_api_key, 
        pa_rt_id['61D'], 
        pa_stp_id['school-outbound'], 
        pa_bus_feed_id, 
        pa_formats['json'])\
        ['bustime-response']['prd'][0]['prdctdn']),
        (truetime(pa_base_url, 
        pa_api_key, 
        pa_rt_id['61C'], 
        pa_stp_id['school-ountbound'], 
        pa_bus_feed_id, 
        pa_formats['json'])\
        ['bustime-response']['prd'][0]['prdctdn'])]

    if str(_data[0]) == 'DUE' or str(_data[1]) == 'DUE':
        _response = 'DUE'

    _response = str(min(_data))
    
    return _response

def get_information(input):
    w_a_id = str(os.environ['w_a_id'])
    
    w_a_client = wolframalpha.Client(w_a_id)
    res = w_a_client.query(str(input))
    return (next(res.results).text)
