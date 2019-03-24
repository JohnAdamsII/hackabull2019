from detect import getFaceIdandGender
from verify import verify
import time

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('mlh hackAbull AttendanceSheet-e713af6542e0.json', scope)
client = gspread.authorize(credentials)

# Find a workbook by name and open the first sheet
sheet = client.open('Attendance Sheet').sheet1

class StudentInfo:
    def __init__(self, name, URL):
        self.name = name
        self.URL = URL
        # commented out to not hit the limit on requests
        self.faceId, self.gender = getFaceIdandGender(URL)
        self.absent = True

class UnknownInfo:
    def __init__(self, URL):
        self.URL = URL
        # commented out to not hit the limit on requests
        self.faceId, self.gender = getFaceIdandGender(URL)

Students = []
UnknownStudents = []

with open("studentDatabase.txt", "r") as readFile:
    for line in readFile:
            currentLine = line.strip().split(",")
            Students.append( StudentInfo(currentLine[0].strip(), currentLine[1].strip()) )

with open("snapshots.txt", "r") as readFile:
    for line in readFile:
        currentLine = line.strip().split(",")
        UnknownStudents.append( UnknownInfo(currentLine[1].strip()) )

#####UPLOAD to google sheet
allfile_data = sheet.get_all_values()
sheet.update_cell(1, 5, datetime.datetime.today().strftime('%d-%m-%Y')) #Addes today's date

print("Please wait.....")
time.sleep(60)

for Unknown_Students in UnknownStudents:
    for Known_Students in Students:
        if Unknown_Students.gender != Known_Students.gender:
            continue
        if not(Known_Students.absent):
            continue
        if verify(Known_Students,Unknown_Students)[0]:
            print(Known_Students.name+" is here!")
            Known_Students.absent = False 
            break
            
for student in Students:
    #print(student.name, student.absent)
    for x in range(1, len(allfile_data)):
        #print(allfile_data[x][0])
        if allfile_data[x][0] == student.name and student.absent == False:
            sheet.update_cell(x+1, len(allfile_data[0])+1, "Present")
            print('------------------------------------------------\n')
            print ("Marked " + allfile_data[x][0] + " as present on your google sheet.")
    
    #for y in UnknownStudents:
        #print(y.URL)
        #
        #print(comparsion)
        #if comparsion[1] > 75:
            #print("FOUND LEO!")
       
    #break

#print(Students[0])
#print(Students)

#for items in UnknownStudents:
    #comparsion = verify(Student.URL[0],items.URL)
    #print(comparsion)
    #if comparsion[1] > 75:
        #print("FOUND LEO!")




