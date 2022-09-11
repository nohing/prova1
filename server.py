from flask import Flask, render_template, url_for
app = Flask(__name__)
#print(__name__)            # __main__ è il nome di app

@app.route('/<username>/<int:post_id>')   # home route
def hello_world(username=None, post_id=None):
    #return 'Hello fuuuuuck!!!'     # http://127.0.0.1:5000/ è il local host, il computer in uso
     #print(url_for('static', filename='favicon.ico')) equivale a quello che c'è nel file html
     return render_template("index.html", name=username, post_id=post_id)

@app.route('/about.html')   # home route
def about():
    return render_template("about.html")

@app.route('/blog')
def blog():
    return "That's my blog1!!!"  # flask converte la strinfa in html


@app.route('/blog/2022/animals')
def blog2():
    return "That's my beast!!!"