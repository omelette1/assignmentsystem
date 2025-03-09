import mysql.connector

my_db=mysql.connector.connect(
    host="192.168.50.212",
    user="class_user",
    password="password",
    database="Registration"
)

def add_user(name, address):
    cursor=my_db.cursor()
    sql="INSERT INTO users (name, address, age) VALUES (%s, %s, %s)"
    vals = (names, address, age)
    cursor.executes(sql, vals)
    my_db.commit()

def login(email, password):
    cursor = my_db.cursor(dictionary = True) 
    email = request.json.get("email")
    if email is None or password is None:
        return "email and password are required"
    sql = "SELECT * FROM users WHERE email = %s and pass = %s"
    val = (email,password)
    cursor.execute(sql,val)
    user = cursor.fetchone()
    if user is None:
        return "InValid email or password"
    return "Welcome " + user("name")

def get_users():
    cursor = my_db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def get_user_by_name(name):
    cursor=my_db.cursor(dictionary=True)
    sql="SELECT * FROM users WHERE name= %s"
    val = (name, )
    cursor.execute(sql, val)
    return curspr.fetchone()
def get_user_by_id(id):
    cursor = my_db.cursor(dictionary=True)
    sql="SELECT * FROM users WHERE id = %s"
    val = (id, )
    cursor.excute(sql, val)
    return cursor.fetchone()
def update_address_on_user(id, address):
    cursor = my_db.cursor()
    sql = "UPDATE users SET address = %s WHERE id = %s"
    val = (address, id)
    my_db.commit()
    return "address updated"

def delete_user(id):
    cursor= my_db.cursor()
    sql= "DELETE FROM users WHERE id = %s"
    val = 

if my_db.is_connected():
    print("successfully connected to mysql")
else:
    print("connection failed")