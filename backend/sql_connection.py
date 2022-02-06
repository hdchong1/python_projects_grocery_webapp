import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='steady#22GTfast', database='heroku_c05e3518c49ce58')

  return __cnx

