import pyaudio
import wave

class grabadora():
    def recording():
        chunk = 1024  
        sample_format = pyaudio.paInt16  
        chanels = 2
        smpl_rt = 44100 
        seconds = 4
        filename = "path_of_file.wav"
        pa = pyaudio.PyAudio()
        stream = pa.open(format=sample_format, channels=chanels,  
                 rate=smpl_rt, input=True,  
                 frames_per_buffer=chunk) 
        frames = []
        for i in range(0, int(smpl_rt / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        pa.terminate()