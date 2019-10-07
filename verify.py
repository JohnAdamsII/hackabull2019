########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from detect import getFaceIdandGender

subscription_key = '5f28870ff1f34db39ace7176e72f3f8e'
assert subscription_key

conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')

headers = {
    # Request headers
    'Content-Type': 'application/json', 
    'Ocp-Apim-Subscription-Key': subscription_key
}

#params = urllib.parse.urlencode({
    # "returnFaceId": 'true',
    # "returnFaceLandmarks": 'false',
    # "returnFaceAttributes": 'age',
#})

def verify(Student,Unknown_Student):
    """ takes in two URLS to images compares to see if they are the same person """

    params=""

    body = "{ 'faceId1': '%s', 'faceId2': '%s' }" %(Student.faceId, Unknown_Student.faceId)
   
    conn.request("POST", "/face/v1.0/verify%s" % params, body, headers)
    response = conn.getresponse()
    
    data = str(response.read())
    clean_data = data[2:len(data)-1]
    #print(clean_data)

    
    j = json.loads(clean_data)
    # print(j)
    isIdentical = bool(j["isIdentical"])
    confidence = round(j["confidence"]*100)
  

    print(Student.name+" has been Identified") if isIdentical else print("No Match found for "+Student.name)
    print("It is a " + str(confidence)+"% match.")

    conn.close()
    return(isIdentical,confidence)

    
if __name__ == '__main__':
    pass