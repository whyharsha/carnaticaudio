import youtube_dl
import pandas as pd

url_file = "youtubeurls.csv"

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav'
    }],
    'progress_hooks': [my_hook],
}

def get_audio_files():
    urls = load_urls()

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

def load_urls():
    df = pd.read_csv(url_file)
    return [f"https://www.youtube.com/watch?v={vid}" for vid in df['video_id']]

if __name__ == "__main__":
    get_audio_files()
else:
    print("Well, you are importing this, aren't you?")