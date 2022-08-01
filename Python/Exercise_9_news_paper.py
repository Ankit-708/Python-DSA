# from win32com.client import Dispatch

# speak = Dispatch("SAPI.SpVoice")

# speak.Speak("Ankit vishwakama")


def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.spVoice")

    speak.Sepak(str)

if __name__ == '__main__':
    speak("Kaise ho bhai")


