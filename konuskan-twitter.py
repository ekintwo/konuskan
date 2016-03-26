# -*- coding: utf-8 -*-

import sys, zeka, twitter
reload(sys)  
sys.setdefaultencoding('utf8')

CONSUMER_KEY = 'hTa9NFBqfBfEdEvRqrH1GjUxT'
CONSUMER_SECRET = '5PfIGUdO5CwDXRGurpCkQyQwkpfDlHp1dg5vzGPgENca1yinPS'
ACCESS_TOKEN = '713839272646692868-JpGxvlOLGSSrFZQDZOnIKbrXFgUNv1j'
ACCESS_TOKEN_SECRET = 'qVEkUvz5T8tEDyX0yXs9m7nA8uWjBL7b29cY0legrqXhT'

class konuskan_twitter:
    def __init__(self):
        
        twitter_auth    = twitter.OAuth(
            consumer_key    = CONSUMER_KEY,
            consumer_secret = CONSUMER_SECRET,
            token           = ACCESS_TOKEN,
            token_secret    = ACCESS_TOKEN_SECRET
        )
        twitter_api     = twitter.Twitter(auth=twitter_auth)
        twitter_ustream = twitter.TwitterStream(auth=twitter_auth, domain='userstream.twitter.com')
        
        print "Listening for new direct messages..."
        for msg in twitter_ustream.user():
            if 'direct_message' in msg:
                dm     = msg['direct_message']
                sender = dm['sender']['screen_name']
                text   = dm['text']
                print "TWITTERING: @%s\n%s\n" % (sender, text)
                    
'''
            giris = "selam"
            cikis = zeka.__init__(giris)
            if cikis:
                print cikis
'''
        
if __name__ == "__main__":
    konuskan_twitter()