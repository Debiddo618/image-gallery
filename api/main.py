import requests
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client


# Create a new database called "gallery"
gallery = mongo_client.gallery

# Create a new collection called "images"
images_collection = gallery.images

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
    
@app.route("/images", methods=["GET", "POST"])
def images():
        # Read images from the database
        if request.method == "GET":
            images = images_collection.find({})
            return jsonify([img for img in images])
             
        # Save images from the database
        if request.method == "POST":
            image = request.get_json()       
            image["_id"]= image.get("id")
            result = images_collection.insert_one(image)
            inserted_id = result.inserted_id
            return {"inserted_id": inserted_id}  
        
@app.route("/images/<image_id>", methods=["DELETE"])
def image(image_id):
    result = images_collection.delete_one({"_id":image_id})
    print(result)
    if not result:
         return {"error":"Image wasn't deleted. Please try again"}, 500
    if result and not result.deleted_count:
        return {"error":"Image not found"}, 404 
    return {"deleted_id":image_id}, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)