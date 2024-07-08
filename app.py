#!.venv/bin/python
import yaml
from mysql.connector.pooling import MySQLConnectionPool
from prettytable import from_db_cursor

# load config
with open('./config/debug.yaml', 'r') as f:
  config = yaml.load(f, Loader=yaml.FullLoader)

# mysql connection pool
mypool = MySQLConnectionPool(pool_name = "mypool", pool_size = 3, **config['mysql'])

def get_userinfo(user_id):
    query = ("SELECT username, realname,mobile_no, gender, create_time, operate_time, user_kind "
    "FROM `user`.`sys_user_t` "
    "WHERE `user_id`=%s")
    with mypool.get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (user_id,))
            data = cursor.fetchone()
    return data

def main():
    data = get_userinfo('0000015e31919747-00163e000b170001')
    print(data)


if __name__ == '__main__':
    main()