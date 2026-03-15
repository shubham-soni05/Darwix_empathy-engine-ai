# 🎙️ Empathy Engine -- Emotion-Aware AI Voice Generator

## 📌 Overview

Empathy Engine is an AI-powered system that converts plain text into
emotionally expressive speech.\
Instead of producing robotic monotone voices, the system detects the
emotion in the input text and dynamically adjusts voice parameters such
as speech rate and pitch to generate human-like audio responses.

The project demonstrates how Natural Language Processing (NLP) and
Text-to-Speech (TTS) can work together to create more natural and
empathetic AI communication.

The system is built using **Python, HuggingFace Transformers, Edge-TTS, and Flask**, with a simple **web interface that allows users to input text and hear the generated expressive voice instantly.**

------------------------------------------------------------------------

## 🚀 Vision

Modern AI assistants can understand text but often fail to communicate
emotions in speech.

Traditional TTS systems sound monotone and robotic, which reduces user
engagement and trust.

Empathy Engine solves this problem by:

1.  Detecting emotion from text
2.  Mapping emotion to voice parameters
3.  Generating expressive speech

------------------------------------------------------------------------

## 🧠 Core Features

### Emotion Detection

The system uses the HuggingFace transformer model: `j-hartmann/emotion-english-distilroberta-base`

Detected emotions: 
- Joy
- Surprise
- Anger
- Fear
- Sadness
- Disgust
- Neutral


------------------------------------------------------------------------

### Emotion-Based Voice Modulation

The detected emotion dynamically modifies:

-   Speech Rate
-   Voice Pitch

Example mapping:

| Emotion | Rate | Pitch | Effect |
|------|------|------|------|
| Joy | +25% | +8Hz | Energetic |
| Surprise | +30% | +10Hz | Expressive |
| Anger | +15% | -5Hz | Firm |
| Fear | -20% | +3Hz | Tense |
| Sadness | -25% | -8Hz | Slow & soft |
| Disgust | -10% | -5Hz | Flat |
| Neutral | +0% | +0Hz | Normal |

------------------------------------------------------------------------

### Realistic Neural Voice

Speech is generated using: Microsoft Edge-TTS

Voice used: en-IN-NeerjaNeural

------------------------------------------------------------------------

## 🏗️ System Architecture

User Input (Web UI)\
↓\
Flask API (/analyze)\
↓\
Emotion Detection (Transformer Model)\
↓\
Emotion → Voice Mapping\
↓\
Edge-TTS Speech Generation\
↓\
Generated Audio (.mp3)\
↓\
Audio Playback in Browser

------------------------------------------------------------------------

## 📂 Project Structure

Empathy-Engine\
│\
├── app.py\
├── emotion_detector.py\
├── tts_engine.py\
│\
├── templates\
│ └── index.html\
│\
├── static\
│ └── audio\
│\
├── requirements.txt\
└── README.md

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Clone Repository

git clone https://github.com/shubham-soni05/Darwix_empathy-engine-ai.git

### 2. Create Virtual Environment

### 3. Install Dependencies

pip install -r requirements.txt

Example requirements:

flask\
transformers\
torch\
edge-tts

### 4. Run Application

python app.py

Server runs at: [http://localhost:10000](http://127.0.0.1:5000)

------------------------------------------------------------------------

## 🖥️ Usage

1.  Open the web interface
2.  Enter a sentence
3.  Click **Detect Emotion & Generate Voice**
4.  The system will:
    -   Detect emotion
    -   Adjust voice parameters
    -   Generate expressive speech
    -   Play the audio

Example inputs:

I just got promoted!\
I am extremely angry right now\
I feel very sad today\
Oh wow, I didn't expect that!

------------------------------------------------------------------------

## 🛠️ Tech Stack

 | Technology   |              Purpose |
  |-------------------------- |------------------- |
  | Python                    | Core programming |
  | Flask                     | Web API |
  | HuggingFace Transformers  | Emotion detection |
  | Edge-TTS                  | Speech synthesis |
  | HTML/CSS/JS               | Web interface |

------------------------------------------------------------------------

## 👨‍💻 Author

Shubham Soni\
BTech Engineering Student\
AI / Machine Learning Enthusiast
