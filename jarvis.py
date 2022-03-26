# jarvis
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voices', voices[0].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning')

    elif hour >= 12 and hour < 18:
        speak('good afternoon')

    else:
        speak('good afternoon')

    speak('i am susan  sir, please tell me how may i help you')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listning.........')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognising....')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: ,{query} \n')

    except Exception as e:
        # print(e)
        print('sorry say again bro')
        return 'None'
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('sentp.gmail.com', 587)
    server = echo()
    server = starttls()
    server = login('dnyane.04@gmail.com', 'password')
    server = sendmail('dnyane.04@gmail.com', to, content)
    server = close()


if __name__ == '__main__':
    # speak('danny is a  good boy')
    wishme()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace('wikipedia', " ")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wiki ')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Dnyane\\Documents\\webdesign\\webdesign\\Icons\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(strTime)

        elif 'open code' in query:
            codepath = 'C:\\Users\Dnyane\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(codepath)

        elif 'email me' in query:
            try:
                speak('what should i say?')
                content = take_command()
                to = 'dnyane.04@gmail.com'
                sendEmail(to, content)
                speak('email has been sent')
            except Exception in f:
                print(f)
                speak('sorry could not send')
