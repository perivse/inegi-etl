import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
token = os.getenv("API_TOKEN")  # token on .env

# url = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/3105001001/es/070000{state}/true/BISE/2.0/{token}?type=json"

fulldata = [] # arr for data

for state in range(1,33):
    if state < 10:
        numstring = "0" + str(state)
        url = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/3105001001/es/070000{numstring}/true/BISE/2.0/{token}?type=json"    
    else: 
        url = f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/3105001001/es/070000{str(state)}/true/BISE/2.0/{token}?type=json"
    response = requests.get(url) # request api
    data = response.json() # json data 
    fulldata.extend(data)  # add data on arr 

df = pd.DataFrame(fulldata)
print(df)