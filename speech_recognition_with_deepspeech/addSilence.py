from pydub import AudioSegment
from pydub.silence import detect_silence,detect_nonsilent,split_on_silence

no_voice=AudioSegment.silent(duration=1000,frame_rate=16000)
voice=AudioSegment.from_mp3("/home/zoirasu/ses/turkce.mp3")

last_voice=no_voice+voice+no_voice

last_voice.export("/home/zoirasu/ses/last_voice.mp3",format="mp3",bitrate="192k")

