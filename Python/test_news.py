import pyttsx3
import requests
import json
import time
# Step #2: Setting up URL with API key, place your API key here.

url = ('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=45990bb891924fa294dfab68814379dd')
  
url += 'your_api_key_here'
# Step #3: Setting an engine for pyttsx3 for reading news.

engine = pyttsx3.init()
# Step #4: Setting up properties of our engine, means reading rate, volume, and sound of a voice.

rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)
   
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.60)
   
sound = engine.getProperty ('voices')
engine.setProperty('voice', 'sound[1].id')
# Step #5: Trying to send request to get news. Here, engine.say() function is used to read news.

try:
    response = requests.get(url)
except:
    engine.say("can, t access link, plz check you internet ")
   
news = json.loads(response.text)
for new in news['articles']:
    print("##############################################################\n")
    print(str(new['title']), "\n\n")
    engine.say(str(new['title']))
    print('______________________________________________________\n')
  
    engine.runAndWait()
  
    print(str(new['description']), "\n\n")
    engine.say(str(new['description']))
    engine.runAndWait()
    print("..............................................................")
    time.sleep(2)