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
    mila_URL = "https://www.newdvdreleasedates.com/images/profiles/mila-kunis-01.jpg"
    leo_URL = "https://specials-images.forbesimg.com/imageserve/558c0172e4b0425fd034f8ba/440x0.jpg?fit=scale&background=000000"

    # mila = getFaceIdandGender(mila_URL)
    # leo = getFaceIdandGender(leo_URL)
    leo = StudentInfo("leo",leo_URL)
    mila = StudentInfo("mila", mila_URL)

    compare = verify(mila,leo)
    # Students = []
    # UnknownStudents = []

    # with open("studentDatabase.txt", "r") as readFile:
    #     for line in readFile:
    #             currentLine = line.strip().split(",")
    #             Students.append( StudentInfo(currentLine[0].strip(), currentLine[1].strip()) )

    # with open("snapshots.txt", "r") as readFile:
    #     for line in readFile:
    #         currentLine = line.strip().split(",")
    #         UnknownStudents.append( UnknownInfo(currentLine[1].strip()) )

   
    # print("Please wait Microsoft's free tier only allows 20 API requests per minute...\n")
    # time.sleep(60)

    # for Unknown_Students in UnknownStudents:
    #     for Known_Students in Students:
    #         if Unknown_Students.gender != Known_Students.gender:
    #             continue
    #         if not(Known_Students.absent):
    #             continue
    #         if verify(Known_Students,Unknown_Students)[0]:
    #             Known_Students.absent = False 
    #             break

if __name__ == "__main__":
    main()




