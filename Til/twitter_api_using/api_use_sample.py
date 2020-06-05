from twitter import *

CONSUMER_KEY='nOpJwLCK4HQyJBwDtgvgje0Gn'
CONSUMER_SECRET_KEY='001WsZ04LRlOWnNRIBWbR1vmK1HQHwSZX2pkk5wgMmpOqMouby'
ACCESS_TOKEN='436711409-XQZDJfqWZszKCc2H7aO9UjsMPamljEdt2COM7ZQQ'
ACCESS_TOKEN_SECRET='cT4DtgMGF60oAyhLjrJR3nAkXsNM4Ju3hqkY0b88fM2V5'



t=Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET_KEY))

timelines=t.statuses.home_timeline()
for timeline in timelines:
    tl='({id})[{username}]:{text}'.format(id=timeline['id'],username=timeline['user']['name'],text=timeline['text'])
    print(tl)
