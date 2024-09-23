import pyttsx3 

hey = ' '.join(['hi', 'monic', 'soja'])
print(hey)
engine = pyttsx3.init() 
engine.setProperty('rate', 150)
engine.say('Hi monic')
print(engine.getProperty('voice'))

engine.runAndWait()

print('monic')