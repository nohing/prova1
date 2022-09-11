from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)            # __main__ è il nome di app

@app.route('/')
def my_outer_space():
    return render_template("index.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/works.html')
def works():
    return render_template("works.html")

@app.route('/work.html')
def work():
    return render_template("work.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/components.html')
def components():
    return render_template("components.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

# @app.route('/blog')
# def blog():
#     return "That's my blog1!!!"
#
#
# @app.route('/blog/2022/animals')
# def blog2():
#     return "That's my beast!!!"