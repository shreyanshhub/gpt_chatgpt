import tweepy
import openai
from forever import keep_alive
import time

keep_alive()

openai.api_key = "" #Store the key which you get in this object

consumer_key = "" 
consumer_secret = ""
key = ""
secret = "" 

#Store all the keys which you get from your Twitter Developer Account

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

while 1:

  File = "last.txt"

  def read_last(File):
      f = open(File,"r")
      last_seen_id = int(f.read().strip())
      f.close()
      return last_seen_id

  def store_last(f,last_seen_id):
      f = open(File,"w")
      f.write(str(last_seen_id))
      f.close()
      return 
  
  tweets = api.mentions_timeline(read_last(File),tweet_mode="extended")
  try:
    
    def reply():
      
        for tweet in reversed(tweets):
          
          model_engine = "text-davinci-003"
          prompt = tweet.full_text
          print(prompt)  
  # Generate a response
          completion = openai.Completion.create(
              engine=model_engine,
              prompt=prompt,
              max_tokens=1024,
              n=1,
              stop=None,
              temperature=0.5,
          )
        
          response = completion.choices[0].text
          print(response)
          api.update_status("@"+tweet.user.screen_name+" "+str(response),tweet.id)
          store_last(File,tweet.id)

    reply()
    time.sleep(15)

  except:

    def reply():
        for tweet in reversed(tweets):

          api.update_status("@"+tweet.user.screen_name+" "+"Response exceeds tweet character limit",tweet.id)
          store_last(File,tweet.id)

    reply()

    time.sleep(15)
