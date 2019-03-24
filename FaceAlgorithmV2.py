
import cognitive_face as CF
import requests
from io import BytesIO
from PIL import Image, ImageDraw
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import time


KEY = '3f5f46dbba524e8c9ad99d3a5a63e8c7'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# def getFaceId(img_url):
#     # You can use this example JPG or replace the URL below with your own URL to a JPEG image.
#     faces = CF.face.detect(img_url)
#     print(faces)
#     return(faces[0]['faceId'])

def getFaceId(img_url):
    headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '3f5f46dbba524e8c9ad99d3a5a63e8c7',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'gender',
    })
    body = "{ 'url': '%s' }" %(img_url)
    try:
        conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        # print(data)

        new_data = str(data)
        final_data = new_data[2:len(new_data)-1]
        final_data1 = final_data[1:len(final_data)-1]
        # print(final_data1)
        j = json.loads(final_data1)
        faceId = j["faceId"]
        # print(faceID)
        gender = j["faceAttributes"]["gender"]
        # print(Gender)
        return {faceId, gender}

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


########### Verify #############
def getIdentical(unknown, known):
    """unknown parameter is an UnknownInfo class, known is a StudentInfo class"""
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '3f5f46dbba524e8c9ad99d3a5a63e8c7',
    }

    params = urllib.parse.urlencode({
    })

    faceId1 = unknown.faceId
    faceId2 = known.faceId
    body = "{ 'faceId1': '%s', 'faceId2': '%s' }" %(faceId1, faceId2)
    #body = "{ 'faceId1': '96e5e68a-9b60-4b02-8ed6-b796e45cd21d', 'faceId2': '6a436021-2acc-4166-bb6f-09cc1058e6c9' }"
    #body = str({"faceId": "96e5e68a-9b60-4b02-8ed6-b796e45cd21d", "largeFaceListId": "sample_list", "maxNumOf CandidatesReturned": 10, "mode": "matchPerson"})
    try:
        conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/verify%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

########### Verify #############

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


# if ( len(lines) % 2 == 1 ):
#     print("Odd number of URLs")
#     exit()

# for i in range( 0, len(lines), 2 ):
#     getIdentical(lines[i], lines[i + 1])

# x = StudentInfo("Danielle","https://cdn.cliqueinc.com/cache/posts/271453/getting-ready-with-danielle-campbell-271453-1541016765335-main.700x0c.jpg")
# print(x.name)
# print(x.faceId)
# print(x.gender)
# print(x.absent)


# ########### Verify #############
# def getIdentical(unknown, known):
#     headers = {
#         # Request headers
#         'Content-Type': 'application/json',
#         'Ocp-Apim-Subscription-Key': '3f5f46dbba524e8c9ad99d3a5a63e8c7',
#     }

#     params = urllib.parse.urlencode({
#     })

#     faceId1 = getFaceId( unknown )
#     faceId2 = getFaceId( known )
#     body = "{ 'faceId1': '%s', 'faceId2': '%s' }" %(faceId1, faceId2)
#     #body = "{ 'faceId1': '96e5e68a-9b60-4b02-8ed6-b796e45cd21d', 'faceId2': '6a436021-2acc-4166-bb6f-09cc1058e6c9' }"
#     #body = str({"faceId": "96e5e68a-9b60-4b02-8ed6-b796e45cd21d", "largeFaceListId": "sample_list", "maxNumOf CandidatesReturned": 10, "mode": "matchPerson"})
#     try:
#         conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
#         conn.request("POST", "/face/v1.0/verify%s" % params, body, headers)
#         response = conn.getresponse()
#         data = response.read()
#         print(data)
#         conn.close()
#     except Exception as e:
#         print("[Errno {0}] {1}".format(e.errno, e.strerror))

# ########### Verify #############

# with open('links.txt') as f:
#     lines = f.read().splitlines()

# if ( len(lines) % 2 == 1 ):
#     print("Odd number of URLs")
#     exit()

# for i in range( 0, len(lines), 2 ):
#     getIdentical(lines[i], lines[i + 1])

