from sqlalchemy import create_engine

hostname = 'localhost@postgres'
user = 'postgres'
password = 'root'
dbname = 'warehouse'
port = 5432

def connect_to_db():
    return create_engine(f'postgresql+pg8000://'
                         f'{user}:'
                         f'{password}@'
                         f'{hostname}:'
                         f'{port}/'
                         f'{dbname}')

print(connect_to_db())