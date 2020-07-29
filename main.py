"""
    pip3 install requests  beautifulsoup4 lxml pandas
    
"""
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

def Getjson(str):
    r = requests.get(str)
    return r


if __name__ == "__main__":
    str = 'https://api.netpie.io/feed/Rapoo?apikey=8YzoLCrqTRZXLv4YVW5IvmGJoEgXByuI&granularity=15minutes&since=1year&fbclid=IwAR2JA_UpUFyW_dvOpxG1s7QdB021EzpxXa7EDlM5vgnSwmBaN1ueOuo0DjQ'
    # Get text in String 
    StringText = Getjson(str)
    jsonContent = StringText.json() 
