
### Modify this file to write to your own database

table_name = "json_parse_alexander"

usn = "postgres"
pw = "admin"
url = "localhost"
port = "2304"
db_name = "json-data"

DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(usn, pw, url, port, db_name)