import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today Starting")
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=Xxxxxxxxxxxxxxxxxxxxxxxx')
    # url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=xxxxxxxxxxxxxxxx"
    news=requests.get(url).text
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
