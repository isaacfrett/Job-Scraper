import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="JobScraper"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Jobs (title VARCHAR(100), company VARCHAR(50), location VARCHAR(50), jobID int PRIMARY KEY AUTO_INCREMENT)")


def AddEntries(self, jobtitle, company, location):
    self = self
    job = jobtitle
    comp = company
    loc = location
    for entry in job_list:
        mycursor.execute("INSERT INTO Jobs (title, company, location) VALUES ({job}, {comp}, {loc})")


#mycursor.commit()

# mycursor.execute("SELECT # FROM Jobs")
for x in mycursor:
    print(x)