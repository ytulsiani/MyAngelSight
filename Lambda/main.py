from os import getenv
import pymysql
from pymysql.err import OperationalError
import requests
import logging
################################
# THINGS TO DO:
    # read from database
    # write to database 
    # do calculations in py file
#################################

def get_tsys():
    account_id = "00000022340"
    access_token = "BWx/gfXk0RpFthUECBO0W0mKvyRCrVTdTkbxdv+DKT4="    
    headers = {"Authorization": "Bearer BWx/gfXk0RpFthUECBO0W0mKvyRCrVTdTkbxdv+DKT4=",
            "Content-Type" : "application/json",
            "Accept" : "application/json"}
    url = "https://developers.tsys.com/sandbox/rewards/{}/information".format(account_id)

    result = requests.get(url, headers=headers)
    logger.warn(result.json())

def getActualChange(request):
    #accept their scoreChange input
    searchURL = ""
    data = requests.get(searchURL)
    data = data.json()
    ## NEED TO KNOW WHAT THE DATA LOOKS LIKE ##
    
# TODO(developer): specify SQL connection details
CONNECTION_NAME = getenv(
  'INSTANCE_CONNECTION_NAME')
DB_USER = getenv('MYSQL_USER')
DB_PASSWORD = getenv('MYSQL_PASSWORD')
DB_NAME = getenv('MYSQL_DATABASE')

mysql_config = {
  'user': DB_USER,
  'password': DB_PASSWORD,
  'db': DB_NAME,
  'charset': 'utf8mb4',
  'cursorclass': pymysql.cursors.DictCursor,
  'autocommit': True
}

# Create SQL connection globally to enable reuse
# PyMySQL does not include support for connection pooling
mysql_conn = None


def __get_cursor():
    """
    Helper function to get a cursor
      PyMySQL does NOT automatically reconnect,
      so we mus-t reconnect explicitly using ping()
    """
    try:
        return mysql_conn.cursor()
    except OperationalError:
        mysql_conn.ping(reconnect=True)
        return mysql_conn.cursor()


def mysql_demo(request):
    global mysql_conn
    # Initialize connections lazily, in case SQL access isn't needed for this
    # GCF instance. Doing so minimizes the number of active SQL connections,
    # which helps keep your GCF instances under SQL connection limits.
    if not mysql_conn:
        try:
            mysql_conn = pymysql.connect(**mysql_config)
        except OperationalError:
            # If production settings fail, use local development ones
            mysql_config['unix_socket'] = f'/cloudsql/{CONNECTION_NAME}'
            mysql_conn = pymysql.connect(**mysql_config)
    
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'userid' in request_json:
        userid = request_json['userid']
    elif request_args and 'userid' in request_args:
        userid = request_args['userid']
    if request_json and 'score' in request_json:
        score = request_json['score']
    elif request_args and 'score' in request_args:
        score = request_args['score']

    # Remember to close SQL resources declared while running this function.
    # Keep any declared in global scope (e.g. mysql_conn) for later reuse.
    with __get_cursor() as cursor:

        cursor.execute("SELECT userid, score FROM score WHERE userid=%s" % (userid))
        resultTup = cursor.fetchall()
        updatedScore = int(resultTup[0]["score"]) + int(score)
        if updatedScore >= 100:
            updatedScore = 50
            #call tsys
            get_tsys()
        elif updatedScore <= 0:
            updatedScore = 0
        updatedScore = str(updatedScore)
        final = cursor.execute("UPDATE score SET score = %s WHERE userid = %s" % (updatedScore, userid))
        
        return str(updatedScore)
if __name__=="__main__":
    mysql_demo({"userid": "1", "score":"1"})