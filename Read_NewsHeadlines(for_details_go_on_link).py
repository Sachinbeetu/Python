import requests    #For making request from any site. 
import json    #For JSON.
def speak(str):
    from win32com.client import Dispatch   #For text to speech (TTS)
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today Starting")
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')    #Get your own API from https://newsapi.org/
    # url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    news = requests.get(url).text
    news_dict = json.loads(news)
    c=str(news_dict['totalResults'])
    nc='There are total '+c +' news in feed'
    d=int(c)
    e=d-1
    print(nc)
    speak(nc)
    arts = news_dict['articles']
    count=0
    for a in arts:
        speak(f'News {d-e})')
        print(d-e)
        e-=1
        print(a['title'])
        print('For Detail :',a['url'])
        speak(a['title'])
        count += 1
    print(speak("Thanks for listening Have a good day.."))
