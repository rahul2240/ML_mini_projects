import tweepy
from textblob import TextBlob

Consumer_Key = '8nv7eFVP5EwLEQGw3Or7s5NaZ'
Consumer_Secret = 'ncBv6QazXQXZJu8iLAUqOMai1x4MGpm61CbPWgMobtQZLo5wEM'

Access_Token =  '771717475813687301-AZA1HiLoC8RXWhEs603FLwitaEcPOkb'
Access_Token_Secret = '0qh7jSLV4Qi9W1WneMsjijvJgvVLAf1sAHPxMyvMhraTo'

auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)


api = tweepy.API(auth)

public_tweets = api.search('data')

csv = open("./two/data.csv", "w")
csv.write("TWEETS ON TRUMP \n")

for tweet in public_tweets:
    text = tweet.text
    text = text.replace("\"", "\"\"")
    texty = "\"" + text + "\""
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print analysis.sentiment
    csv.write(texty);
