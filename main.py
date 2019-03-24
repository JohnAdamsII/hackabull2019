from detect import getFaceIdandGender
from verify import verify
import time



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

#[print(x.URL) for x in Students]


#for y in UnknownStudents:
    #print(y.URL)

time.sleep(60)
for Unknown_Students in UnknownStudents:
    for Known_Students in Students:
        if Unknown_Students.gender != Known_Students.gender:
            print
            continue
        if not(Known_Students.absent):
            continue
        if verify(Known_Students,Unknown_Students)[0]:
            print(Known_Students.name+" is here!")
            Known_Students.absent = False 
            break
            

    
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




