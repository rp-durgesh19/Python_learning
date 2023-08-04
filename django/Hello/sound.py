import sounddevice
from scipy.io.wavfile import write
fs=44100

second=int(input("Enter the Recoding Time In Second: "))
print("Recoding.....\n")
record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()
write("My recoding.wav ",fs,record_voice)
print("Recoding is done please check your folder to listen recoding")
