########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from FaceQuickstart import detect
import time

conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'c326783a810a441794afdc421326aa37',
}

params = urllib.parse.urlencode({
    # "returnFaceId": 'true',
    # "returnFaceLandmarks": 'false',
    # "returnFaceAttributes": 'age',
})

faceId1 = detect('https://specials-images.forbesimg.com/imageserve/558c0172e4b0425fd034f8ba/440x0.jpg?fit=scale&background=000000')
faceId2 = detect('http://pretty-hairstyles.com/wp-content/uploads/2016/02/Leonardo-di-Caprio-celebrity-hairstyles-2004.jpg')
print(faceId1)
print(faceId2)
body = "{ 'faceId1': '%s', 'faceId2': '%s' }" %(faceId1, faceId2)
print(body)
#body = "{ 'faceId1': '19e78ae6-bf7b-4ba8-9aad-f3377f39384f', 'faceId2': '5d4dc282-58b7-4aeb-9edb-14ac56f6f150' }"

conn.request("POST", "/face/v1.0/verify%s" % params, body, headers)
response = conn.getresponse()
data = response.read()

new_data = str(data)
final_data = new_data[2:len(new_data)-1]

print(final_data)

j = json.loads(final_data)
isIdentical = j["isIdentical"]
confidence = j["confidence"]

print(isIdentical)
print(confidence)


conn.close()
#except Exception as e:
    #print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

# {"faceIds": "'96e5e68a-9b60-4b02-8ed6-b796e45cd21d', 'db64a557-01f1-4d0c-8840-94baaa3d06b0'"}