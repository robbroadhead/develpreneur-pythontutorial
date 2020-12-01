import mysql
from mysql.connector import Error

# 2. Variables in Python
myOutput = "This is a program"

# 1. How to output a string or value
print(myOutput)

dayType = "Rainy"
dayType2 = "Cold"
# 4. Formatting strings
print("Today is a {} and {} day".format(dayType,dayType2))

    
    
# 3. This is an array
myArray = ['A','B','C']

# This is a range (starts with 0 by default)
rng = range(5,11)

for item in myArray:
    print("Letter is {}".format(item))

for index in rng:
    print(index)


# 5. Defining Functions
def myFunction(value):
    print(value*2)
    return [1,2,3,4,5]
    
# 4. For Loops
for index in range(10):
    print(myFunction(index))
    
config = {
    'user' : 'root',
    'password': 'develpreneur',
    'host': '127.0.0.1',
    'database': 'dpproject',
    'raise_on_warnings': True
}
db = mysql.connector.connect(**config)
cursor = db.cursor()
try:
    sql = "select first_name,last_name,email from auth_user"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        print("Email Address is: {}".format(row[2]))
except Error as e:
    print(e)



print("End Of Program")

#  a. Verify your pthon version (python3 -V or python -V)
#  b. Create a python program to output your name and then print an array of your favorite foods.