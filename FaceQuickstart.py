import cognitive_face as CF

KEY = '51c2bc53e2934661a26f924a280b4c91'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

BASE_URL = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
#img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlORIsX6ONEY_R6OnNxJsID-tXqDqxbKpW5Oz0Cwm52pHg0z2F'
faces = CF.face.detect(img_url)
print(faces)