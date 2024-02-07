import subprocess
import os
import signal
import time

# Global variable to keep track of recording state and process
is_recording = False
arecord_process = None

def start_recording(filename):
    global arecord_process
    arecord_process = subprocess.Popen(['arecord', '-f', 'cd', '-t', 'wav', filename], preexec_fn=os.setsid)

def stop_recording():
    global arecord_process
    os.killpg(os.getpgid(arecord_process.pid), signal.SIGTERM)
    arecord_process = None



start_recording("recording_test.wav")
time.sleep(30)
stop_recording()


