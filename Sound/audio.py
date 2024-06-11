from gtts import gTTS
from playsound import playsound

audio = 'sla.mp3'
language = 'pt-br'

sp = gTTS(
    text = '''
opaaaaa
''',
    lang = language
)

sp.save(audio)
playsound(audio)