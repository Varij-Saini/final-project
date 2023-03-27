
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__, template_folder="templates")

class Database:
    def __init__(self):
        host = "richardinfr.mysql.pythonanywhere-services.com"
        user = "richardinfr"
        pwd = "infr3810"
        db = "richardinfr$2023"

        self.con = pymysql.connect(host=host, user=user, password=pwd,
                    db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def insert(self, id, name, age):
        self.cur.execute("insert into student (id, name, age) values (%s, %s, %s)", (id, name, age))
        self.con.commit()
        self.con.close()
        return 'It worked!!!!'

    def query(self):
        self.cur.execute("select id, name, age from student")
        result = self.cur.fetchall()
        self.con.close()
        return result


@app.route('/')
def hello():
    return 'THis is INFR3810!!!'


@app.route('/login')
def login():
    return 'This is my login function'

@app.route('/dynamic', methods=['GET', 'POST'])
def dyn():
    var1 = 'INFR3810'

    if request.method == "POST":
        data = request.form
        name = data['name']
        return name

    return render_template('form.html', myvar=var1)

@app.route('/register', methods=['GET', 'POST'])
def register():
    result=""
    if request.method=='POST':
        data = request.form
        id = data['id']
        name = data['name']
        age = data['age']

        db = Database()

        result = db.insert(id, name, age)

    return render_template('register.html', msg=result)

@app.route('/list')
def select():
    db = Database()
    result = db.query()
    return render_template('results.html', data=result,
            content_type='application/json')


