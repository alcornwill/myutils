from pydub import AudioSegment
from os.path import splitext
from os import listdir, getcwd

def mp3_to_wav():
    for file in listdir(getcwd()):
        fn, ext = splitext(file)
        if ext != '.mp3': continue
        sound = AudioSegment.from_mp3(file)
        sound.export(fn + '.wav', format='wav')

def wav_to_ogg():
    for file in listdir(getcwd()):
        fn, ext = splitext(file)
        if ext != '.wav': continue
        sound = AudioSegment.from_wav(file)
        sound.export(fn + '.ogg', format='ogg')
        
def stereo_to_mono(input, output):
    sound = AudioSegment.from_wav(input)
    sound = sound.set_channels(1)
    sound.export(output, format="wav")