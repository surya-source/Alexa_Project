import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from datetime import datetime
import pyjokes


def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say(answer)
    engine.runAndWait()


def processquestion(question):
    if "what are you doing" in question:
        print("I'm waiting for your question")
        talk("I'm waiting for your question")
        return True

    elif "how are you" in question:
        print("I'm good, thankyou.How can I help you?")
        talk("I'm good, thankyou.How can I help you?")
        return True
    elif "play" in question:
        question = question.replace("play", "")
        pywhatkit.playonyt(question)
        return True
    elif "who is" in question:
        question = question.replace("who is", "")
        print(wikipedia.summary(question, 1))
        talk(wikipedia.summary(question, 1))
        return True
    elif "time" in question:
        time = datetime.today().time().strftime("%I:%M %p")
        print(time)
        talk(time)
        return True
    elif "joke" in question:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
        return True
    elif "bye" in question():
        print("po po,take care")

        return False
    else:
        print("Maybe we can try again later\ni'm not sure what you want to do")
        return True
def getQuestion():

    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
        try:
            print(r.recognize_google(audio))
            question = r.recognize_google(audio)
            if "Alexa" in question:
                question= question.replace("Alexa","")
                print(question)
                return question
            else:
                print("Maybe we can try again later\ni'm not sure what you want to do")
            return "notwithme"


        except sr.UnknownValueError:
            print("Maybe we can try again later\ni'm not sure what you want to do")
            talk("Maybe we can try again later\ni'm not sure what you want to do")
canAskQuestion = True
while canAskQuestion:
    question = getQuestion()
    if (question=="notwithme"):
        talk("ok carry on")
        canAskquestion = False
    else:
        canAskQuestion= processquestion(question)


