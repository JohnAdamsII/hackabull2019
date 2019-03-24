from detect import getFaceIdandGender
from verify import verify



class StudentInfo:
    def __init__(self, name, URL):
        self.name = name
        self.URL = URL
        # commented out to not hit the limit on requests
        # self.faceId, self.gender = getFaceId(URL)
        self.absent = True

class UnknownInfo:
    def __init__(self, URL):
        self.URL = URL
        # commented out to not hit the limit on requests
# self.faceId, self.gender = getFaceId(URL)

Students = []
UnknownStudents = []

with open("studentDatabase.txt", "r") as readFile:
    for line in readFile:
            currentLine = line.strip().split(",")
            Students.append( StudentInfo(currentLine[0].strip(), currentLine[1].strip()) )

with open("snapshots.txt", "r") as readFile:
    for line in readFile:
        currentLine = line.strip().split(",")
UnknownStudents.append( currentLine[1].strip() )

#[print(x.name,x.URL) for x in Students]

for items in Students:
    print(items.URL)
    FaceID = getFaceIdandGender(items.URL)


