import os
import http.client
from config import app
from urllib.parse import quote #replace spaces with %20
# from dotenv import load_dotenv


def fetchdata(params,limit):
   
    # api_key=os.getenv("API_KEY")
    conn = http.client.HTTPSConnection("exercisedb.p.rapidapi.com")

    headers = {
    'X-RapidAPI-Key': app.config['API_KEY'],
    'X-RapidAPI-Host': "exercisedb.p.rapidapi.com"
}

    conn.request("GET", f"/exercises/bodyPart/{quote(params)}?limit={limit}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    # print(data.decode("utf-8"))
    return data.decode("utf-8")


