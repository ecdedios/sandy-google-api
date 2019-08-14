from flask import Flask, render_template, jsonify
import requests
from key import key
app = Flask(__name__)

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

@app.route("/", methods=["GET"])
def retrieve():
    return render_template('layout.html')

@app.route("/sendRequest/<string:query>")
def results(query):

    url = "https://www.google.com"
    return jsonify({'result' : url})

#     search_payload = {"key":key, "query":query}
#     search_req = requests.get(search_url, params=search_payload)
#     search_jason = saerch_req.json()

#     place_id = sedarch_json["results"][0]["place_id"]
    
#     details_payload = {"key":key, "placeid":place_id}
#     details_resp = requests.get(details_url, params=details_payload)
#     details_json = details_resp.json()

#     url = details_json["result"]["url"]
#     return jsonify({'result' : url})
    
    
if __name__ == "__main__":
    app.run(debug=True)