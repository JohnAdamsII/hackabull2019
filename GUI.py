import tkinter
import urllib.request
from PIL import Image, ImageTk
from io import BytesIO
import time



def URL2img(URL):
    response = urllib.request.urlopen(URL)
    data = response.read()

    img = Image.open(BytesIO(data))
    img = img.resize((500,500), Image.ANTIALIAS)

    return ImageTk.PhotoImage(img)

def makeImgLabel(image):

    label = tkinter.Label(window,image=image, borderwidth=2, relief='solid')
    label.image = image
    return label


window = tkinter.Tk()

window.geometry("1200x900")
window.title("Face Matcher")

mila_URL = "https://www.newdvdreleasedates.com/images/profiles/mila-kunis-01.jpg"
mila = URL2img(mila_URL)
label = makeImgLabel(mila)
label.place(x=50,y=200)

leo_URL = "https://specials-images.forbesimg.com/imageserve/558c0172e4b0425fd034f8ba/440x0.jpg?fit=scale&background=000000"
leo = URL2img(leo_URL)
label = makeImgLabel(leo)
label.place(x=625,y=200)

window.mainloop()