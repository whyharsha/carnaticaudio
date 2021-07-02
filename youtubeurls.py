from secrets import API_KEY, CLIENT_ID, CLIENT_SECRET
import pandas as pd
import requests

url = "https://www.googleapis.com/youtube/v3/search"
results = []

def call_youtube():
    
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
            parse_response(raga, response.json())
    
    if len(results) > 0:
        df = pd.DataFrame(results)
        df.to_csv('youtubeurls.csv', index = False)

def list_ragas():
    ragas = []

    ragas.append("Kapi ragam")
    ragas.append("Mayamalavagowla")
    ragas.append("Harikambhoji")
    ragas.append("Kharaharapriya")
    ragas.append("Keeravani")
    ragas.append("Sindhubhairavi")
    ragas.append("Charukesi")
    ragas.append("Abheri")
    ragas.append("Kamas")
    ragas.append("Behag")

    return ragas

def parse_response(ragam, data):
    for item in data["items"]:
        record = {'ragam': ragam,
                  'video_id': item["id"]["videoId"], 
                  'title': item["snippet"]["title"], 
                  'desc': item["snippet"]["description"]}

        results.append(record)