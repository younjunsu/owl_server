from cub_owl import app
import CUBRIDdb
db = CUBRIDdb.connect('CUBRID:localhost:33000:owlDB:::','owl','owladmin')
cursor = db.cursor()
query="SELECT /* owl web application connection test */ 1"
cursor.execute(query)
row = cursor.fetchone()
cursor.close()
db.close()

if row:
    app.run(debug=True,host='localhost', port=8080)
else:
    print("DB can not connection")
