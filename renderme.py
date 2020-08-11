# render a markdown so that we can see how it looks in html
import markdown
import sys

def md_html(md_txt):
    md = markdown.Markdown()
    html_txt = md.convert(md_txt)

    return html_txt

if __name__ == "__main__":
    md_file = open(str(sys.argv[1]),"r")
    new_file = open(str(sys.argv[2]),"x")
    md_txt = md_file.read()
    html_txt = md_html(md_txt)
    new_file.write(html_txt)
    print(html_txt)
    md_file.close()
    new_file.close()
