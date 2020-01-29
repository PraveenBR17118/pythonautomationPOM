'''
Created on 27-Jan-2020

@author: praveen
'''
import cx_Oracle

import os 

os.environ['PATH']= "/Users/praveen/Documents/Softwares/instantclient_19_3"

#Establishing connection to the database

con = cx_Oracle.connect("hr","hr","localhost/pdborcl")

print("Connceted")

con.close()