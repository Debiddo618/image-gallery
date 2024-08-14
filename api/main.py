import requests
import os
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS

# Add all the variables in .env.local to the os.environment
load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL='https://api.unsplash.com/photos/random'
UNSPLASH_KEY=os.environ.get("UNSPLASH_KEY","")
DEBUG=bool(os.environ.get("DEBUG",True))

if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and insert there UNSPLASH_KEY")

app = Flask(__name__)
CORS(app)
app.config["DEBUG"]=DEBUG

@app.route("/new-image")
def new_image():
    # Get the word from the URL
    word = request.args.get("query")

    # Set the header (see UNSPLASH DOCS)
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_KEY}",
        "Accept-Version": "v1"
    }

    # Set the params
    params = {
        "query" : word
    }

    # Send a request to the URL
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)

    # Change response to json format
    data = response.json()

    return data
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)