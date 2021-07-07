import os
from pydub.utils import make_chunks
from pydub import AudioSegment

chunk_size = 60000 #millisecs
ragas = ['Kapi', 
         'Mayamalavagowla', 
         'Harikambhoji', 
         'Kharaharapriya', 
         'Nattai', 
         'Bilahari',
         'Charukesi',
         'Abheri',
         'Kamas',
         'Behag']

def split_audio_files():
    file_number = 0
    for file in os.listdir(os.getcwd()):
        if file.endswith(".mp3"):
            file_number = file_number + 1
            audio = AudioSegment.from_file(file, format="mp3")
            for i, chunk in enumerate(make_chunks(audio, chunk_size)):
                for j, ragam in enumerate(ragas):
                    if ragam in file:
                        filename = ragam + "-" + str(file_number) + "-" + str(i + 1) + ".wav"
                        print("exporting " + filename)
                        os.chdir(os.getcwd() + "/finaldata")
                        chunk.export(filename, format="wav")
                        os.chdir('../')

if __name__ == "__main__":
    split_audio_files()
else:
    print("Well, you are importing this, aren't you?")