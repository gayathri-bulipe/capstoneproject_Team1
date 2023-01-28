import mysql.connector
class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
           self.connection=mysql.connector.connect(host=self.host,database=self.db,user=self.user,password=self.password)
        except:
            print("error while connecting to the database")

    def insert_data(self,filename):
        self.filename=filename

        self.cur=self.connection.cursor()
        sql="insert into files(filename) values(%s);"
        val=(self.filename)
        self.cur.execute(sql,(val,))
        self.connection.commit()

    def search(self):
        self.cur=self.connection.cursor()
        sql="SELECT * from files limit 0,10"
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data
    def searchDB(self,files):
        self.cur = self.connection.cursor()

        sql=""" select * from files where filename like '%{0}'""".format(files)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row==0:
            return
        else:
            print(row)

dbobj=Mysql_DBaccess('localhost','root','Gayathri@123','searchfiles')

#dbobj.insert_data('C:/hcl1/filename1.txt')
dbobj.searchDB("C://hcl1//filename1.txt")
