# ✋🤖 Sign Language Recognition for Digital Assistants

A deep learning-based gesture recognition system that enables individuals with hearing or speech impairments to interact with digital assistants (like Alexa, Siri, or Google Assistant) using hand signs. This project is designed to improve accessibility and bridge the communication gap through real-time sign language interpretation.

---

## 🎯 Objective

To create a real-time hand gesture recognition system that:

- Recognizes static sign language gestures using CNNs
- Translates gestures into meaningful voice/text commands
- Interfaces with virtual assistants for hands-free control

---

## 🧠 Powered By Research

This project builds upon techniques described in:

- [IEEE Xplore: Sign Language to Speech Conversion](https://ieeexplore.ieee.org/abstract/document/9183179)
- [IRJET: Gesture Recognition using CNN for Speech Impairment](https://www.irjet.net/archives/V7/i3/IRJET-V7I31032.pdf)

These papers informed the architecture and modeling strategies used for gesture classification, focusing on enhancing real-time accuracy and usability.

---

## ⚙️ Tech Stack

- **Programming Language**: Python
- **Libraries**: TensorFlow, OpenCV, NumPy, scikit-learn
- **Model**: Convolutional Neural Network (CNN)
- **Input**: Hand gestures captured via webcam

---

## 📁 Project Structure
Sign_Language_Recognition_for_Digitial_Assistants/ 
│ ├── dataset/ # Labeled image dataset of hand gestures 
  ├── model/ # Saved CNN model and training logs 
  ├── src/ 
│ ├── preprocess.py # Image processing utilities 
│ ├── train.py # CNN model training script 
│ ├── predict.py # Real-time prediction using webcam input 
│ └── utils.py # Helper functions for mapping and visualization 
  ├── requirements.txt # Python dependencies 
├── README.md # Project documentation 
└── assistant_integration/ # Optional: Scripts for assistant API interfacing


---

## 🚀 How to Run

### 1. Clone the Repo
```
git clone https://github.com/veeoid/Sign_Language_Recognition_for_Digitial_Assistants.git
cd Sign_Language_Recognition_for_Digitial_Assistants
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Train the Model
```
python src/train.py
```
4. 4. Start Real-Time Prediction
```
python src/predict.py
```
📝 Make sure your webcam is connected.

Gesture | Detected Command | Assistant Action
✋ Palm | “Turn on lights” | Google Home turns on bulb
👍 Thumb | “Play music” | Alexa plays Spotify track

🧩 Future Scope
Support dynamic gestures and full sentences (RNNs/LSTMs)

Multilingual sign language (ASL, ISL, BSL, etc.)

Integration with wearable or AR devices

Feedback loop for correcting model predictions
