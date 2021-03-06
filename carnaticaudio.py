
import youtube_dl
import pandas as pd

url_file = "youtubeurls.csv"

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def get_audio_files():
    urls = load_urls()

    count = 1
    ragam = ""

    for url in urls:
        if not url["ragam"] == ragam:
            count = 1
            ragam = url["ragam"]

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        filename = str(count) + url["ragam"] + "."
        ydl_opts.update({'outtmpl':filename})

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url["url"]])

        count = count + 1

def load_urls():
    df = pd.read_csv(url_file)
    return [{'ragam': ragam, 'url': f"https://www.youtube.com/watch?v={vid}"} for ragam, vid in zip(df['ragam'], df['video_id'])]

if __name__ == "__main__":
    get_audio_files()
else:
    print("Well, you are importing this, aren't you?")