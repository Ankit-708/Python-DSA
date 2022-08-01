# news paper alexa
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=45990bb891924fa294dfab68814379dd"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles'] 
    for article in arts:
        speak(article['title'])
        speak("moving on to the next news.. listen carefully")
