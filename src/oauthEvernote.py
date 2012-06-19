import urlparse
import urllib

import oauth2 as oauth
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
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

@app.route('/authComplete')
def auth_finish():
    """After the user has authorized this application on Evernote's website,
    they will be redirected back to this URL to finish the process."""

    oauth_verifier = request.args.get('oauth_verifier', '')

    token = oauth.Token(session['oauth_token'], session['oauth_token_secret'])
    token.set_verifier(oauth_verifier)

    client = get_oauth_client()
    client = get_oauth_client(token)

    # Retrieve the token credentials (Access Token) from Evernote
    resp, content = client.request(EN_ACCESS_TOKEN_URL, 'POST')

    if resp['status'] != '200':
        raise Exception('Invalid response %s.' % resp['status'])

    access_token = dict(urlparse.parse_qsl(content))
    authToken = access_token['oauth_token']

    userStore = get_userstore()
    user = userStore.getUser(authToken)

    # Save the users information to so we can make requests later
    session['shardId'] = user.shardId
    session['identifier'] = authToken

    return "<ul><li>oauth_token = %s</li><li>shardId = %s</li></ul>" % (
        authToken, user.shardId)
    
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