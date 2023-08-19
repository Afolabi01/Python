# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 01:20:23 2023

@author: Afolabi
"""

import sqlite3

conn = sqlite3.connect('INSTRUCTOR.db')
cursor_obj = conn.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

table = "CREATE TABLE IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARHAR(20), CCODE CHAR(2));"

cursor_obj.execute(table)
print("Table is Ready")

cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')

cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')

#the fecthall function returns all records in the row...
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)
  
  
#to fetch just some/a number of rows use the fetchmany function(fetchmany(n), where n is number of rows needed)
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement) 
print("All the data")
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)
  
#to update a value in the table
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)
  
#using pandas to query the database
import pandas as pd
df = pd.read_sql_query("select * from instructor;", conn)
df
  