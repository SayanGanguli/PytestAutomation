import os
import cx_Oracle

#os.environ['Path'] = 'D:\Documents\Software\instantclient_19_14'
conn = cx_Oracle.connect('system/orcl@localhost:1521/orcl')
print(conn.version)
conn.close()
