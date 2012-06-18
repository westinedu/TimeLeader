import oauth.oauth as oauth


consumer_evernote = oauth.Consumer(key="westine", 
    secret="277e8b3a8cc49b2d")
client_evernote = oauth.Client(consumer_evernote)
evernoteHost = "www.evernote.com"
request_token_url_evernote = "https://" + evernoteHost + "/oauth"

resp, content = client_evernote.request(request_token_url_evernote, "GET")

print resp
print content