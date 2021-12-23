from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)




@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = dt.date.today().year
    return render_template("index.html", num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    name_params = {
        "name": name,
    }
    age_response = requests.get(url="https://api.agify.io/", params=name_params)
    gender_response = requests.get(url="https://api.genderize.io/", params=name_params)
    age_data = age_response.json()["age"]
    gender_data = gender_response.json()["gender"]
    return render_template("guess.html", nam=name.capitalize(), age=age_data, gend=gender_data)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


