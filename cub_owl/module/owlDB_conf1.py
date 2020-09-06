import CUBRIDdb

class owlDB_conf1():
    def __init__(self):
        self.db = CUBRIDdb.connect('CUBRID:localhost:33000:owlDB:::','owl','owladmin')
        self.cursor = self.db.cursor()
    
    def execute(self, query):
        self.cursor.execute(query)
    
    def executeOne(self, query):
        self.cursor.execute(query)
        row = self.cursor.fetchone()
    
    def executeAll(self, query):
        self.cursor.execute(query)

    def commit(self):
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()
#        print(1)

