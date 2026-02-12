import requests
from dotenv import load_dotenv
import os
from supadata import Supadata, SupadataError

#Openrouter Credentials
load_dotenv()
url = "https://openrouter.ai/api/v1/chat/completions"
Openrouter_API_KEY = os.getenv("Openrouter_API_KEY")
System_Prompt = os.getenv("System_Prompt")
Supadata_API_KEY=os.getenv("Supadata_API_KEY")

def Vid_Cat(Vid_Transcript):    
    
    #API Request
    headers = {
        "Authorization": f"Bearer {Openrouter_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-oss-120b:free",   # change to any model you want
        "messages": [
        {"role": "system", "content": System_Prompt},
        {"role": "user", "content": Vid_Transcript}
    ]
    }

    #Response parsing & output
    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    return(result["choices"][0]["message"]["content"])

def Get_Transcript(Vid_URL):
    # Initialize the client
    supadata = Supadata(api_key=Supadata_API_KEY)

    # Get transcript from any supported platform (YouTube, TikTok, Instagram, X (Twitter), file URLs)
    transcript = supadata.transcript(
        url=Vid_URL,
        text=True,  #return plain text instead of timestamped chunks
        mode="auto"
    )
    return(transcript.content)

Vid_URL=input()
Vid_Transcript=Get_Transcript(Vid_URL)
Vid_Category = Vid_Cat(Vid_Transcript)
print (Vid_Category)