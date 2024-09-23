import sys
import os

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import copy
import cv2
import pyttsx3 
import speech_recognition as sr
# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

r = sr.Recognizer()

def main2():
    print('printing stuff')

def main():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        audio = r.listen(source)
        print("Recognizing Now .... ")
        # recognize speech using google
 
        try:
            output_text = r.recognize_google(audio)
            print(output_text)
            imgNew= np.zeros((200,1200,3), np.uint8)
            cv2.namedWindow("Output", cv2.WINDOW_FREERATIO)
            cv2.putText(imgNew,'%s' %(output_text), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            cv2.imshow("Output", imgNew)
            #cv2.waitKey(0)


            print("Audio Recorded Successfully \n ") 
        except Exception as e:
            print("Error :  " + str(e))

       

def predict(image_data):

    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})

    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

    max_score = 0.0
    res = ''
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        if score > max_score:
            max_score = score
            res = human_string
    return res, max_score

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("logs/trained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("logs/trained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

    c = 0

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300);
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300);

    res, score = '', 0.0
    i = 0
    mem = ''
    consecutive = 0
    sequence = ''
    speak_text = ''
    speak_words = []
    not_to_speak_words = ['', 'space', 'nothing', 'call', 'del']
    command_end_words = ['del', 'call']
    engine = pyttsx3.init()
    engine.setProperty('rate',130)
    #voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    #engine.setProperty('voice', voice_id)

    
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        
        if ret:
            x1, y1, x2, y2 = 100, 100, 300, 300
            img_cropped = img[y1:y2, x1:x2]

            c += 1
            image_data = cv2.imencode('.jpg', img_cropped)[1].tostring()
            
            a = cv2.waitKey(1) # waits to see if `esc` is pressed
            
            prediction_text = ''
            if i == 4:
                res_tmp, score = predict(image_data)
                print("prediction result ", res_tmp)
                res = res_tmp
                prediction_text = res_tmp
                i = 0
                if mem == res:
                    consecutive = 1
                    print(consecutive)
                else:
                    consecutive = 0
                if consecutive == 2 and res not in ['nothing']:
                    if res == 'space':
                        #sequence += '/n'
                        sequence = sequence
                        #print(sequence)
                    elif res == 'del':
                        sequence = sequence[:-1]
                    else:
                        #sequence += res
                        sequence = res
                    consecutive = 0
            i += 1
            #imgnew = np.zeros((200,1200,3), np.uint8)
            # cv2.putText(img, '%s ' % (res.upper()), (100,400), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2)
            #cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
            cv2.putText(img, '(score = %.5f)' % (float(score)), (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
            mem = res
            cv2.rectangle(img, (x1, y1), (x2, y2), (255,0,0), 2)

            cv2.imshow("img", img)
            #cv2.imshow("score",imgnew)
            
            img_sequence = np.zeros((200,1200,3), np.uint8)
            
            
            #Original Code
            #cv2.putText(img_sequence, '%s' % (sequence.upper()), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            
            cv2.putText(img_sequence, '%s' % (prediction_text.upper()), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            
            cv2.imshow('sequence', img_sequence)
            # engine = pyttsx3.init() 
            # rate = engine.getProperty('rate')   # getting details of current speaking rate
            # engine.setProperty('rate', 125)     # setting up new voice rate
            # engine.say(prediction_text)
            if (prediction_text in command_end_words and len(speak_words) > 0):
                prediction_text = ''
                speak_text = ' '.join(speak_words).strip()
                print('Will utter: ' + speak_text)
                engine.say("alexa")
                engine.say(speak_text)
                speak_words = []
                engine.runAndWait()

                main()
            elif(prediction_text not in not_to_speak_words and prediction_text not in speak_words):
                speak_words.append(prediction_text)
                prediction_text = ''      

            
            if a == 27: # when `esc` is pressed
                break

# Following line should... <-- This should work fine now
cv2.destroyAllWindows() ()
cv2.VideoCapture(0).release()
