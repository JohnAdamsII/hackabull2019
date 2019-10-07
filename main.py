from detect import getFaceIdandGender
from verify import verify
import time
import datetime

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


def main():
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


    print("Please wait Microsoft's free tier only allows 20 API requests per minute...\n")
    time.sleep(60)

    for Unknown_Students in UnknownStudents:
        for Known_Students in Students:
            if Unknown_Students.gender != Known_Students.gender:
                continue
            if not(Known_Students.absent):
                continue
            if verify(Known_Students,Unknown_Students)[0]:
                Known_Students.absent = False 
                break

if __name__ == "__main__":
    main()




