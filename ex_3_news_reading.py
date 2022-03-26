# ex_3_news_reading
import requests
r = requests.get('https://newsapi.org/v2/everything?q=bitcoin&from=2021-07-22&sortBy=publishedAt&apiKey=ab626f10aa83481da399a17622c62bd1')
print(r)

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak(r)