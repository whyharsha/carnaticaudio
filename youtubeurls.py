from secrets import API_KEY, CLIENT_ID, CLIENT_SECRET
import pandas as pd
import requests

url = "https://www.googleapis.com/youtube/v3/search"

def call_youtube():
    results = []
    ragas = list_ragas()

    for raga in ragas:
        params = {
            "part": "snippet",
            "maxResults": 100,
            "q": raga,
            "type": "video",
            "key": API_KEY
        }
    
        response = requests.get(url, params)

        if not response.status_code == 200:
            print(response)
        else:
            results = parse_response(results, raga, response.json())
    
    if len(results) > 0:
        df = pd.DataFrame(results)
        df.to_csv('youtubeurls.csv', index = False)

def list_ragas():
    ragas = []

    ragas.append("Kapi ragam")
    ragas.append("Mayamalavagowla")
    ragas.append("Harikambhoji")
    ragas.append("Kharaharapriya")
    ragas.append("Nattai ragam")
    ragas.append("Bilahari ragam")
    ragas.append("Charukesi")
    ragas.append("Abheri ragam")
    ragas.append("Kamas ragam")
    ragas.append("Behag")

    return ragas

def parse_response(results, ragam, data):
    for item in data["items"]:
        record = {'ragam': ragam,
                  'video_id': item["id"]["videoId"], 
                  'title': item["snippet"]["title"], 
                  'desc': item["snippet"]["description"]}
        results.append(record)

    return results

if __name__ == "__main__":
    call_youtube()
else:
    print("Well, you are importing this, aren't you?")