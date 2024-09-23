import pyttsx3
import engineio

#voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engineio = pyttsx3.init()
engineio.setProperty('voice', voice_id)
engineio.setProperty('rate',150)
engineio.say('ok google')
engineio.runAndWait()
