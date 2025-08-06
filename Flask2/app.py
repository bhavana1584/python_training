from flask import Flask, render_template
from flask_mysqldb import MySQL

# create object for flask
app = Flask(__name__)


@app.route("/", methods=["GET"])
def template():
    return render_template('index.html')


@app.route("/index", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')


@app.route("/blog", methods=['GET'])
def blog():
    return render_template('blog.html')


@app.route("/grid", methods=['GET'])
def grid():
    return render_template('grid.html')


@app.route("/masonry", methods=['GET'])
def masonry():
    return render_template('masonry.html')


@app.route("/single-post", methods=['GET'])
def singlePost():
    return render_template('single-post.html')


# connecting database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'bhavana_ece'

mysql = MySQL(app)

# fetching data from the database


@app.route('/user_detail')
def userDetail():
    sql = "SELECT * FROM user"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    cur.close()
    return render_template("index.html", results=results)


if __name__ == 'main':
    app.run()
