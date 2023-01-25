#this program is for crud operation in postgresql database
from flask import *
import psycopg2
connection=psycopg2.connect(user="postgres",database="bubtlab",password="sad@2600")
app = Flask(__name__,template_folder='temp')
@app.route('/')
def index():
    cur = connection.cursor()
    cur.execute("SELECT * FROM person")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html',data=data)
@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cur = connection.cursor()
        cur.execute("INSERT INTO person(name,age) VALUES(%s,%s)",(name,age))
        connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('index.html')
@app.route('/update/<string:id>',methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cur = connection.cursor()
        cur.execute("UPDATE person SET name=%s,age=%s WHERE id=%s",(name,age,id))
        connection.commit()
        cur.close()
        return redirect(url_for('index'))
    cur = connection.cursor()
    cur.execute("SELECT * FROM person WHERE id=%s",(id,))
    data = cur.fetchall()
    cur.close()
    return render_template('update.html',data=data)
@app.route('/delete/<string:id>',methods=['GET'])
def delete(id):
    cur = connection.cursor()
    cur.execute("DELETE FROM person WHERE id=%s",(id,))
    connection.commit()
    cur.close()
    return redirect(url_for('index'))
app.run(debug=True)