from flask import Flask, render_template
import requests
app = Flask(__name__)

blog_url = "https://api.npoint.io/ceeb4145c9335d46329f"


@app.route('/')
def home():
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<num>')
def post(num):
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("post.html", number = int(num), posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)