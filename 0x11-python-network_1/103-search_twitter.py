"""
 module to perform a Twitter search
 usage: [API key] [API secret] [search string]
 """


from sys import argv
import base64
import requests


if __name__ == '__main__':
    consumer = base64.b64encode((argv[1] + ':' + argv[2]).encode())
    req = requests.post(
        'https://api.twitter.com/oauth2/token',
        headers={
            'Authorization': 'Basic ' + consumer.decode(),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        },
        data={'grant_type': 'client_credentials'}
    )
    token = req.json().get('access_token')
    req = requests.get(
        'https://api.twitter.com/1.1/search/tweets.json',
        headers={'Authorization': 'Bearer ' + token},
        params={'q': argv[3], 'count': '5'}
    )
    tweets = req.json().get('statuses')
    for tweet in tweets:
        print('[{}] {} by {}'.format(
            tweet.get('id'),
            tweet.get('text'),
            tweet.get('user').get('name')
        ))
