from urllib.parse import urlparse

def extract_website_name(url):
    """
    Extract the website name from a URL, adding https:// if no protocol is provided.
    Example: 'example.com' -> 'example' or 'https://www.example.com/path' -> 'example'
    """
    try:
        # Add https:// if no protocol is present
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Parse the URL
        parsed_url = urlparse(url)
        
        # Check for valid netloc
        if not parsed_url.netloc:
            raise ValueError("Invalid URL provided")
        
        # Extract domain
        domain = parsed_url.netloc
        
        # Remove 'www.' prefix and '.com', '.org', etc.
        if domain.startswith('www.'):
            domain = domain[4:]
        website_name = domain.split('.')[0]
        
        return website_name.capitalize()
    except Exception as e:
        raise Exception(f"Failed to extract website name: {str(e)}")