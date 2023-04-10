from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = "DuaCuEifyNh8i0cjdYoGt6du82vYVxD3KwaR5sqSxiElaBERgiFgZttg"
ENDPOINT = "https://api.pexels.com/v1/curated"


def get_photo_urls(query):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": API_KEY}
    params = {"query": query, "per_page": 3}
    response = requests.get(url, headers=headers, params=params)
    photos = response.json()["photos"]
    photo_urls = [
        f"https://images.pexels.com/photos/{photo['id']}/pexels-photo-{photo['id']}.jpeg"
        for photo in photos
    ]
    return photo_urls


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["search"]
        photo_urls = get_photo_urls(query)
        return render_template("results.html", photo_urls=photo_urls)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
