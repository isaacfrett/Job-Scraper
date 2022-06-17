import mysql.connector
from Scraper import entries

#This will establish our conenction to our SQL server and initalize our database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="JobScraper"
)

mycursor = db.cursor(buffered = True)

#This will create an SQL Table with 4 columns including and ID for our primary key
#mycursor.execute("CREATE TABLE Jobs (title VARCHAR(100), company VARCHAR(50), location VARCHAR(50), jobID int PRIMARY KEY AUTO_INCREMENT)")

#This function will bring in data from our Scraper.py file to convert it into our data table

def addEntries():
    for entry in entries:
        title = entry[0]
        company = entry[1]
        location = entry[2]
        if entry != mycursor.execute("SELECT * FROM Jobs"):
            mycursor.execute("INSERT INTO Jobs (title, company, location) VALUES (%s,%s,%s)", (title, company, location))
        else:
            pass
addEntries()

db.commit()
# mycursor.execute("SELECT * FROM Jobs WHERE location = 'Remote'")
# for x in mycursor:
#     print(x)