import speech_recognition
import wikipedia

#Read input from microphone
def speech_to_text():
    #Initialize SpeechRecognition recognizer
    speech = speech_recognition.Recognizer()
    try:
        #Use microphone as audio source
        with speech_recognition.Microphone() as mic:
            #Adjust for ambient noise
            speech.adjust_for_ambient_noise(mic, duration=0.2)
            #Capture audio
            audio = speech.listen(mic)
            #Google Web Speech Api to recognize input
            text = speech.recognize_google(audio).lower()
            return text
    except speech_recognition.UnknownValueError:
        print("Sorry, I couldn't understand that. Please try again.")
        return speech_to_text()
    except speech_recognition.RequestError:
        print("Speech recognition request error. Check your microphone and internet connection.")

def wiki_query(text):
    try:
        #Query Wikipedia
        result = wikipedia.summary(text, sentences=2)
        print(f"\nInput: {text}")
        print("Result:", result)
        #Handle any errors from Wikipedia summary
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Ambiguous query. Please be more specific: {e}\n")
    except wikipedia.exceptions.PageError as e:
        print(f"Page not found. Try a different query: {e}")

def main():
    #Continously listen for user input
    while True:
       text = speech_to_text()
       #End program check
       if(text == "exit"):
           break
       #Wikipedia Query
       wiki_query(text)
           

if __name__ == "__main__":
    main()