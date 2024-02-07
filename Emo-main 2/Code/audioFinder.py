import pyaudio

audio = pyaudio.PyAudio()

print("Available audio devices:")
for index in range(0, audio.get_device_count()): 
    info = audio.get_device_info_by_index(index)
    print(f"Index: {index}, Name: {info['name']}, Input Channels: {info['maxInputChannels']}")

audio.terminate()
