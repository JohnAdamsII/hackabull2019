
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'c326783a810a441794afdc421326aa37',
}

params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'gender',
})

def getFaceIdandGender(Image_URL):

    body = "{ 'url': '%s' }" %(Image_URL)

    conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()

    data = str(response.read())
    clean_data = data[3:len(data)-2]

    j = json.loads(clean_data)
    faceID = j["faceId"]
    Gender = j["faceAttributes"]["gender"]
  
    conn.close()

    return (faceID,Gender)

if __name__ == '__main__':
    student = getFaceIdandGender('http://pretty-hairstyles.com/wp-content/uploads/2016/02/Leonardo-di-Caprio-celebrity-hairstyles-2004.jpg')
    print(student)
####################################

