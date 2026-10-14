from dotenv import load_dotenv
from requests import get
import os
load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)

response = get(f"https://api.example.com/data?api_key={api_key}")
print(response.json())