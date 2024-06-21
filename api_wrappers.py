import os
from googleapiclient.discovery import build
import requests

class GoogleSearchAPIWrapper:
    def __init__(self):
        self.service = build("customsearch", "v1", developerKey=os.getenv("GOOGLE_API_KEY"))
    
    def run(self, query):
        res = self.service.cse().list(q=query, cx=os.getenv("GOOGLE_CSE_ID")).execute()
        return res['items'][0]['snippet'] if 'items' in res else "No results found."

class OpenAQAPIWrapper:
    def __init__(self):
        self.base_url = "https://api.openaq.org/v2"
    
    def run(self, location):
        response = requests.get(f"{self.base_url}/latest", params={"city": location})
        return response.json()

class NOAAAPIWrapper:
    def __init__(self):
        self.base_url = "https://www.ncdc.noaa.gov/cdo-web/api/v2"
        self.headers = {"token": os.getenv("NOAA_API_KEY")}
    
    def run(self, dataset, start_date, end_date, location):
        params = {
            "datasetid": dataset,
            "startdate": start_date,
            "enddate": end_date,
            "locationid": location,
        }
        response = requests.get(f"{self.base_url}/data", headers=self.headers, params=params)
        return response.json()

class GBIFAPIWrapper:
    def __init__(self):
        self.base_url = "https://api.gbif.org/v1"
    
    def run(self, species):
        response = requests.get(f"{self.base_url}/species/match", params={"name": species})
        return response.json()
