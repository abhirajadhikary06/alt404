import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
website_name = "example.com"  # Replace with the actual website name you want to check
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

prompt = f"Suggest only top 3 free alternatives to {website_name} in Python list of dictionaries format [{{'name': 'link'}}]"
response = model.generate_content(prompt)
print(response.text)
