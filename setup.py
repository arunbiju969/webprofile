import os
os.system('pip install -r requirements.txt')
from decouple import config
import psycopg2


def postgres_test():
    try:
        conn = psycopg2.connect(f"dbname='postgres' user='postgres' host='{config('DB_HOST')}' password='{config('DB_PASS')}' connect_timeout=1 ")
        conn.close()
        return True
    except:
        return False


def env_setup(initial):
    if initial:
        print('Running Setup')
    else:
        print('Database Connection not Established, reconfiguring. Make sure to to enter correct value for\n DB_HOST AND DB_PASS')
    try:
        os.remove('.env')  
        print('Deleting and recreating .env file')
    except:
        print('.env file does not exist, creating')
    key = input('Enter Django Secret Key generated from "https://djecrety.ir/"  : ')
    os.system('clear')
    db_host = input('Enter DB HOST  : ')
    os.system('clear')
    db_pass = input('Enter DB Password  : ')
    new_env = open(".env", "x", encoding="utf-8")
    new_env.write(f"DEBUG=True\nALLOWED_HOSTS='*'\nSECRET_KEY='{key}'\nDB_HOST='{db_host}'\nDB_PASS='{db_pass}'")
    new_env.close()


env_setup(initial=True)
os.system('python manage.py migrate')
os.system('python manage.py loaddata whole.json')

if postgres_test():
    print ('Database Connection Successfully Established')

else:
    print ('Database Connection not established, \nplease confirm correctness of Database Host and password value and re-run \'python setup.py\'')





  
