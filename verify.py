########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'c326783a810a441794afdc421326aa37',
}

params = urllib.parse.urlencode({
})

body = "{ 'url': 'https://specials-images.forbesimg.com/imageserve/558c0172e4b0425fd034f8ba/440x0.jpg?fit=scale&background=000000' }"
body1 = "{ 'url': 'http://pretty-hairstyles.com/wp-content/uploads/2016/02/Leonardo-di-Caprio-celebrity-hairstyles-2004.jpg' }"
bodies = []
bodies.append(body)
bodies.append(body1)

try:
    conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/verify?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################