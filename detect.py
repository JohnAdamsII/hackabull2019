
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

body = "{ 'url': 'https://specials-images.forbesimg.com/imageserve/558c0172e4b0425fd034f8ba/440x0.jpg?fit=scale&background=000000' }"
body1 = "{ 'url': 'http://pretty-hairstyles.com/wp-content/uploads/2016/02/Leonardo-di-Caprio-celebrity-hairstyles-2004.jpg' }"
bodies = []
bodies.append(body)
bodies.append(body1)


for items in bodies:
    try:
        conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, items, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)

        new_data = str(data)
        final_data = new_data[2:len(new_data)-1]
        #print(final_data)
        final_data1 = final_data[1:len(final_data)-1]
        print(final_data1)
        j = json.loads(final_data1)
        faceID = j["faceId"]
        print(faceID)
        Gender = j["faceAttributes"]["gender"]
        print(Gender)
        #conn.close()

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


####################################

