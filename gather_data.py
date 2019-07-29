import json, requests, os, time, datetime
from requests_oauthlib import OAuth1

auth_config = json.loads(open('config.json','r').read())
consumer_key = auth_config["consumer_key"]
consumer_secret = auth_config["consumer_secret"]
access_token = auth_config["access_token"]
access_secret = auth_config["access_secret"]

base_url = "https://api.twitter.com/1.1/"
user = "realDonaldTrump"
params = {"screen_name":user,
            "count":200,
            "tweet_mode":"extended",
            "exclude_replies":"true",
            "include_rts":"false"}
def get_api_info(params):
    auth = OAuth1(consumer_key,consumer_secret,
        access_token,access_secret)
    request_url = 'statuses/user_timeline.json?'
    for num,param in enumerate(params):
        if not num == 0:
            request_url = request_url+"&"
        request_url = request_url+param+"="+str(params[param])
    response = requests.get(base_url+request_url,auth = auth)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
def get_stack():
    total_statuses = []
    for i in range(int(3200/params["count"])):
        statuses = get_api_info(params)
        if statuses:
            for num,status in enumerate(statuses):
                total_statuses.append(status["full_text"])
                if num == len(statuses) - 1:
                    params["max_id"] = status["id"]
    if("max_id" in params):
        params.pop("max_id")
    return total_statuses

total_tweets = []
temp_tweets = []
counter = 0
tweet_count = 0
start_time = time.clock()

readFile = open("input.txt","r")
total_tweets = readFile.readlines()
readFile.close()
counter = len(total_tweets)
tweet_count = len(total_tweets)

while True:
    temp_tweets = get_stack()
    if temp_tweets:
        for tweet in temp_tweets:
            if tweet not in total_tweets:
                total_tweets.append(tweet)
                tweet_count += 1
    counter += 1
    print("Stack: {0} Total Tweet Count: {1} Time Running: {2} Date/Time: {3}".format(counter,tweet_count,time.clock()-start_time,datetime.datetime.now()))
    file = open("input.txt","w")
    for line in total_tweets:
        formatted_line = str(line.encode('ascii','ignore'))
        file.write(formatted_line+"\n")
    file.close()
    time.sleep(1000)
