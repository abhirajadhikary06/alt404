import os
import google.generativeai as genai
import json
import logging
import re
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

try:
    genai.configure(api_key=api_key)
except Exception as e:
    raise ValueError(f"Failed to configure Gemini API: {str(e)}")

def get_alternatives(website_name):
    try:
        # Configure Gemini model
        model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
        
        # Construct prompt
        prompt = f"""
        Suggest exactly 3 free alternatives to {website_name}. 
        Return the response in JSON format as a list of dictionaries: 
        [{{"name": "site_name", "link": "site_url"}}, {{"name": "site_name", "link": "site_url"}}, {{"name": "site_name", "link": "site_url"}}].
        Ensure the response is valid JSON and contains exactly 3 entries.
        """
        logger.debug(f"Prompt sent to Gemini API: {prompt}")
        
        # Generate response
        response = model.generate_content(prompt)
        
        # Log raw response
        response_text = response.text.strip()
        logger.debug(f"Raw Gemini API response: {response_text}")
        
        # Remove code fences if present
        if response_text.startswith('```') and response_text.endswith('```'):
            response_text = response_text[3:-3].strip()
            if response_text.startswith('json'):
                response_text = response_text[4:].strip()  # Remove 'json' if present
            logger.debug(f"Response after removing code fences: {response_text}")
        
        # Parse response
        try:
            alternatives = json.loads(response_text)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {str(e)}")
            # Fallback: attempt to extract JSON-like content with regex
            json_match = re.search(r'\[\s*\{.*?\}\s*\]', response_text, re.DOTALL)
            if json_match:
                logger.debug("Attempting regex-based JSON extraction")
                try:
                    alternatives = json.loads(json_match.group(0))
                except json.JSONDecodeError as e:
                    logger.error(f"Regex JSON parsing failed: {str(e)}")
                    return []
            else:
                logger.error("No JSON-like content found in response")
                return []
        
        # Convert dictionary to list of dictionaries if necessary
        if isinstance(alternatives, dict):
            logger.debug("Converting dictionary to list of dictionaries")
            alternatives = [{'name': name, 'link': link} for name, link in alternatives.items()]
        
        # Validate response format
        if not isinstance(alternatives, list):
            logger.error("Response is not a list")
            return []
        
        if len(alternatives) != 3:
            logger.warning(f"Expected 3 alternatives, got {len(alternatives)}")
        
        for alt in alternatives:
            if not isinstance(alt, dict) or 'name' not in alt or 'link' not in alt:
                logger.error(f"Invalid alternative format: {alt}")
                return []
        
        logger.debug(f"Parsed alternatives: {alternatives}")
        return alternatives
    except Exception as e:
        logger.error(f"Failed to get alternatives from Gemini API: {str(e)}")
        return []