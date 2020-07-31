# import the Flask class from the flask module
from flask import Flask, render_template
import os
import markdown
import sql_com_class

# create global application objects
app = Flask(__name__)


# converts a markdown string into html
def md_html(blog_md):
    md = markdown.Markdown()
    blog_html = md.convert(blog_md)

    return blog_html

# read files in a directory into an array
def read_files(posts_path):
    blog_files = os.listdir(posts_path)

    return blog_files

# use decorators to link the function to a url
@app.route('/')
def home():
    
    posts_div_head = '<div class="blog-post">'
    posts_div_tail = '</div><hr>'
    blog_post = ""

    data = sql_com_class.database()
    data.connect()

    tables_list = data.returnTables()
    for i in range(len(tables_list)):
        table_data = data.returnTableValues(tables_list[i])
        blog_post += posts_div_head
        blog_post += md_html(table_data[3])
        blog_post += posts_div_tail

    return render_template("index.html",blog_post=blog_post)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
