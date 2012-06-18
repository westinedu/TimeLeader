import oauth2 as oauth

# Create your consumer with the proper Consumer key/Consumer secret.
consumer_twitter = oauth.Consumer(key="IJiitWuYiHZDEEbPEJqlow", 
    secret="hbj8OzOOS57X4PKkdEs0ShXOo57dT6Qsz1q1Rq8crFg")

# Request token URL for Twitter.
request_token_url_twitter = "http://twitter.com/oauth/request_token"

# Create our client.
client_twitter = oauth.Client(consumer_twitter)

# The OAuth Client request works just like httplib2 for the most part.
resp, content = client_twitter.request(request_token_url_twitter, "GET")
print resp
print content

consumer_evernote = oauth.Consumer(key="westine", 
    secret="277e8b3a8cc49b2d")
client_evernote = oauth.Client(consumer_evernote)
evernoteHost = "www.evernote.com"
request_token_url_evernote = "https://" + evernoteHost + "/oauth"

resp, content = client_evernote.request(request_token_url_evernote, "GET")

print resp
print content