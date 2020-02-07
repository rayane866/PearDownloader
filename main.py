import requests
import json
import os


with open("download_settings.json", "r") as json_file:
    settings = json.load(json_file)

def download(url=settings["url"], file_name=settings["file_name"], download_dir=settings["download_dir"]):
    doc = requests.get(url)
    with open(download_dir+ "\\"+ file_name, "wb") as f:
        f.write(doc.content)
    

download()
