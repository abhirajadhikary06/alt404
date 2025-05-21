# Alt404

**Alt404** is a Flask-based web application that empowers users to discover free alternatives to any website by simply entering its URL. Powered by the Gemini 2.5 Flash API, Alt404 extracts the website name, suggests the top three free alternative websites, and displays each with its name, logo, and clickable link in a clean, responsive interface. Whether the input URL is active or broken, Alt404 delivers reliable results with logos fetched via the Clearbit Logo API and a favicon fallback.

## Features

- **Flexible URL Input**: Accepts website URLs with or without `http://` or `https://` (e.g., `example.com`, `www.notion.so`, or `https://leetcode.com`).
- **AI-Powered Suggestions**: Uses the Gemini 2.5 Flash API to generate three free alternative websites in JSON format.
- **Logo Integration**: Fetches website logos using the Clearbit Logo API, with a fallback to Google’s favicon service for robust display.
- **Responsive UI**: Displays results in a modern, user-friendly interface built with HTML, CSS, and Flask templates.
- **Robust Error Handling**: Gracefully handles invalid URLs, API errors, and non-JSON responses, ensuring a seamless user experience.
- **Debugging Support**: Includes detailed logging for easy troubleshooting during development.

## Project Structure

```
alt404/
├── app.py                   # Flask app entry point
├── gemini.py                # Gemini API integration
├── utils.py                 # Utility functions for URL parsing
├── templates/
│   └── index.html           # Frontend UI template
├── static/
│   └── styles.css           # Styling for the frontend
├── .env                     # Environment variables (API keys, not in repo)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Prerequisites

- **Python 3.8+**: Ensure Python is installed.
- **Gemini API Key**: Obtain a key from [xAI's API portal](https://x.ai/api).
- **Git**: For cloning the repository.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abhirajadhikary06/alt404.git
   cd alt404
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root with your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`.

## Usage

1. Open `http://localhost:5000` in your browser.
2. Enter a website URL (e.g., `example.com`, `https://notion.so`, or `www.leetcode.com`) in the input field.
3. Click **Find Alternatives** to view the top three free alternative websites, each displayed with a logo, name, and clickable link.
4. If an error occurs (e.g., invalid URL or API issue), a user-friendly message will be shown.

## Acknowledgments

- [xAI](https://aistudio.google.com) for the Gemini API.
- [Clearbit](https://clearbit.com) for the Logo API.
- [Flask](https://flask.palletsprojects.com) for the web framework.

---

For issues, feature requests, or questions, please open an issue on the [GitHub repository](https://github.com/abhirajadhikary06/alt404/issues). We’d love to hear your feedback!