# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

def read_post(blogfile):
    with open(blogfile,"r") as file:
        blog_md = file.read()

    return blog_md

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
