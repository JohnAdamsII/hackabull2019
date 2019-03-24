########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from detect import getFaceIdandGender

conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'c326783a810a441794afdc421326aa37',
}

#params = urllib.parse.urlencode({
    # "returnFaceId": 'true',
    # "returnFaceLandmarks": 'false',
    # "returnFaceAttributes": 'age',
#})

def verify(Student,Unknown_Student):
    """ takes in two URLS to images compares to see if they are the same person """

    params=""

    # Student = getFaceIdandGender(Student)
    # Unknown_Student = getFaceIdandGender(Unknown_Student)

    body = "{ 'faceId1': '%s', 'faceId2': '%s' }" %(Student.faceId, Unknown_Student.faceId)
   
    conn.request("POST", "/face/v1.0/verify%s" % params, body, headers)
    response = conn.getresponse()
    
    data = str(response.read())
    clean_data = data[2:len(data)-1]
    #print(clean_data)

    
    j = json.loads(clean_data)
    isIdentical = bool(j["isIdentical"])
    confidence = round(j["confidence"]*100)
  

    print("It's a match!") if isIdentical else print("Match not found")
    print("I am " + str(confidence)+"% sure of this decision.")

    conn.close()
    return(isIdentical,confidence)

    
if __name__ == '__main__':
    pass
    #verify('https://specials-images.forbesimg.com/imageserve/558c0172e4b0425fd034f8ba/440x0.jpg?fit=scale&background=000000','http://pretty-hairstyles.com/wp-content/uploads/2016/02/Leonardo-di-Caprio-celebrity-hairstyles-2004.jpg')
#except Exception as e:
    #print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

# {"faceIds": "'96e5e68a-9b60-4b02-8ed6-b796e45cd21d', 'db64a557-01f1-4d0c-8840-94baaa3d06b0'"}