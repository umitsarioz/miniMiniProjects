import pyaudio
import math
import struct
import wave
import sys

#Assuming Energy threshold upper than 30 dB
Threshold = 30

SHORT_NORMALIZE = (1.0/32768.0)
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
swidth = 2
Max_Seconds = 5
TimeoutSignal=((RATE / chunk * Max_Seconds) + 1)
silence = True
FileNameTmp = '/home/zoirasu/ses/deneme37.wav'
Time=0
all =[]

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = True,
    frames_per_buffer = chunk)

def GetStream(chunk):
    return stream.read(chunk)
def rms(frame):
    count = len(frame)/swidth
    format = "%dh"%(count)
    # short is 16 bit int
    shorts = struct.unpack( format, frame )

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n
    # compute the rms
    rms = math.pow(sum_squares/count,0.5)
    return rms * 1000

def WriteSpeech(WriteData):
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(FileNameTmp, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(WriteData)
    wf.close()

def KeepRecord(TimeoutSignal, LastBlock):
    all.append(LastBlock)
    for i in range(0, int(TimeoutSignal)):
        try:
            data = GetStream(chunk)
        except:
            continue
        all.append(data)

    print ("Sessizik tespit edildi..")
    data = (b''.join(all))
    print ("Dosyaya yazılıyor..")
    WriteSpeech(data)
    silence = True
    Time=0 #süre sıfırlanarak tekrar çalıştırılıyor..
    listen(silence,Time)

def listen(silence,Time):
    print ("Ses bekleniyor..")
    while silence:
        try:
            input = GetStream(chunk)
            rms_value = rms(input)
            if (rms_value > Threshold):
                silence = False
                LastBlock = input
                print("Ses algilandi kayittasin...!")
                KeepRecord(TimeoutSignal, LastBlock)
            Time = Time + 1
        except:
            continue
        if(Time > TimeoutSignal):
         sys.exit()
        if KeyboardInterrupt:
            break;



listen(silence,Time)
