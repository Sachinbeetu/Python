import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today.. Lets begin")
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=163b3071f144450eb6e67ff3c848bdc1')
    # url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=163b3071f144450eb6e67ff3c848bdc1"
    news = requests.get(url).text
    news_dict = json.loads(news)
    c=str(news_dict['totalResults'])
    nc='There are total '+c +' news in feed'
    print(nc)
    speak(nc)
    arts = news_dict['articles']
    count=0
    for article in arts:
        if count>0:
          speak("Next news..")
        print(article['title'])
        speak(article['title'])
        count += 1
    speak("Thanks for listening Have a good day..")
