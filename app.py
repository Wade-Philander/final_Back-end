from flask import Flask, render_template, request, jsonify
import sqlite3
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def create_database_tables():
    connection = sqlite3.connect('Users.db')
    print("Databases has opened")

    connection.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER, username TEXT)")
    print("Created user table successfully")
    connection.close()
    # cursor = connection.cursor()
    # cursor.execute('')
    # cursor.execute()
    #cursor = sql.commit()
create_database_tables()

#*******************************************  ADD NEW USER  ******************************************************************


@app.route('/add-new-user/', methods=['POST'])
def new_user():
    if request.method =="POST":
        
        msg = None

        try:
            name = request.form['name']
            username = request.form['username']
            password = request.form['password']
            city = request.form['city']

            with sqlite3.connect('Users.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO users(name, username, password, city) VALUES (?, ?, ?, ?)", (name, username, password, city))
                con.commit()
                msg = name = "was successfully added to the database."
                print("New user has been added")

        except Exception as e:
            con.rollback()
            msg = "Error occurred: " +str(e)

        finally:
            con.close()
            return jsonify (msg = msg)


#**************************************************  SHOW USERS DATABASE  **************************************************************

@app.route('/show-users/', methods=["GET"])

def show_users():
    records = []
    try:
        with sqlite3.connect('Users.db') as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            cur.execute("SELECT * From users")
            records = cur.fetchall()
            print("Here are the users")

    except Exception as e:
        con.rollback()
        print("There was an error fetching users: " +str(e))

    finally:
        con.close()
        return jsonify (records)

#*************************************LOGIN PAGE*********************************************************
#*************************************LOGIN PAGE********************************************************

@app.route('/login-user/', methods=['GET'])

def login():
    try:
        username = request.form['username']
        password = request.form['password']

        con = "select * from users where username = ? and password = ?"
        mycursor.execute(con, [(username),(password)])
        result = mycursor.fetchall()

        if user:
            for i in user:
                login_user()
                print("Logged in successfully")
        else:
            print("Error in verify function")
            pass

    except Exception as e:
        con.rollback()
        print("Please enter a existing user username and password") + str(e)
    finally:
        con.close()

        return 

# def login_user():
#     # get form data
#     # check db 
#     pass
