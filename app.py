from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL

# create object for flask
app = Flask(__name__)

# routing to home page


@app.route('/')
def home():
    return render_template('home.html')

# rounting to about page


@app.route('/about')
def about():
    return render_template('about.html')

# routing to contact page


@app.route('/contact')
def contact():
    return render_template('contact.html')


# connecting to database
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
    return jsonify(results)


@app.route('/getData')
def getData():
    id = request.args.get("id")
    sql = ""
    if id is None:
        sql = "SELECT * FROM user"
    else:
        sql = f"SELECT * FROM user where id = {id}"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    cur.close()
    return jsonify(results)


# updating the table in the database
@app.route("/add", methods=["POST"])
def addUser():
    id = request.form['id']
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    contact = request.form['contact']
    country = request.form['country']
    cur = mysql.connection.cursor()
    sql = "insert into user(id,fname,lname,email,contact,country) values(%s,%s,%s,%s,%s,%s)"
    val = [id, fname, lname, email, contact, country]
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Registration Success"


@app.route('/sign_up', methods=['GET'])
def sign_up():
    return render_template('sign_up.html')


# update data in the table
@app.route("/update", methods=["POST"])
def updateUser():
    id = request.form['id']
    email = request.form['email']
    cur = mysql.connection.cursor()
    sql = "update user set email=%s where id=%s"
    val = [email, id]
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Update Successful"


@app.route('/update_user', methods=['GET'])
def update_user():
    return render_template('update_user.html')


# delete data from the table
@app.route("/delete", methods=["POST"])
def deleteUser():
    id = request.form['id']
    cur = mysql.connection.cursor()
    sql = "delete from user where id=%s"
    val = [id]
    cur.execute(sql, val)
    mysql.connection.commit()
    cur.close()
    return "Delete Successful"


@app.route('/delete_user', methods=['GET'])
def delete_user():
    return render_template('delete_user.html')


# render a webpage that uses template
@app.route('/myWeb1', methods=['GET'])
def myWeb1():
    return render_template('index1.html')


@app.route('/myWeb2', methods=['GET'])
def myWeb2():
    return render_template('index2.html')


if __name__ == '__main__':
    app.run()
