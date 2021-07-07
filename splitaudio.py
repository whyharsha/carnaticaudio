import os
from pydub.utils import make_chunks
from pydub import AudioSegment

chunk_size = 60000 #millisecs

def split_audio_files():
    for file in os.listdir(os.getcwd()):
        if file.endswith(".mp3"):
            audio = AudioSegment.from_file(file, format="mp3")
            for i, chunk in enumerate(make_chunks(audio, chunk_size)):
                os.chdir(os.getcwd() + "/finaldata")
                filename = file.removesuffix(".mp3") + str(i + 1) + ".wav"
                print("exporting " + filename)
                chunk.export(filename, format="wav")
                os.chdir('../')

if __name__ == "__main__":
    split_audio_files()
else:
    print("Well, you are importing this, aren't you?")