import cognitive_face as CF

KEY = 'c326783a810a441794afdc421326aa37'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'

URL1 = 'https://specials-images.forbesimg.com/imageserve/558c0172e4b0425fd034f8ba/440x0.jpg?fit=scale&background=000000'
URL2 = 'http://pretty-hairstyles.com/wp-content/uploads/2016/02/Leonardo-di-Caprio-celebrity-hairstyles-2004.jpg'

def detect(Img_url):
    """ takes in URL (photo) and returns its face id """
    faces = CF.face.detect(Img_url)
    faceid = faces[0]['faceId']
    return faceid


print(URL1)
myid1 = detect(URL1)
print(URL2)
myid2 = detect(URL2)

print(myid1)
print(myid2)


#j = json.loads(data)
#print(j["faceid"])