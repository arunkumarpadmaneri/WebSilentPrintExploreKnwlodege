import sqlite3

def get_conn(dbname):
	conn = sqlite3.connect(dbname)
	print ("connection opened",conn)
	return conn

def exec_query(type,conn,query):
	response = None
	if conn and query:
		if type =="fetch":
			response = exec_fetch_query(conn,query)
		else:
			response = exec_insert_or_update(conn,query)
	else:
		print("query is empty")
		conn.close()
	return response

def exec_fetch_query(conn,query):
	data=[]
	cursor=conn.execute(query)
	for row in cursor:
		data.append(row)
	return data
	conn.close()

def exec_insert_or_update(conn,query):
	conn.execute(query)
	conn.commit()
	conn.close()

