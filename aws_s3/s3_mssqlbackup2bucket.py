# importing Packages
import pyodbc
import os
import datetime
import boto3
import glob


# define the backup paths
server_backup_path = 'c:\\mssql_backup\\'
date = datetime.datetime.utcnow().strftime('%d%m%Y')

# Connection MSSQL object (notice that i dont include the database name)
connx = pyodbc.connect('DRIVER={SQL Server};SERVER=ServerName\MSSQLEXPRESS;Trusted_Connection=yes', autocommit=True)

# List databases function
def list_databases(connx_obj):
  dbs = []
  cur = connx_obj.cursor()
  result = cur.execute('SELECT name from sysdatabases').fetchall()
  cur.close()
  for db in result:
    dbs.append(db[0])
  return dbs

# Backup databases
def backup_db(connx_obj, db_name, server_backup_path):

  cur = connx_obj.cursor()
  try:
   
    cur.execute('BACKUP DATABASE ? TO DISK=?', [db_name, server_backup_path + db_name + '_'+ date + r'_sql.bak'])
    while cur.nextset(): 
      pass
    cur.close()
  except:
    print('cant backup: ' + db_name)

# take the list
dbs = list_databases(connx)

# take backup for each database
for db in dbs:
  backup_db(connx, db, server_backup_path)

connx.close() # close the connection


'''
Backed up mssql data movement to S3 Bucket

'''
# Intialize S3 module and define variable #
mybucket = boto3.resource('s3', aws_access_key_id = 'MyAccessKey',   
aws_secret_access_key = 'MySecretAccessKey')     # S3 Bucket authentication #
fileName=os.listdir('C:\mssql_backup')
dataPath=("C:\\mssql_backup\\test_db_30052019_sql.bak")
myBucket='mybucket'

# Defining Condition for File movement from localdist to S3 movement 
for file in fileName:
	mybucket.meta.client.upload_file(dataPath, myBucket, file)
else:
	print("No file available for movement")

# Performing Folder Cleanup
Junk = glob.glob('c:\mssql_backup\*')
for garbage in Junk:
    os.remove(garbage)
else:
    print('All Items are trashed successfully')