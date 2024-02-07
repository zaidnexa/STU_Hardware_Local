import RPi.GPIO as GPIO
import pyaudio
import wave
import os

# Setup
button_pin = 29
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = None
is_recording = False

def toggle_recording(channel):
    global stream, is_recording
    
    input_device_index = 2


    if not is_recording:
        # Start recording
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024, input_device_index=input_device_index)
        is_recording = True
        print("Recording Started")
    else:
        # Stop recording and save
        stream.stop_stream()
        stream.close()
        is_recording = False
        print("Recording Stopped")
        # Save the recording as needed

# Add event detection
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=toggle_recording, bouncetime=300)

try:
    # Keep your main thread alive or your program will exit
    while True:
        pass
except KeyboardInterrupt:
    print("Program stopped")
finally:
    GPIO.cleanup()
    audio.terminate()
