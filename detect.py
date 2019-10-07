
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

"""
Endpoint: https://westcentralus.api.cognitive.microsoft.com/face/v1.0

Key 1: 5f28870ff1f34db39ace7176e72f3f8e

Key 2: af3e8c15c7054c69a0071102724d9997
"""

# set to your own subscription key value
subscription_key = '5f28870ff1f34db39ace7176e72f3f8e'
assert subscription_key


headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'gender',
})

def getFaceIdandGender(Image_URL):
    # print(Image_URL)

    body = "{ 'url': '%s' }" %(Image_URL)

    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()

    data = str(response.read())
    clean_data = data[3:len(data)-2]

    j = json.loads(clean_data) #need exception handling here
    faceID = j["faceId"]
    Gender = j["faceAttributes"]["gender"]
  
    conn.close()

    return (faceID,Gender)

if __name__ == '__main__':
    student = getFaceIdandGender('http://pretty-hairstyles.com/wp-content/uploads/2016/02/Leonardo-di-Caprio-celebrity-hairstyles-2004.jpg')
    print(student)
####################################

