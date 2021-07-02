from tube_dl import Youtube, extras
import pandas as pd

url_file = "youtubeurls.csv"

def get_audio_files():
    urls = load_urls()

    for url in urls:
        title = url["title"]
        vid = Youtube(url["url"]).formats.filter_by(only_audio=True)[0]
        form = vid.download(file_name=title)
        extras.Convert(form,add_meta=False)

def load_urls():
    df = pd.read_csv(url_file)
    return [{"title": row[0] + "-" + row[2], "url":  f"https://www.youtube.com/watch?v={row[1]}"} for row in zip(df['ragam'], df['video_id'], df['title'])]

if __name__ == "__main__":
    get_audio_files()
else:
    print("Well, you are importing this, aren't you?")