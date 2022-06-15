from colorama import Cursor
import mysql.connector


def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="aroon wanthong",
    )
    return mydb

class Con:
    def getHW():
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM hard_ware"

        mycursor.execute(sql)

        data = mycursor.fetchall()

        mycursor.close()

        mydb.close()

        return data
    
    def update_set_ware(ID, status):  
        mydb =con()
        mycursor = mydb.cursor()
        sql = "UPDATE hard_ware SET status ='{}' WHERE ID ={}".format(status, ID)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True
    
    def select_ware(ID):  
        mydb =con()
        mycursor = mydb.cursor()
        sql = "SELECT * FROM hard_ware WHERE ID ={}".format(ID)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def ADD_Hard_Ware(name, HW_name):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hard_ware (ID, name, HW_name,status, value) VALUE (0, '{}','{}','เปิด',2.00);".format(name, HW_name)
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID
        
    # def delete_from_were(ID):
    #     mydb = con()
    #     mycursor = mydb.cursor(dictionary=True)
    #     sql = "DELETE FROM hard_ware WHERE ID
    #     mycursor.execute(sql)
    #     mydb.commit()
    #     data = mycursor.fetchall()
    #     return data
       