########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '3f5f46dbba524e8c9ad99d3a5a63e8c7',
}

params = urllib.parse.urlencode({
    # "returnFaceId": 'true',
    # "returnFaceLandmarks": 'false',
    # "returnFaceAttributes": 'age',
})

#url1 = input()
#url2 = input()
#body = "{ 'url': 'https://i.pinimg.com/originals/b2/cc/74/b2cc74eb9def94c32fdf51beb33d1869.jpg' }"
body = "{ 'faceId1': '96e5e68a-9b60-4b02-8ed6-b796e45cd21d', 'faceId2': '6a436021-2acc-4166-bb6f-09cc1058e6c9' }"
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

####################################

# {"faceIds": "'96e5e68a-9b60-4b02-8ed6-b796e45cd21d', 'db64a557-01f1-4d0c-8840-94baaa3d06b0'"}