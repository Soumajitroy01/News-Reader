import json
import requests
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("News for today... lets begin")
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=33d8c3f6375842ad8f8e03bf427babc1"
    text=requests.get(url).text
    news=json.loads(text)
    for i in range(0,11):
        if i==10:
            speak(news['articles'][i]['title'])
        else:
            speak(news['articles'][i]['title'])
            speak("Moving on to the next news")
speak("Thanks for listening..")