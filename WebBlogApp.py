# import the Flask class from the flask module
from flask import Flask, render_template
import os
import markdown
import sql_comm_class

# create global application objects
app = Flask(__name__)

# reads in a file and returns the text
def read_post(blogfile):
    with open(blogfile,"r") as file:
        blog_md = file.read()

    return blog_md

# converts a markdown string into html
def md_html(blogfile):
    md = markdown.Markdown()
    blog_md = read_post(blogfile)
    blog_html = md.convert(blog_md)

    return blog_html

# read files in a directory into an array
def read_files(posts_path):
    blog_files = os.listdir(posts_path)

    return blog_files

# use decorators to link the function to a url
@app.route('/')
def home():
    
    posts_folder = "posts/"
    posts_div_head = '<div class="blog-post">'
    posts_div_tail = '</div>'
    blog_files = read_files(posts_folder)
    blog_post = ""
    for i in blog_files:
        blog_post += posts_div_head
        blog_post += md_html(posts_folder+i)
        blog_post += posts_div_tail
    return render_template("index.html",blog_post=blog_post)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
