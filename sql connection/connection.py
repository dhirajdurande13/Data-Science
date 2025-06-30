# Sqlite:self contained serverless and zero configuration database engine widely used for database emeded systems.

import sqlite3

# Connection

connection=sqlite3.connect("example.db")
print(connection)


# creating table in database cursor,execute cursor commit connection

cursor=connection.cursor()

cursor.execute(
    '''Create table If Not Exists employee(
        emp_id Integer primary key,
        emp_name Text Not Null,
        age Integer,
        department Integer
        
        )'''
)

connection.commit()



# cursor.executemany(
#     '''insert into employee(emp_id,emp_name,age,department) values(
#         ?,?,?,?)''',
#         [
#             (18,"RIshi",21,"Comp"),
#         (19,"Mahesh",46,"Cinema"),
#         (21,"PK",46,"Cinema")
#         ]
# )
# connection.commit()
cursor.execute("PRAGMA table_info(employee)")


result=cursor.fetchall()

for row in result:
    print(row)
    
    
cursor.execute(
    '''Select * from employee'''
)
result=cursor.fetchall()

for row in result:
    print(row)



cursor.execute(
    '''
    Update employee 
    set age=22
    where emp_name='RIshi'
    '''
)
 
 
cursor.execute(
    '''Delete from employee
    where emp_name="PK"
    '''
)   
cursor.execute(
    '''Select * from employee'''
)
result=cursor.fetchall()

for row in result:
    print(row)

