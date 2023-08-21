import psycopg2
from config import host,user,dbname,password
try:
    # Код, который может вызвать исключение
    connection = psycopg2.connect(
        host=host,
        database=dbname,
        user=user,
        password=password
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM book")
    result = cursor.fetchall()
    print(result)

except Exception as e:
    # Блок обработки исключения
    print("Произошла ошибка:", e)

finally:
    # Код, который выполняется всегда
    cursor.close()
    connection.close()