import urllib.parse
from urllib.request import *
import json
import requests

params = urllib.parse.urlencode({0: "collect_readonly"}).encode('utf-8')
with urlopen('http://trialos.test.com/api/csp-service/trialos/role/edc/edc_collect_test/ceshi51?', data=params) as f:
    print(f.read().decode('utf-8'))


url = 'http://trialos.test.com/api/csp-service/trialos/role/edc/edc_collect_test/ceshi51?'
headers = {'Cookie': 'token=3fe3165d2e6a4cef98df1c7461901eff', 'Content-Type': 'application/json',
           'TM-Header-SubEnv-StrictMode': 'false',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
request_params = {0: "collect_readonly"}
response = requests.post(url, data=json.dumps(request_params), headers=headers)
print(response.text)


req = Request(url=url, method='POST')
req.add_header('Cookie', 'token=3fe3165d2e6a4cef98df1c7461901eff')
req.add_header('Content-Type', 'application/json')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36')
req.add_header('TM-Header-SubEnv-StrictMode', 'false')
with urlopen(req, data=params) as f:
    print(f.read().decode('utf-8'))
