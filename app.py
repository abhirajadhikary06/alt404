from flask import Flask, render_template, request
from gemini import get_alternatives
from utils import extract_website_name
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return render_template('index.html', error="Please provide a URL")
        
        try:
            # Extract website name from URL
            website_name = extract_website_name(url)
            
            # Get alternatives from Gemini API
            alternatives = get_alternatives(website_name)
            
            if not alternatives:
                return render_template('index.html', error=f"No alternatives found for {website_name}. Please try again.")
            
            # Add logo URLs to alternatives
            for alt in alternatives:
                domain = alt['link'].split('//')[-1].split('/')[0]
                alt['logo'] = f"https://logo.clearbit.com/{domain}"
                
            return render_template('index.html', alternatives=alternatives, website_name=website_name)
        except Exception as e:
            return render_template('index.html', error=f"Error processing request: {str(e)}")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)