from flask import Flask, jsonify, request
from flask_cors import CORS  # Import the CORS module
import requests
import os
from dotenv import load_dotenv
#from urllib.parse import quote
from flask_caching import Cache

from flask_cors import CORS  # Import the CORS module

app = Flask(__name__)
CORS(app, resources={r"/get_news": {"origins": "*"}})


# Configure Flask-Caching
cache = Cache(app, config={'CACHE_TYPE': 'simple', 'CACHE_DEFAULT_TIMEOUT': 300})

load_dotenv()

@app.route('/get_news', methods=['GET'])
@cache.cached()  # Cache the result for the default timeout (300 seconds)
def get_news():
    api_key = os.environ.get('api')

    if not api_key:
        return jsonify({'error': 'News API key not found. Set the api environment variable.'}), 500
    print('REQUEST by yashas'+str(request))
    search_input = request.args.get('search', '').strip()

    if not search_input:
        return jsonify({'error': 'Search input is empty or contains only whitespace.'}), 400
    
    print("Search"+search_input)
    
    base_url = "https://newsapi.org/v2/everything"
    params = {
        'q': 'accident',
        'from': '2024-01-28',
        'sortBy': 'latest',
        'pageSize': '20',
        'apiKey': api_key
    }
    
    #search_input_encoded = quote(search_input)
    # Modify the URL to include the pageSize parameter
    
    try:
        response = requests.get(base_url,params=params)
        response.raise_for_status()  # Check for errors in the response
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f"Error fetching data from News API: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
