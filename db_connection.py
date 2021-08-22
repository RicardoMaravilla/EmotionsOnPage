import pymysql

def db_connect():
    ############### CONFIGURAR ESTO ###################
    # Abre conexion con la base de datos
    db = pymysql.connect("database_host","username","password","database_name")
    ##################################################

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # ejecuta el SQL query usando el metodo execute().
    cursor.execute("SELECT VERSION()")

    # procesa una unica linea usando el metodo fetchone().
    data = cursor.fetchone()
    print ("Database version : {0}".format(data))
    # Prepare SQL query to READ a record into the database.
    sql = "SELECT * FROM test \
    WHERE id > {0}".format(0)

    # Execute the SQL command
    cursor.execute(sql)

    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
    id = row[0]
    name = row[1]
    email = row[2]
   # Now print fetched result
   print ("id = {0}, name = {1}, email = {1}".format(id,name,email))

    # desconecta del servidor
    db.close()