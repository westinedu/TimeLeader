import urlparse
import urllib

import oauth2 as oauth
from flask import Flask, session, redirect, url_for, request

APP_SECRET_KEY = \
    'YOUR KEY HERE'

EN_CONSUMER_KEY = 'westine'
EN_CONSUMER_SECRET = '277e8b3a8cc49b2d'

EN_REQUEST_TOKEN_URL = 'https://www.evernote.com/oauth'
EN_ACCESS_TOKEN_URL = 'https://www.evernote.com/oauth'
EN_AUTHORIZE_URL = 'https://www.evernote.com/OAuth.action'

EN_HOST = "www.evernote.com"
EN_USERSTORE_URIBASE = "https://" + EN_HOST + "/edam/user"
EN_NOTESTORE_URIBASE = "https://" + EN_HOST + "/edam/note/"


consumer = oauth.Consumer(EN_CONSUMER_KEY,EN_CONSUMER_SECRET)
client = oauth.Client(consumer)

callback_url = 'http://%s%s' % ('127.0.0.1:5000', url_for('auth_finish'))
request_url = '%s?oauth_callback=%s' % (EN_REQUEST_TOKEN_URL,
        urllib.quote(callback_url))
    
resp, content = client.request(request_url, 'GET')

if resp['status'] != '200':
    raise Exception('Invalid response %s.' % resp['status'])

access_token = dict(urlparse.parse_qsl(content))
authToken = access_token['oauth_token']
    
print resp
print content