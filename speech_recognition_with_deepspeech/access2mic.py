import pyaudio
import wave
import time
from array import array

CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=16000
DURATION=5.0
WAVE_OUTPUT_FILENAME="/home/zoirasu/ses/callback.wav"

p=pyaudio.PyAudio() #init

frames=[]

stream=p.open(format=FORMAT,
              channels=CHANNELS,
              rate=RATE,
              input=True,
              frames_per_buffer=CHUNK,
              )
stream.start_stream()
while stream.is_active(): #stream'i aktif et
    time.sleep(0.2)
    print('Kayittasin..')
    try:            #mic al
     for i in range(0, int(RATE / CHUNK * DURATION )):
        data = stream.read(CHUNK)
        data_chunk=array('h',data)
        vol=max(data_chunk) #frames_per_buffer sese göre al 
        if(vol>=500):
            print("Ses algilandi..")
            frames.append(data)
        else:
           print("Ses yok..")
    except KeyboardInterrupt: #klavye interrupt olursa while'dan cık streami durdur ve bitir .
        break
print('Kayit bitti..')
stream.stop_stream()
stream.close()
p.terminate()

wf=wave.open(WAVE_OUTPUT_FILENAME,'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
