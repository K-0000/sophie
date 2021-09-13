import speech_recognition as sr
import pyttsx3
import wikipedia
# Initialize the recognizer
r = sr.Recognizer()




def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(command)
    engine.runAndWait()

SpeakText("Welcome")

while (1):

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        print("Done")
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            if (MyText == "hey sophie"):
                print("Did you say" + MyText)
                SpeakText("Hello how may I serve you?")
            elif (MyText == "what is your name"):
                SpeakText("I am sophie. I am an AI machine created by Ken")
            elif (MyText == "what is your purpose"):
                SpeakText("I am here to assists you with the questions you have")
            elif (MyText == "i have some question"):
                with sr.Microphone() as source2:
                    SpeakText("What would you like to know?")
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    audio1 = r.listen(source2)
                    wiki = r.recognize_google(audio1)
                    wiki = wiki.lower()
                    print(wiki)
                    SpeakText("I am searching for"+wiki)
                    k=wikipedia.summary("'"+wiki+"'")
                    print(k)
                    SpeakText(k)

            elif (MyText == "goodbye sophie"):
                SpeakText("goodbye, have a nice day")
                exit()

            else:
                print("Did you say " + MyText)
                SpeakText("could you repeat that?")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
