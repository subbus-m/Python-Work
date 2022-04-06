from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/mysqlapi', methods=['POST','GET'])
def mysql1():
    import mysql.connector as conn
    mydb = conn.Connect(host='localhost', user='root', psswd='mysql')
    if (request.method == 'GET'):
        cursor.execute('use testsudhineuron')
        cursor.execute('select * from testsudhineuron.ineuron1')
        result = cursor.fetchall()
        return jsonify(str(result))

if __name__ == '__main__':
        app.run()