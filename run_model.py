import argparse
import shutil
import os
from pydub import AudioSegment
import noisereduce as nr
import numpy as np
import librosa
import yaml
import subprocess
HOME = os.getcwd()

def create_task_yamel():
   
    tasks = {
        'task_0': {
            'video_path': f'{HOME}/sample/video.mp4',
            'audio_path': f'{HOME}/sample/audio.wav'
        }
    }

    with open('infer.yaml', 'w') as file:
        yaml.dump(tasks, file, default_flow_style=False)

def preprocess(audio_path):
    output_path=f'{HOME}/sample/audio.wav'
    y, sr = librosa.load(audio_path, sr=None)

    # Perform noise reduction
    reduced_noise = nr.reduce_noise(y=y, sr=sr)

    # Convert the numpy array back to an AudioSegment
    audio = AudioSegment(
        (reduced_noise * (2**15 - 1)).astype(np.int16).tobytes(),
        frame_rate=sr,
        sample_width=2,
        channels=1
    )

    # Apply equalization (boost frequencies around 1000-3000 Hz for clearer phonetics)
    audio = audio + 15
    eq_audio = audio.low_pass_filter(3000).high_pass_filter(1000)

    # Export the processed audio to a new file
    eq_audio.export(output_path, format="wav")

def run_inference(audio, video):
    preprocess(audio)
    shutil.move(video, f'{HOME}/sample/video.mp4')
    create_task_yamel()
    command = ["python", "-m", "'./MuseTalk/scripts.inference'", "--inference_config", "--result_dir './results'","infer.yaml"]
    result = subprocess.run(command, capture_output=True, text=True)
    command = ["ffmpeg", "-i", "'./results/video.mp4'", "-c:v", "copy", "-map", "0:v:0", "-map", "1:a:0", "-shortest", "'./results/video.mp4'" ]
    result = subprocess.run(command, capture_output=True, text=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Enhanced MuseTalk Pipeline.')
    parser.add_argument('--video', type=str, help='Path to the video.mp4')
    parser.add_argument('--audio', type=str, help='Path to the audio.wav')

    args = parser.parse_args()
    run_inference(args.video, args.audio)
