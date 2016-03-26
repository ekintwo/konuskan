# -*- coding: utf-8 -*-

import sys, zeka, twitter
reload(sys)  
sys.setdefaultencoding('utf8')

CONSUMER_KEY = 'OndA1IbisgwyqflyNfqVSZyMX'
CONSUMER_SECRET = 'ZzNxanCvO3sAz78htAdCY3JDLJzzLZNu9KJyVzzkPNP4eEYM7c'
ACCESS_TOKEN = '713839272646692868-HIDDEN-'
ACCESS_TOKEN_SECRET = '-HIDDEN-'
TWITTER_USERNAME = 'konuskanbot'

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
                
                if text and sender != TWITTER_USERNAME:
                    print "Sender: @%s\nMessage: %s\n" % (sender, text)

                    cikis = zeka.__init__(text)
                    if cikis:
                        twitter_api.direct_messages.new(user=sender, text=cikis)
        
if __name__ == "__main__":
    konuskan_twitter()