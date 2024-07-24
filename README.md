# Lip-Sync
## Project Overview
LipSyncer Video is an advanced AI model designed to synchronize lip movements with spoken audio in video content. This model leverages state-of-the-art deep learning techniques to ensure accurate and realistic lip synchronization, enhancing the visual appeal and coherence of video productions.
## Features
- <b>High Precision Lip Syncing:</b> The model achieves high accuracy in matching lip movements to the audio, ensuring natural and believable speech animation.
- <b>Multi-Language Support:</b> Supports multiple languages, allowing for broad applicability across different regions and languages.
- <b>Robust to Audio Variations:</b>  Handles various audio qualities and speaking styles, maintaining performance across different audio sources.
## Tech Stack

<p align="left"> 
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .icon-container {
      display: flex;
      align-items: center;
      gap: 10px; /* Adjust spacing between items as needed */
    }
    .icon-container div {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  </style>
</head>
<body>
  <div class="icon-container">
    <div>
      <a href="https://pypi.org/project/pydub/" target="_blank" rel="noreferrer">
        <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" alt="pydub" width="40" height="40"/>
      </a>
      <p>Pydub</p>
    </div>
    <div>
      <a href="https://pypi.org/project/noisereduce/" target="_blank" rel="noreferrer">
        <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" alt="noisreduce" width="40" height="40"/>
      </a>
      <p>noisereduce</p>
    </div>
    <div>
      <a href="https://librosa.org/" target="_blank" rel="noreferrer">
        <img src="https://avatars.githubusercontent.com/u/18124827?s=200&v=4" alt="librosa" width="40" height="40"/>
      </a>
      <p>librosa</p>
    </div>
    <div>
      <a href="https://www.ffmpeg.org/" target="_blank" rel="noreferrer">
        <img src="https://img.icons8.com/?size=512&id=32418&format=png" alt="FFmpeg" width="40" height="40"/>
      </a>
      <p>FFmpeg</p>
    </div>
  </div>
</body>
</html>


# Getting Started
## Prerequisites
What things you need to install the software and how to install them:
```py
python >= 3.10
librosa
noisereduce
pydub
MuseTalk Requirements
```
You can install the required Python packages using:
```bash
pip install -r requirements.txt
```
## Installation
A step-by-step series of commands that tells you how to get a development environment running.

Clone the repository:
```bash
git clone https://github.com/maher-mohsen/LipSyncDiverge.git
```
Navigate into the project directory:
```cmd
cd LipSyncDiverge
```
Install the dependencies:
```cmd
pip install -r requirements.txt
```
## Prepare MuseTalk Environment
Follow official repo to setup environemnt
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <div class="icon-container">
    <div>
      <a href="https://github.com/TMElyralab/MuseTalk/tree/main" target="_blank" rel="noreferrer">
        <img src="https://avatars.githubusercontent.com/u/163981778?s=48&v=4" alt="MuseTalk" width="40" height="40"/>
      </a>
      <p>MuseTalk</p>
    </div>
  </div>
</body>
</html>

```
Note : All you have to do is setup requried dependencies for MuseTalk and Download following models weights [musetalk, dwpose, sd-vae-ft-mse] and move it to ./MuseTalk/models/model_name
```
## Running Inference
Instructions on how to run the model to segment furniture in new images.
```cmd
python run_model.py --video /path/to/video.mp4 --audio /path/to/audio.wav
```
# Authors
- Maher Mohsen <a href="https://github.com/maher-mohsen">maher-mohsen</a>

# Acknowledgments
- Hat tip to anyone whose code was used, specially <b>MuseTalk</b> guys!
- This project presented for <b>Diverge</b>

