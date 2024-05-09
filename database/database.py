import pymysql.cursors
import pymysql

host = '127.0.0.1'  # хост
user = 'root'
password = 'root'
db_name = 'users'


async def db_start():
    global connection, cursor
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = connection.cursor()
    create_table_query = "CREATE TABLE IF NOT EXISTS users(id int AUTO_INCREMENT," \
                         "tg_id varchar(32)," \
                         "category varchar(32)," \
                         "price_rub int," \
                         "price_y int, PRIMARY KEY (id));" \
                         # "time varchar(32), PRIMARY KEY (id));"
    cursor.execute(create_table_query)
    connection.commit()


async def calc_try(tg_id, category, price_rub, price_y):
    insert_values = f"INSERT INTO users (tg_id, category, price_rub, price_y)" \
                    f" VALUES ('{tg_id}', '{category}', {price_rub}, {price_y})"
    cursor.execute(insert_values)
    connection.commit()
