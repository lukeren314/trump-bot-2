#trump_bot v 1.0
import os,subprocess,json,time,random,urllib,oauth2

checkpoints = []
for dirname,dirnames,filenames in os.walk("cv"):
    for filename in filenames:
        checkpoints.append(filename)
print("Available checkpoints: " + str(checkpoints))
last_cv = checkpoints[0]
print("Using checkpoint: " + last_cv)
auth_config = json.loads(open('config.json','r').read())

consumer_key = auth_config["consumer_key"]
consumer_secret = auth_config["consumer_secret"]
access_token = auth_config["access_token"]
access_secret = auth_config["access_secret"]
status = ""
# def tweet(params):
#     auth = OAuth1(consumer_key,consumer_secret,
#         access_token,access_secret)
#     verify_url = "https://api.twitter.com/1.1/account/verify_credentials.json"
#     verify_response = requests.get(verify_url,auth=auth)
#     print(verify_response)
#     request_url = 'statuses/update.json?'
#     for num,param in enumerate(params):
#         if not num == 0:
#             request_url = request_url+"&"
#         request_url = request_url+param+"="+str(params[param])
#     print("Request URL:\n"+base_url+request_url)
#     response = requests.get(base_url+request_url,auth = auth)
#     print(response)
#     if response.status_code == 200:
#         return json.loads(response)
#     else:
#         return None
def tweet(status):
    consumer = oauth2.Consumer(key=consumer_key,secret=consumer_secret)
    token = oauth2.Token(key=access_token,secret=access_secret)
    client = oauth2.Client(consumer,token)
    resp,content = client.request("https://api.twitter.com/1.1/statuses/update.json?status="+status,method="POST")
    print(resp)
    return(content)
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while True:
    random.seed(time.time())
    #int(time.time())
    rand_letter = str(random.choice(alph)).capitalize()
    return_value = subprocess.call("th sample.lua cv/"+last_cv+" -gpuid -1 -length 120 -seed -"+str(int(time.time()))+" -primetext -"+rand_letter,shell=True)
    sample = rand_letter+open("sample.txt","r").read()
    print("\nSample Taken!\n")
    cutIndex = 120
    for i in range(len(sample)):
        if(i > 80 and cutIndex == 120):
            if sample[i] == "." or sample[i] == "!" or sample[i] == "?" or sample[i] == "\n":
                cutIndex = i
    sample = sample[0:cutIndex]
    print("Return Value: "+str(return_value))
    # params["status"] = "@realDonaldTrump "+sample
    status = urllib.parse.quote(sample)

    response_content = tweet(status)
    readFile = open("out.txt","r")
    save = readFile.read()
    readFile.close()
    writeFile = open("out.txt","w")
    writeFile.write(response_content)
    localtime = time.localtime(time.time())
    writeFile.write("Tweet sent on {}/{}/{}:\n{}".format(localtime.tm_mon,localtime.tm_mday,localtime.tm_year,sample))
    writeFile.close()
    #print(response_content)
    #print("Tweet Sent:\n" + sample)
    time.sleep(24*60*60)
